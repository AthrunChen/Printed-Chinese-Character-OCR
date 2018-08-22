# -*- coding: utf-8 -*-

import os
import word_script
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from PIL import Image, ImageFilter


class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"

    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds

    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)

def rndColor():
    """
    生成随机颜色
    :return:
    """
    return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))


text = "重邮"
path = r"D:\build my dl NN test\chinese_fonts"
Front = os.listdir(path)
print(Front)
# front = ["DroidSansFallbackFull.ttf", "fangzheng_fangsong.ttf", "fangzheng_heiti.TTF", "fangzheng_jieti.TTF", "fangzheng_shusong.ttf", "mingliu.ttc", "NotoSansHans-Black.otf", "NotoSansHans-Bold.otf", "NotoSansHans-DemiLight.otf", "NotoSansHans-Light.otf", "NotoSansHans-Medium.otf", "NotoSansHans-Regular.otf", "NotoSansHans-Thin-Windows.otf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "huawenxihei.ttf", "fangsong.TTF"]
n = 1
Front = ["huawenxihei.ttf"]
for h in range(30):
    label = 0
    for i in text:

        size = random.randint(0, 20)  # 随机调整大小

        axis_x = random.randint(-10, 10)
        axis_y = random.randint(-5, 1)

        noise = random.randint(0, 50)

        scale1 = random.randint(-30, 30)
        scale2 = random.randint(-10, 10)

        filtersacle = 0.1*random.randint(-5, 0)

        rotate = random.randint(-5, 5)
        im = Image.new("RGB", (64, 64), (255, 255, 255))
        dr = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join("chinese_fonts", "huawenxihei.ttf"), 40+size)
        if size > 0:
            g = size
        else:
            g = 0
        axis_y = axis_y-g
        dr.text((axis_x, axis_y), i, font=font, fill="#000000")


        for i in range(noise):  # 加噪点
            dr.point([random.randint(0, 64), random.randint(0, 64)], fill=rndColor())

        path = "D:\\paper_use\\" + str(label)
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        im = im.rotate(rotate)  # 旋转
        # im = im.filter(MyGaussianBlur(radius=1.3+filtersacle))
        im = im.resize((640-20*scale1, 640+20*scale1))
        im = im.resize((64, 64))

        im.save("D:\\paper_use\\"+str(label)+"\\" + str(n)+".jpg")
        im.close()
        label = label+1
    n = n + 1
    print(str(h)+" completed")


# if __name__ == '__main__':


