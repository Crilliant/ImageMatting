# -*- coding: utf-8 -*-
# @Time : 2022/6/22 9:15
# @Author : Cao Yuxin
# @File : tool.py

import os
import numpy as np
from PIL import Image
import glob
import cv2 as cv
# 用于风格迁移
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt


def img_metting(img_dir, mask_dir, metted_dir):
    if not os.path.exists(metted_dir):
        os.makedirs(metted_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2]+'.png'
        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue
        img = cv.imread(os.path.join(img_dir, file))
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))

        result = cv.bitwise_and(img, mask)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)  # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)  # 4通道

        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 1
        cv.imwrite(os.path.join(metted_dir, pure_img_name), result)
        print(file+" is finished.")


def test_png(img):
    img = cv.imread(img)
    img = cv.resize(img, (80, 100))
    cv.imshow("small png", img)
    cv.waitKey()
    cv.destroyAllWindows()
    print(img.shape)
    # print(img[0])
    # print(len(img[0]))
    for i in range(30, 40):
        print(img[51][i])

def watercolor(img_dir, mask_dir , save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2]+'.png'
        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue
        img = cv.imread(os.path.join(img_dir, file))
        result = cv.stylization(img, sigma_s=60, sigma_r=0.6)
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))
        result = cv.bitwise_and(result, mask)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)     # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)    # 4通道


        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 1
        cv.imwrite(os.path.join(save_dir, pure_img_name), result)
        print(file+" is finished.")


def oilpainting(img_dir, mask_dir , save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2]+'.png'
        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue

        img = cv.imread(os.path.join(img_dir, file))
        result = cv.xphoto.oilPainting(img, 7, 1)
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))
        result = cv.bitwise_and(result, mask)

        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)     # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)    # 4通道

        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 1
        cv.imwrite(os.path.join(save_dir, pure_img_name), result)
        print(file+" is finished.")

def starrynight(content_image_path, style_image_path, save_dir):
    content_image = plt.imread(content_image_path)
    style_image = plt.imread(style_image_path)
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = tf.image.resize(style_image, (256, 256))

if __name__ == "__main__":
    origin_dir = "test_data/test_images"
    mask_dir = "test_data/u2netp_results"
    save_dir = "test_data/mytest"

    img_metting(origin_dir, mask_dir, "test_data/mytest/metting")
    print("=======metting ok======")
    watercolor(origin_dir, mask_dir, "test_data/mytest/watercolor")
    print("=======watercolor ok======")
    oilpainting(origin_dir, mask_dir, "test_data/mytest/oilpaint")
    print("=======oilpaint ok======")