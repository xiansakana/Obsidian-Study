# tools

# Markdown

## copy一个文件夹里的所有markdown文件

```python
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
```

## 替换markdown文件中的链接

```python
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
directory_path = 'd:/notes/study/'
old_link_prefix = 'cdn.jsdelivr.net/npm/xiansakana-blog-img'
# old_link_prefix = 'cdn.cbd.int/xiansakana-blog-img'
# old_link_prefix = 'cdn.jsdelivr.net/npm/xiansakana-blog-img'
# new_link_prefix = 'cdn.cbd.int/xiansakana-blog-img'
new_link_prefix = 'cdn.jsdelivr.net/npm/xiansakana-blog-img'
# 执行替换操作
replace_image_links_in_directory(directory_path, old_link_prefix, new_link_prefix)
```

# Image

## 检测相同图片

```python
import os
import warnings
from PIL import Image
import imagehash
from concurrent.futures import ThreadPoolExecutor

# 忽略特定类型的警告
warnings.filterwarnings("ignore", category=UserWarning, module='PIL.TiffImagePlugin')

def process_image(file_path):
    """处理单个图片文件，返回其哈希值和文件路径"""
    try:
        with Image.open(file_path) as img:
            img = img.convert('RGB')  # 确保图片格式统一
            hash = str(imagehash.average_hash(img))
        return hash, file_path
    except Exception as e:
        print(f"无法处理图片 {file_path}: {e}")
        return None

def find_duplicates(folder_path):
    hashes = {}
    duplicates = {}
    files_to_process = []

    # 递归遍历文件夹及所有子文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'webp')):
                file_path = os.path.join(root, filename)
                files_to_process.append(file_path)

    # 使用线程池来处理所有图片
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_image, files_to_process)

    # 收集结果并组织哈希
    for result in results:
        if result:
            hash, file_path = result
            if hash in hashes:
                hashes[hash].append(file_path)
            else:
                hashes[hash] = [file_path]

    # 筛选出含有多于一个元素的列表，即重复的图片
    for hash, files in hashes.items():
        if len(files) > 1:
            duplicates[hash] = files
  
    return duplicates

# 替换为你的图片文件夹路径
folder_path = 'cover'
duplicates = find_duplicates(folder_path)

if duplicates:
    print("找到重复的图片:")
    for hash, files in duplicates.items():
        print(f"哈希值 {hash} 对应的重复图片: {', '.join(files)}")
else:
    print("没有找到重复的图片")
```

# Torncity

## Tornstats 无权限spy导出

**crawl.py**

```python
from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = 'D:\\chromedriver.exe'
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.tornstats.com/login')
driver.find_element(By.ID, 'email').send_keys('saltedfishcj@gmail.com')
driver.find_element(By.ID, 'password').send_keys('kimiga1bansuki')
# Correct way to find an element with multiple classes
button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
button.click()


# Folder to save HTML files
folder_path = 'spies'
os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

# Base URL without the page number
base_url = 'https://www.tornstats.com/spies/faction?page='

# Loop through the desired range of pages
for page_number in range(1, 101):  # Adjust the range as needed
    # Generate the full URL for each page
    url = base_url + str(page_number)
  
    # Navigate to the URL
    driver.get(url)
  
    # Optional: wait for dynamic content to load if necessary
    time.sleep(2)  # Adjust timing as necessary for page load or AJAX content to complete

    # Get the page source
    page_source = driver.page_source
  
    # Define the file path
    file_path = os.path.join(folder_path, f'page_source_{page_number}.html')
  
    # Save the source to a file, naming it according to the page number
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(page_source)
  
    # Print progress
    print(f"Saved source of page {page_number} to {file_path}")

# Close the browser after the loop completes
driver.quit()


```

**converter.py**

```python
import os
import pandas as pd
from bs4 import BeautifulSoup

# 设置文件夹路径
folder_path = 'spies'  # 这里替换为您的文件夹路径

# 创建一个Excel写入器
writer = pd.ExcelWriter('all_spies.xlsx', engine='xlsxwriter')

startrow = 0  # 初始化开始行为0

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
      
        # 读取HTML文件
        with open(file_path, 'r', encoding='utf-8') as file:  # 加入encoding确保中文正确读取
            content = file.read()
      
        # 解析HTML
        soup = BeautifulSoup(content, 'html.parser')
      
        # 提取所有表格
        tables = soup.find_all('table')
      
        # 保存每个表格到Excel的同一个工作表中，表格间不留空
        for table in tables:
            data = pd.read_html(str(table))[0]
            data.to_excel(writer, sheet_name='Combined Data', startrow=startrow, index=False, header=False if startrow != 0 else True)
            startrow += data.shape[0]  # 更新开始行为下一个表格的开始

# 关闭并保存Excel文件
writer.close()
print("所有表格已成功提取并保存到一个Excel工作表中。")

```

# 其他

## 映射文件夹

将study文件夹映射到test文件夹中

```bash
mklink /d /j D:\Hexo\source\_posts\test D:\notes\study
```

## 将vscode添加到右键菜单

1. 新建`vscode.reg`​文件，并写入以下内容

```bash
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\VSCode]
@="Open with Code"
"Icon"="D:\\Program Files\\Microsoft VS Code\\Code.exe"

[HKEY_CLASSES_ROOT\*\shell\VSCode\command]
@="\"D:\\Program Files\\Microsoft VS Code\\Code.exe\" \"%1\""

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\shell\VSCode]
@="Open with Code"
"Icon"="D:\\Program Files\\Microsoft VS Code\\Code.exe"

[HKEY_CLASSES_ROOT\Directory\shell\VSCode\command]
@="\"D:\\Program Files\\Microsoft VS Code\\Code.exe\" \"%V\""

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\VSCode]
@="Open with Code"
"Icon"="D:\\Program Files\\Microsoft VS Code\\Code.exe"

[HKEY_CLASSES_ROOT\Directory\Background\shell\VSCode\command]
@="\"D:\\Program Files\\Microsoft VS Code\\Code.exe\" \"%V\""
```

2. 将`D:\\Program Files\\Microsoft VS Code\\Code.exe`​替换你电脑上**VSCode**的安装路径

3. 双击运行并选择**是**

## 开源协议比较

​![image](assets/image-20240517000412-dlawlod.png)​
