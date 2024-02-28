#!/usr/bin/env -S -P${HOME}/anaconda/bin python
# -*- coding:utf-8 -*-
 
import re, os, shutil, time, sys, argparse
from itertools import chain
import oss2
 
# 需要替换url的MD文件
md_file = ''
 
# 操作类型, L2L (默认本地到本地)， L2W（本地到图床）， W2L（图床到本地）
action = 'L2L'
 
# 保存图片文件的根目录
dir_base = '/*******/_MD_Media'
 
# Markdown中图片语法 ![](url) 或者 <img src='' />
img_patten = r'!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>'
 
 
def get_img_local_path(md_file, path):
    """
    获取MD文件中嵌入图片的本地文件绝对地址
    :param md_file: MD文件
    :param path: 图片URL
    :return: 图片的本地文件绝对地址
    """
 
    result = None
 
    # /a/b/c
    if path.startswith('/'):
        result = path
    # ./a/b/c
    elif path.startswith('.'):
        result = '{0}/{1}'.format(os.path.dirname(md_file), path)
    # file:///a/b/c
    elif path.startswith('file:///'):
        result = path[8:]
        result = result.replace('%20',' ')
    else:
        result = '{0}/{1}'.format(os.path.dirname(md_file), path)
 
    return result
 
def local_2_local(md_file, dir_ts, match):
    """
    把MD中的本地图片移动到指定目录下，并返回URL。 这里并没有进行URL的替换
    :param md_file:
    :param dir_ts:
    :param match:
    :return: new_url，新本地文件地址。如果不需要替换，就返回空
    """
    dir_tgt = '{0}/{1}'.format(dir_base, dir_ts)
    new_url = None
    # 判断是不是已经是一个图片的网址，或者已经在指定目录下
    if not (re.match('((http(s?))|(ftp))://.*', match) or re.match('{}/.*'.format(dir_base), match)):
        # 如果图片url是本地文件，就替换到指定目录
        img_file = get_img_local_path(md_file, match)
        if os.path.isfile(img_file):
            new_url = '{0}/{1}'.format(dir_tgt, os.path.basename(match))
            os.makedirs(dir_tgt, exist_ok=True)
            # 移动物理文件
            shutil.move(img_file, dir_tgt)
 
    return new_url
 
def local_2_web(md_file, dir_ts, match):
    """
    把MD中的本地图片上传到OSS下，并返回URL。 这里并没有进行URL的替换
    :param md_file:
    :param dir_ts:
    :param match:
    :return: new_url，新本地文件地址。如果不需要替换，就返回空
    """
 
    # 阿里云OSS信息
    bucket_name = "b******ce"
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    access_key_id = "******"
    access_key_secret = "******"
    web_img_prfix = 'https://******.oss-cn-beijing.aliyuncs.com'
    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
 
    new_url = None
    # 判断是不是已经是一个图片的网址
    if not (re.match('((http(s?))|(ftp))://.*', match) ):
        # 如果图片url是本地文件，就上传
        img_file = get_img_local_path(md_file, match)
        if os.path.isfile(img_file):
            key_url = '{0}/{1}'.format(dir_ts, os.path.basename(match))
            bucket.put_object_from_file(key_url, img_file)
            new_url = '{}/{}'.format(web_img_prfix, key_url)
 
    return new_url
 
def replace_md_url(md_file):
    """
    把指定MD文件中引用的图片移动到指定地点（本地或者图床），并替换URL
    :param md_file: MD文件
    :return:
    """
 
    if os.path.splitext(md_file)[1] != '.md':
        print('{}不是Markdown文件，不做处理。'.format(md_file))
        return
 
    cnt_replace = 0
    # 本次操作时间戳
    dir_ts = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
 
    with open(md_file, 'r',encoding='utf-8') as f: #使用utf-8 编码打开
        post = f.read()
        matches = re.compile(img_patten).findall(post)
        if matches and len(matches)>0 :
            # 多个group整合成一个列表
            for match in list(chain(*matches)) :
                if match and len(match)>0 :
                    new_url = None
 
                    # 进行不同类型的URL转换操作
                    if action == 'L2L':
                        new_url = local_2_local(md_file, dir_ts, match)
                    elif action == 'L2W':
                        new_url = local_2_web(md_file, dir_ts, match)
 
                    # 更新MD中的URL
                    if new_url :
                        post = post.replace(match, new_url)
                        cnt_replace = cnt_replace + 1
 
        # 如果有内容的话，就直接覆盖写入当前的markdown文件
        if post and cnt_replace > 0:
            open(md_file, 'w', encoding='utf-8').write(post)
            print('{0}的{1}个URL被替换到<{2}>/{3}'.format(os.path.basename(md_file), cnt_replace, action, dir_ts))
        elif cnt_replace == 0:
            print('{}中没有需要替换的URL'.format(os.path.basename(md_file)))
 
 
 
 
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
 
    parser.add_argument('-f', '--file', help='文件Full file name ofMarkdown file.')
    parser.add_argument('-a', '--action', help='操作类型： L2L, L2W, W2L .')
    parser.add_argument('-d', '--dir', help='Base directory to store MD images.')
 
    args = parser.parse_args()
 
    if args.action:
        action = args.action
    if args.dir:
        dir_base = args.dir
    if args.file:
        replace_md_url(args.file)
 
 
