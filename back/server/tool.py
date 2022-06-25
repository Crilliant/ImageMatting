# -*- coding: utf-8 -*-
# @Time : 2022/6/22 9:15
# @Author : Cao Yuxin
# @File : tool.py

import os
import numpy as np
from PIL import Image
import glob
import cv2 as cv
import back.server.u2net_test as u2net


# 识别单张图片（路径imp_path）显著物体，并保存到meetter_dir
# mask_dir为黑白掩码保存的目录
def img_matting(img_path, mask_dir, metted_dir):
    u2net.inference_img(img_path, mask_dir)
    print("finish the inference")
    if not os.path.exists(metted_dir):
        os.makedirs(metted_dir)

    pure_img_name = os.path.basename(img_path)
    pure_img_name = pure_img_name.split('.')[-2] + ".png"

    if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
        print("no exist" + os.path.join(mask_dir, pure_img_name))

    print(pure_img_name + " is being met...")
    img = cv.imread(os.path.join(img_path))
    mask = cv.imread(os.path.join(mask_dir, pure_img_name))
    print(img.shape)
    print(mask.shape)

    result = cv.bitwise_and(img, mask)  # 必须是相同通道数
    mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)  # 灰度图
    result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)  # 4通道

    for i in range(0, result.shape[0]):  # 访问所有行
        for j in range(0, result.shape[1]):  # 访问所有列
            if mask[i][j] < 100:
                result[i, j, 3] = 0
    cv.imwrite(os.path.join(metted_dir, pure_img_name), result)
    print(pure_img_name + " is finished.")


# met一个文件夹的图片
def img_metting_dir(img_dir, mask_dir, metted_dir):
    if not os.path.exists(metted_dir):
        os.makedirs(metted_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2] + '.png'

        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue
        print(pure_img_name + " is being met...")
        img = cv.imread(os.path.join(img_dir, file))
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))

        result = cv.bitwise_and(img, mask)  # 必须是相同通道数
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)  # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)  # 4通道

        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 0
        cv.imwrite(os.path.join(metted_dir, pure_img_name), result)
        print(file + " is finished.")


# 水彩
def watercolor(img_dir, mask_dir, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2] + '.png'
        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue
        img = cv.imread(os.path.join(img_dir, file))
        result = cv.stylization(img, sigma_s=60, sigma_r=0.6)
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))
        result = cv.bitwise_and(result, mask)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)  # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)  # 4通道

        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 1
        cv.imwrite(os.path.join(save_dir, pure_img_name), result)
        print(file + " is finished.")


# 油画，弃用
def oilpainting(img_dir, mask_dir, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2] + '.png'
        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue

        img = cv.imread(os.path.join(img_dir, file))
        result = cv.xphoto.oilPainting(img, 7, 1)
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))
        result = cv.bitwise_and(result, mask)

        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)  # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)  # 4通道

        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 1
        cv.imwrite(os.path.join(save_dir, pure_img_name), result)
        print(file + " is finished.")


def overlap(top_path, btm_path, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    img_name = top_path.split('/')[-1]

    top = cv.imread(top_path, cv.IMREAD_UNCHANGED)  # 读取四通道
    btm = cv.imread(btm_path)

    btm = cv.resize(btm, (top.shape[1], top.shape[0]))
    print("top and btm shapes:")
    print(top.shape)
    print(btm.shape)
    for i in range(0, top.shape[0]):  # 访问所有行
        for j in range(0, top.shape[1]):  # 访问所有列
            if (top[i][j][3] == 0):
                top[i][j][:3] = btm[i][j][:3]
                top[i][j][3] = 255

    cv.imwrite(os.path.join(save_dir, img_name), top)


if __name__ == "__main__":
    filename_test = '0.jpg'
    '/home/mloser/Program/Python/ImageMatting/back/static/'
    file_path = os.path.join('/home/mloser/Program/Python/ImageMatting/back/static/Upload', filename_test)
    mask_path = os.path.join('/home/mloser/Program/Python/ImageMatting/back/static/Mask')
    save_path = os.path.join('/home/mloser/Program/Python/ImageMatting/back/static/Download')
    # executor.submit(img_metting, file_path, mask_path, save_path)
    img_matting(file_path, mask_path, save_path)
