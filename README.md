# ImageMatting

本仓库为WHU2022年六月第三学期实训项目，图像前景分隔。

<img src="img/sea_cat.png" alt="logo" style="zoom: 13%;" />

---

### 项目成员

[Mloser](https://github.com/Mloser-z), [sykyyds](https://github.com/sykyyds), [Crilliant](https://github.com/Crilliant), [weishikun](https://github.com/weishikun), [Zhi-hi](https://github.com/Zhi-hi), [Zhuxyyy](https://github.com/Zhuxyyy)

---

### 工程结构

```
├─back
├─front
│  ├─public
│  └─src
│      ├─assets
│      ├─components
│      ├─router
│      ├─store
│      └─views
├─img
└─server
    ├─model
    │  └─__pycache__
    ├─saved_models
    │  └─u2netp	：保存的模型参数
    └─test_data	：用于测试的图片数据
        ├─mytest
        │  └─metting
        ├─test_human_images
        ├─test_images
        └─u2netp_results
```





---

### 模型说明

使用U^2^-Net，参考论文[U2-Net: Going Deeper with Nested U-Structure for Salient Object Detection](https://arxiv.org/pdf/2005.09007.pdf)

