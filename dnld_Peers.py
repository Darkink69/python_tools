import requests
from fake_useragent import UserAgent
import time
import os
import subprocess

ua = UserAgent()
directory = "video"

# https://peers.tv/ajax/program/10338261/2024-10-16/?tz=25200&t=126

link = f"https://peers.tv/ajax/program/10338261/2024-10-16/?tz=25200&t=126"  # Сделать дату и канал
print(link)
headers = {"User-Agent": ua.random}
r = requests.get(link, headers=headers)
m3u8 = r.json()["telecasts"][0]["files"][0]["movie"]
print(m3u8)

r = requests.get(m3u8, headers=headers)

with open(f'1.m3u8', 'wb') as file:
    file.write(r.content)

data = open('1.m3u8')
for line in data:
    if ".ts" in line:
        ts = line.split("/")[-1].rstrip()

        link = f"https://nsk26.peers.tv/hls/49kanal/16/g2500/20241015/{ts}"  # Сделать дату
        print(link)
        headers = {"User-Agent": ua.random}
        r = requests.get(link, headers=headers)
        # time.sleep(15)

        with open(f'{directory}/{ts}', 'wb') as file:
            file.write(r.content)


files = os.listdir(directory)

text_file = open("out.txt", "w")
for file in files:
    path = f"file '{directory}/{file}'\n"
    text_file.write(str(path))
text_file.close()

subprocess.run('ffmpeg -f concat -i out.txt -c copy output.mp4', shell=True, stdin=None, stderr=subprocess.PIPE)

# https://nsk26.peers.tv/hls/49kanal/16/g2500/20241015/segment-1728949175-15883096.ts
# https://nsk26.peers.tv/hls/49kanal/16/g2500/20241013/segment-1728949175-15883268.ts
