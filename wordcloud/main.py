from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("KakaoTalk5.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
      if '] [' in line:
        text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('이모티콘\n', '').replace('사진', '').replace('삭제된 메시지입니다', '')



font_path = 'HANSomaB.ttf'

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked2.png")