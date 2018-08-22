import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


def sege_func(filename="IMG_20180424_123611_HHT.jpg", dst_dir=r"D:\build my dl NN test\imagegen", base_dir=r"D:\build my dl NN test\imagedataset", temppicfile=r"D:\build my dl NN test\tempfile"):
    global count
    count = 0
    dst_dir = dst_dir
    base_dir = base_dir
    path_test_image = os.path.join(base_dir+"\\"+filename)

    del_file(temppicfile)

    temppicfile = temppicfile
    image_color = cv2.imread(path_test_image)

    scale = image_color.shape[1]/2500
    new_shape = (int(image_color.shape[1] / scale), int(image_color.shape[0] / scale))
    image_color = cv2.resize(image_color, new_shape)
    image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

    true_width = int(1.4 * image.shape[0])
    width_cut_start = int((image.shape[1]-true_width)/2)
    width_cut_end = int((image.shape[1]+true_width)/2)
    image = image[:, width_cut_start:width_cut_end]

    cv2.threshold(image, 90, 255, 1, image)

    temp1 = int(image.shape[1]/2)
    temp2 = int(image.shape[0]/2)
    image[:, temp1:] = 0

    cv2.imshow('binary image', image)
    cv2.waitKey(0)

    horizontal_sum = np.sum(image, axis=1)

    plt.plot(horizontal_sum, range(horizontal_sum.shape[0]))
    plt.gca().invert_yaxis()
    plt.show()
    del_file(dst_dir + r'\address')

    def extract_peek_ranges_from_array(array_vals, minimun_val=2700, minimun_range=30,endline=500):
        start_i = None
        end_i = None
        peek_ranges = []
        gate1 = int(image.shape[0]*0.15+1)
        gate2 = int(image.shape[0]*0.95+1)
        for i, val in enumerate(array_vals):
            if i < gate1:
                pass
            elif i > gate2:
                pass
            elif val > minimun_val and start_i is None:
                start_i = i-15
            elif val > minimun_val and start_i is not None:
                pass
            elif val < endline and start_i is not None:
                end_i = i+10
                if end_i - start_i > minimun_range:
                    peek_ranges.append((start_i, end_i))
                    start_i = None
                    end_i = None

            elif val < minimun_val and start_i is None:
                pass
            else:
                pass
        return peek_ranges



    def cutImage(img):
        global count
        for i, peek_range in enumerate(peek_ranges):
            y = peek_range[0]
            count += 1
            img1 = img[y:peek_range[1], :]
            cv2.imwrite(temppicfile + "//" + str(count) + ".jpg", img1)


    peek_ranges = extract_peek_ranges_from_array(horizontal_sum)

    cutImage(image_color)          # 行分割


    def extract_peek_ranges_from_array_vertical(array_vals, minimun_val=200, minimun_range=50, gate=3000, bias=0,  upergate=1000, beta = 0.522):
        start_i = None
        end_i = None
        peek_ranges = []
        beta = beta
        gate1 = int(gate)
        val = 100
        upergate1 = upergate
        for i, t in enumerate(array_vals):
            val = beta*t + (1-beta)*val
            if val > minimun_val and start_i is None:
                start_i = i-bias-3
            elif val > minimun_val and start_i is not None:
                pass
            elif val < gate1 and start_i is not None:
                end_i = i+bias-5
                if end_i - start_i > minimun_range:

                    if end_i - start_i > upergate1:

                        peek_ranges.append((start_i, int(start_i+(end_i - start_i) / 2)))
                        peek_ranges.append((int(start_i+(end_i - start_i) / 2), end_i))
                        start_i = None
                        end_i = None
                    else:
                        peek_ranges.append((start_i, end_i))
                        start_i = None
                        end_i = None
            elif val < minimun_val and start_i is None:
                pass
            else:
                pass
        return peek_ranges


    def extract_peek_ranges_from_array_vertical_num(array_vals, minimun_val=200, minimun_range=20, bias=0, gate=3000):
        start_i = None
        end_i = None
        peek_ranges = []
        beta = 0.95
        gate1 = gate
        val = 100
        for i, t in enumerate(array_vals):
            val = beta*t + (1-beta)*val
            if val > minimun_val and start_i is None:
                start_i = i-bias
                if start_i < 0:
                    start_i = None
            elif val > minimun_val and start_i is not None:
                pass
            elif val < gate1 and start_i is not None:
                end_i = i+bias
                if end_i - start_i > minimun_range:
                    peek_ranges.append((start_i, end_i))
                    start_i = None
                    end_i = None
            elif val < minimun_val and start_i is None:
                pass
            else:
                pass
        return peek_ranges


    def cutImage_vertical(img2, z, peek_ranges_ver, dst_dir1=dst_dir):
        for i, peek_range in enumerate(peek_ranges_ver):

            if peek_range[0] < 0:
                pass
            else:
                img3 = img2[:, peek_range[0]:peek_range[1]]
                cv2.imwrite(dst_dir1 + "//" + str(z*10+i) + ".png", img3)


    index = os.listdir(temppicfile)
    for j, file in enumerate(index[:count]):
        image_block = cv2.imread(temppicfile+"\\"+file)

        new_shape = (int(image_block.shape[1] / scale), int(image_block.shape[0] / scale))
        image_block = cv2.resize(image_block, new_shape)
        image2 = cv2.cvtColor(image_block, cv2.COLOR_BGR2GRAY)
        cv2.threshold(image2, 55, 255, 1, image2)

        cv2.imshow('binary image', image2)
        cv2.waitKey()

        vertical_sum = np.sum(image2, axis=0)
        # print("vertical array shape:"+str(vertical_sum.shape))
        plt.plot(vertical_sum, range(vertical_sum.shape[0]))
        plt.gca().invert_yaxis()
        plt.show()

        if j == 0:
            peek_ranges_vertical = extract_peek_ranges_from_array_vertical(vertical_sum, minimun_val=100, minimun_range=35,
                                                                           gate=2, bias=6, upergate=80, beta=0.4)
            del_file(dst_dir + r'\name')
            cutImage_vertical(image_block, j, peek_ranges_vertical, dst_dir1=dst_dir + r'\name')
        elif j == 1:
            peek_ranges_vertical = extract_peek_ranges_from_array_vertical(vertical_sum, minimun_val=100, minimun_range=35,
                                                                           gate=2, bias=5, upergate=80, beta=0.4)
            del_file(dst_dir + r'\sex')
            cutImage_vertical(image_block, j, peek_ranges_vertical, dst_dir1=dst_dir + r'\sex')
        elif j == 2:
            peek_ranges_vertical = extract_peek_ranges_from_array_vertical_num(vertical_sum, minimun_val=200, minimun_range=16, bias=3, gate=20)
            del_file(dst_dir +r'\birth')
            cutImage_vertical(image_block, j, peek_ranges_vertical, dst_dir1=dst_dir+r'\birth')

        elif j == len(index)-1:
            peek_ranges_vertical = extract_peek_ranges_from_array_vertical_num(vertical_sum)
            del_file(dst_dir + r'\id num')
            cutImage_vertical(image_block, j, peek_ranges_vertical,dst_dir1=dst_dir+r'\id num')

        else:
            peek_ranges_vertical = extract_peek_ranges_from_array_vertical(vertical_sum,minimun_val=200, minimun_range=10, gate=2, bias=5, upergate=80)
            cutImage_vertical(image_block, j, peek_ranges_vertical, dst_dir1=dst_dir+r'\address')

    print("segementate completed!")







