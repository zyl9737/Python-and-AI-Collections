import os
import requests
from bs4 import BeautifulSoup

# 导入必要的库
# 定义基础URL
# 使用requests获取网页内容
# 使用BeautifulSoup解析HTML
# 找到所有的img标签
# 对于每个img标签，获取src属性的值
# 将相对路径添加到基础URL，得到完整的图片URL
# 使用requests下载图片
# 将图片保存到指定的文件夹

base_url = "https://vis-www.cs.umass.edu/lfw/"
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
response = requests.get(base_url + "devTrain.html", headers=headers, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

for img in soup.find_all('img'):
    img_url = base_url + img.get('src')
    img_response = requests.get(img_url, verify=False)  # 添加 verify=False
    img_name = img.get('src').split('/')[-1]
    folder_name = img.get('src').split('/')[-2]
    os.makedirs('data/' + folder_name, exist_ok=True)
    with open('data/' + folder_name + '/' + img_name, 'wb') as f:
        f.write(img_response.content)