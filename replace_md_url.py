import re
import os

def replace_image_links_in_directory(directory, old_link_prefix, new_link_prefix):
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
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
directory_path = 'd:/notes/study/miscellaneous'
old_link_prefix = 'img.xiansakana.xyz'
new_link_prefix = 'cdn.cbd.int/xiansakana-blog-img'

# 执行替换操作
replace_image_links_in_directory(directory_path, old_link_prefix, new_link_prefix)
