# -*- coding: utf-8 -*-
# @Time : 2022/6/22 9:15
# @Author : Cao Yuxin
# @File : tool.py

import os
import numpy as np
from PIL import Image
import glob
import cv2 as cv


def img_metting(img_dir, mask_dir, metted_dir):
    if not os.path.exists(metted_dir):
        os.makedirs(metted_dir)

    for file in os.listdir(img_dir):
        pure_img_name = file.split('.')[-2]+'.png'

        if not os.path.exists(os.path.join(mask_dir, pure_img_name)):
            print("no exist" + os.path.join(mask_dir, pure_img_name))
            continue
        print(pure_img_name+" is being met...")
        img = cv.imread(os.path.join(img_dir, file))
        mask = cv.imread(os.path.join(mask_dir, pure_img_name))

        result = cv.bitwise_and(img, mask)          # 必须是相同通道数
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)  # 灰度图
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)  # 4通道

        for i in range(0, result.shape[0]):  # 访问所有行
            for j in range(0, result.shape[1]):  # 访问所有列
                if mask[i][j] < 100:
                    result[i, j, 3] = 0
        cv.imwrite(os.path.join(metted_dir, pure_img_name), result)
        print(file+" is finished.")


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

# 用于修改背景
def overlap(top_path, btm_path, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    img_name = top_path.split('/')[-1]

    top = cv.imread(top_path, cv.IMREAD_UNCHANGED)      # 读取四通道
    btm = cv.imread(btm_path)
    top_shape = top.shape
    print("firstly, btm shape ")
    print(btm.shape)
    # cv.imshow("origin btm", btm)
    btm_shape = (top_shape[1], top_shape[0])
    btm = cv.resize(btm, btm_shape)
    cv.imwrite(os.path.join(save_dir, "btm_resize.png"), btm)
    # cv.imshow("resize", btm)
    # cv.waitKey()
    # cv.destroyAllWindows()
    # btm_shape = btm.shape
    print("top and btm shapes:")
    print(top_shape)
    print(btm.shape)
    for i in range(0, top_shape[0]):  # 访问所有行
        for j in range(0, top_shape[1]):  # 访问所有列
            if (top[i][j][3] == 0):
                top[i][j][:2] = btm[i][j][:2]
                top[i][j][3] = 255

    cv.imwrite(os.path.join(save_dir, img_name), top)


if __name__ == "__main__":
    origin_dir = "test_data/test_images"
    mask_dir = "test_data/u2netp_results"
    save_dir = "test_data/mytest"
    cat_path = r'E:\Code\u2_net\U-2-Net\test_data\mytest/metting/cat.png'

    # img_metting(origin_dir, mask_dir, "test_data/mytest/metting")
    # print("=======metting ok======")
    # watercolor(origin_dir, mask_dir, "test_data/mytest/watercolor")
    # print("=======watercolor ok======")
    # oilpainting(origin_dir, mask_dir, "test_data/mytest/oilpaint")
    # print("=======oilpaint ok======")

    overlap(r"E:\Code\u2_net\U-2-Net\test_data\mytest/metting/cat.png", r"E:\Code\u2_net\U-2-Net\test_data/test_images/alask.png", save_dir)


