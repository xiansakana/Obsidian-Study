import re
import os

def replace_image_links_in_directory(directory, old_link_prefix, new_link_prefix):
    # 遍历目录下的所有文件和子文件夹
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # 仅处理Markdown文件
            if filepath.endswith('.md'):
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 使用正则表达式替换图片链接
                new_content = re.sub(old_link_prefix, new_link_prefix, content)
                
                # 将替换后的内容写回文件
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)

# 指定目录和需要替换的链接前缀
directory_path = 'd:/notes/study/itheima/最新版JavaWeb开发教程'
# old_link_prefix = 'img.xiansakana.xyz'
old_link_prefix = 'assets/'
# old_link_prefix = 'zui-xin-ban-java-web-kai-fa-jiao-cheng1.0.2/assets2/'
# old_link_prefix = 'cdn.cbd.int/xiansakana-blog-img'
# old_link_prefix = 'cdn.jsdelivr.net/npm/xiansakana-blog-img'

# new_link_prefix = 'img.xiansakana.xyz'
# new_link_prefix = 'cdn.cbd.int/xiansakana-blog-img'
# new_link_prefix = 'cdn.jsdelivr.net/npm/xiansakana-blog-img'
new_link_prefix = 'https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.2/assets/'
# new_link_prefix = 'zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.2/assets2/'
# 执行替换操作
replace_image_links_in_directory(directory_path, old_link_prefix, new_link_prefix)
