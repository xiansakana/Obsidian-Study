import os
import shutil

# 源文件夹路径
source_dir = r'D:\notes\study'
# 目标文件夹路径
target_dir = r'D:\Hexo\source\_posts'

# 遍历源文件夹
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # 检查文件扩展名是否为.md
        if file.endswith('.md'):
            # 构建源文件的完整路径
            source_file = os.path.join(root, file)
            # 构建目标文件的完整路径
            target_file = os.path.join(target_dir, file)
            
            # 复制文件
            shutil.copy2(source_file, target_file)
            print(f'文件 {file} 已被复制到 {target_dir}')
