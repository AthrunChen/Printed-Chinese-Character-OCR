import word_script
import word_script
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
from PIL import Image , ImageOps
from keras.models import load_model
import segementation_plus3
import os
import cv2
import decode_script
import padding


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

# 完成主体逻辑之后需要完成的工作：1、整合tempfile文件夹，用文件夹的形式隔离开2、编写删除tempfile文件夹内容的函数3、减少对绝对地址的依赖
basedir=r"D:\build my dl NN test\imagedataset"
dstdir=r"D:\build my dl NN test\imagegen"
model_path_chinese = r'D:\build my dl NN test\test\MK11.h5'
filename = "0.jpg"
model_path_num = r'D:\build my dl NN test\test\alphav10.h5'
tempfile2_pil2cv = r'D:\build my dl NN test\tempfile2'
segementation_plus3.sege_func(base_dir=basedir, dst_dir=dstdir, filename=filename)           # 预切割图像  并按身份证相关顺序保存在不同文件夹
a = decode_script.decode_fuc()
b = decode_script.decode_num()
model = load_model(model_path_chinese)
model_num = load_model(model_path_num)
t = '.png'


def predict_func(path=dstdir, method="chinese"):
    listing1 = os.listdir(path)

    for z, i in enumerate(listing1):
        result = t in i
        if result:
            pass
        else:
            del listing1[z]
    listing1.sort(key=lambda x:int(x[:-4]))

    # listing1 = os.listdir(imgpath)

    output1 = []
    output2 = []
    print(listing1)
    for j, i in enumerate(listing1):
        imgpath = path +"\\"+i

        x = Image.open(imgpath)
        image_color = padding.padding_fuc(x)
        image_color.save(imgpath)

        char = word_script.func1()
        char_num = word_script.func_num()

        image_color = cv2.imread(imgpath)
        new_shape = (image_color.shape[1] * 2, image_color.shape[0] * 2)
        image_color = cv2.resize(image_color, new_shape)
        image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

        cv2.threshold(image, 90, 255, 1, image)

        x = cv2.blur(image, (4, 4))

        x = cv2.resize(x, (64, 64))
        cv2.imwrite(tempfile2_pil2cv + "\\" + str(j)+".jpg", x)

        x = Image.open(tempfile2_pil2cv + "\\"+str(j)+".jpg")
        x = ImageOps.invert(x)
        x.save(tempfile2_pil2cv + "\\" + str(j)+".jpg")

        x = img_to_array(x)
        print(x.shape)
        x = np.array(x)
        data_x = np.expand_dims(x, axis=0)

        data_x = data_x.astype('float32')
        data_x = (data_x - 127) / 127
        if method =="chinese":
            pos = model.predict(data_x, batch_size=1, verbose=1)
            if np.max(pos) < 0.2:
                pass
            else:
                preds = model.predict_classes(data_x, batch_size=1, verbose=1)
                # print("class:" + str(preds))
                num = a[int(preds)]
                # print("output: "+str(char[int(num)]))
                output2.append((str(char[int(num)])))
                output1.append((str(char[int(num)]), np.max(pos)))


        elif method == "num":
            pos = model_num.predict(data_x, batch_size=1, verbose=1)
            if np.max(pos) < 0.45:
                pass
            else:
                print("asdfadfasdfasdf")
                preds = model_num.predict_classes(data_x, batch_size=1, verbose=1)
                # print("class:" + str(preds))
                num = b[int(preds)]
                # print("output: "+str(char[int(num)]))
                output2.append((str(char_num[int(num)])))
                output1.append((str(char_num[int(num)]), np.max(pos)))
        elif method =="mix":
            pos = model.predict(data_x, batch_size=1, verbose=1)
            pos_num = model_num.predict(data_x, batch_size=1, verbose=1)
            if np.max(pos) < 0.3 and np.max(pos_num)<0.65:
                pass
            else:
                pred_1 = model.predict_classes(data_x, batch_size=1, verbose=1)
                pred_2 = model_num.predict_classes(data_x, batch_size=1, verbose=1)

                if np.max(pos)*2 > np.max(pos_num):

                    num = a[int(pred_1)]
                    output2.append((str(char[int(num)])))
                    output1.append((str(char[int(num)]), np.max(pos)))
                else:

                    num = b[int(pred_2)]
                    output2.append((str(char_num[int(num)])))
                    output1.append((str(char_num[int(num)]), np.max(pos)))
    output2 = ''.join(output2)
    return output2


# path = dstdir + "\\" + "name"
# output1 = predict_func(path, method="chinese")
# # del_file(path)
#
# path = dstdir + "\\" + "sex"
# output2 = predict_func(path, method="chinese")
# # del_file(path)

path =r"D:\build my dl NN test\paper_use"
output3 = predict_func(path, method="mix")
# del_file(path)

# path = dstdir + "\\" + "id num"
# output4 = predict_func(path, method="num")
# # del_file(path)

# year = output4[6:10]
# month = output4[10:12]
# day = output4[12:14]
#


# print("姓名：" + output1)
# print("性别：" + output2[0]+"     "+"民族："+output2[1:])
# print("出生：" + year + " 年 " + month + " 月 " + day + " 日 ")
# print("住址：" + output3)
# print("公民身份证号：" + output4[:14])

