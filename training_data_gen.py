# -*- coding: utf-8 -*-

import os
import word_script
from PIL import Image, ImageFont, ImageDraw

text = word_script.func1()
path = r"D:\build my dl NN test\chinese_fonts"
Front = os.listdir(path)
print(Front)
# front = ["DroidSansFallbackFull.ttf", "fangzheng_fangsong.ttf", "fangzheng_heiti.TTF", "fangzheng_jieti.TTF", "fangzheng_shusong.ttf", "mingliu.ttc", "NotoSansHans-Black.otf", "NotoSansHans-Bold.otf", "NotoSansHans-DemiLight.otf", "NotoSansHans-Light.otf", "NotoSansHans-Medium.otf", "NotoSansHans-Regular.otf", "NotoSansHans-Thin-Windows.otf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "fangsong.TTF"]
n = 1
Front = ["huawenxihei.ttf"]
for h in Front:
    label = 0
    for i in text:
        im = Image.new("RGB", (64, 64), (255, 255, 255))
        dr = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join("chinese_fonts", h), 45)
        dr.text((5, 0), i, font=font, fill="#000000")

        path = "D:\\huawenxihei2\\" + str(label)
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        im.save("D:\\huawenxihei2\\"+str(label)+"\\" + str(n)+".jpg")
        im.close()
        label = label+1
    print(h+"completed")
    n = n + 1


# if __name__ == '__main__':


