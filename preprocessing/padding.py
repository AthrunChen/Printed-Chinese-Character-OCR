from PIL import Image


def padding_fuc(image):
    imread = image
    print(imread.size)

    bench = max(imread.size[0], imread.size[1])/64
    print(bench)

    imread = imread.resize((int(imread.size[0]/bench), int(imread.size[1]/bench)))
    print(imread.size)
    im_padding = Image.new("RGB", (64, 64), (255, 255, 255))

    region = imread

    offset_x = 0
    offset_y = 0
    offset = int((64-min(imread.size[0], imread.size[1]))/2-1)
    if imread.size[0]<imread.size[1]:
        offset_x = offset
    else:
        offset_y = offset
    im_padding.paste(region, (offset_x, offset_y, imread.size[0]+offset_x, imread.size[1]+offset_y))
    return im_padding
