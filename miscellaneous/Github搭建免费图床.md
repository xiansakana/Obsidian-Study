---
title: Github搭建免费图床
tags:
  - 图床
  - Git
categories: 杂项
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262259266.jpg
abbrlink: 4df281b8
date: 2024-01-26 22:58:42
---

# 创建 Github 新仓库

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262255535.png)

一定要勾选 public，不然别人看不到图，然后建议加一个 README 文件。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256340.png)

看到如下界面就说明图床已经创建好了，接下来就是上传图片了。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256112.png)

# 上传图片

## 下载 PicGo

推荐使用一个开源图床工具  [PicGo](https://molunerfinn.com/PicGo/)  来作为我们的图片上传工具，打开链接的官网后点击免费下载后会跳转到 Github 的界面。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256214.png)

一般前几个是 beta 版本，也就是测试版本，所以我们选择后面的正式版。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256551.png)

在所需下载版本的最后的 assets 中选择对应的系统版本，windows 系统 32 位就选 ia32，64 位就选 x64，或者直接直接选下面那个 setup exe 的，ios 系统选 dmg。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256187.png)

安装之后软件的界面大概是这样。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256532.png)

## 创建 Github token

在 Github 里打开 Settings

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262256820.png)

然后翻到最下面左侧选择 Developer settings

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257339.png)

进入 Developer settings 后选择左边 Personal access tokens 里的的 tokens (classic)，最后点击 Generate new token (classic)。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257207.png)

填写用途，我选择的是永不过期，并勾选 repo，然后点 Generate token 即可

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257800.png)

这个 token 只会显示一次，所以最好把它复制下来存好，方便下次使用，否则下次有需要重新新建。我的话直接在 Github 上新建一个 private 库来存这个 token，这样想用也能随时找到。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257228.png)

## 配置 PicGo

打开 PicGo，选择图床设置中的 GitHub 然后设置如下，其中仓库名是刚刚创建的仓库，分支名一般是 main，Token 就是刚刚生成的那个，最后点击确定。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257405.png)

我一般直接选择 qq 或者 snipaste 截图然后直接剪切板图片快捷上传，或者直接拖动图片上传。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257815.png)

也可以通过快捷键上传，默认为 ctrl + shift +P。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262257869.png)

如果在国内的话 Github 图片访问可能会很慢，所以这时候我们就可以用  [jsDelivr](https://www.jsdelivr.com/")  进行免费加速，而设置的方法也很简单，只需要在我们 PicGo 图床配置中添加如下自定义域名即可

> https://cdn.jsdelivr.net/gh/用户名/仓库名

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262258811.png)
