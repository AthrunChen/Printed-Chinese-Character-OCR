from keras.utils import np_utils
from PIL import Image
import os, sys
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from array import array
import numpy as np


def encode(path='D:\\datasetplus', class_num=6509, proportion=0, data_num=6509):

    def make_one_hot(data1):
        return (np.arange(class_num) == data1[:, None]).astype(np.integer)
    
    # 现在来构建X_train  与 Y_trian  int list
    data_x = []
    data_y = []
    classes = 0
    # 读取读一个类的内容  每个类的内容对应一个标签
    pathResizedTrainDataBomei = path
    listing1 = os.listdir(pathResizedTrainDataBomei)
    for file in listing1[0:3500]:
        listing2 = os.listdir(pathResizedTrainDataBomei+"\\"+file)
        flag = 0
        for pic in listing2:
            img = Image.open(pathResizedTrainDataBomei +"\\" + file+"\\"+pic)
            x = img.convert('L')  # 转化为灰度图
            x = img_to_array(x)
            data_x.append(x)
            data_y.append(classes)
            flag = flag + 1
            # if flag > 30:
            #     break
        classes = classes + 1
        print("class:"+str(classes)+"completed")

    data_x = np.array(data_x)

    temp = np.array(data_y)
    data_y = make_one_hot(temp)  # one hot encode

    split4test =int( data_num * proportion)
    split4train = data_num - split4test
    index = np.arange(data_num)
    np.random.shuffle(index)
    data_x = data_x[index, :, :, :]
    data_y = data_y[index, :]

    X_train = data_x[0:split4train, :, :, :]
    Y_train = data_y[0:split4train, :]

    X_test = data_x[split4train:data_num-1, :, :, :]
    Y_test = data_y[split4train:data_num-1, :]

    parameter = {'x_train': X_train, 'y_train': Y_train, 'x_test': X_test, 'y_test': Y_test}
    return parameter


if __name__ == "__main__":
    # parameter = encode(path='D:\\datasetplus2', class_num=6509, proportion=0, data_num=65090)
    # np.savez("trainsetv3.npz", parameter['x_train'], parameter['y_train'])
    parameter = np.load("trainsetv3.npz")
    print(parameter["arr_0"].shape)
    print(parameter["arr_1"].shape)


    

