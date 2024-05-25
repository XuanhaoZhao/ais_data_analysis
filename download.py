import os
import requests
from bs4 import BeautifulSoup

# 设置下载文件夹路径
download_folder_base = '/Users/myfile/Desktop/ais_code/raw_data'
if not os.path.exists(download_folder_base):
    os.makedirs(download_folder_base)

# 年份范围
start_year = 2019
end_year = 2023

# 基础URL
base_url = 'https://coast.noaa.gov/htdata/CMSP/AISDataHandler/{}/index.html'

# 遍历每一年
for year in range(start_year, end_year + 1):
    # 构建每一年index.html的URL
    year_url = base_url.format(year)
    # 发送HTTP请求
    response = requests.get(year_url)
    response.raise_for_status()  # 确保请求成功

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有的ZIP文件链接
    zip_files = soup.find_all('a', href=True, text=lambda t: t and '.zip' in t)

    # 为每一年创建单独的文件夹
    year_folder = os.path.join(download_folder_base, f'AIS_{year}')
    if not os.path.exists(year_folder):
        os.makedirs(year_folder)

    # 下载文件
    for file_tag in zip_files:
        file_name = file_tag['href']
        if file_name.endswith('.zip'):
            file_url = year_url + file_name
            local_file_path = os.path.join(year_folder, file_name)

            # 发送下载请求
            with requests.get(file_url, stream=True) as r:
                r.raise_for_status()
                with open(local_file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"Downloaded {file_name} for {year}")

print("All files downloaded successfully.")
