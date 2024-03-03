---
title: Obsidian同步到Github (Windows)
tags:
  - Obsidian
  - 笔记
  - Git
categories: 杂项
cover: 'https://cdn.cbd.int/xiansakana-blog-img/202401262304183.jpg'
abbrlink: 3c869818
date: 2024-01-26 23:03:09
---

# 创建 Github 新仓库

![](https://cdn.cbd.int/xiansakana-blog-img/202401262255535.png)

然后根据自己需求设置名称，如果想要公开笔记就选 public，不想公开就选 private。

![](https://cdn.cbd.int/xiansakana-blog-img/202401262300632.png)

# 同步仓库到本地

这里如果熟悉 git 就用 git clone，不熟悉 git 的话就用[Github Desktop](https://desktop.github.com/)，也就是 Github 的桌面端。

下载完成后选择 clone a repository。

![](https://cdn.cbd.int/xiansakana-blog-img/202401262301225.png)

同步完成后选择刚刚创建的仓库，然后 Local Path 是我们要 clone 的地方，随便选个空的文件夹就好，因为后面要把.git 目录移动到 Obsidian 的仓库里面。

![](https://cdn.cbd.int/xiansakana-blog-img/202401262301847.png)

# 合并 Obsidian 仓库和 Git 仓库

在 clone 后的 Obsidian-Library 的文件夹中可以看到隐藏的.git 文件夹，如果看不到可能是因为没有勾选显示隐藏的项目，选择勾选就好。

![](https://cdn.cbd.int/xiansakana-blog-img/202401262301476.png)

然后将.git 文件夹移动到 Obsidian 笔记所在的仓库，使得其和.obsidian 文件夹在一起

![](https://cdn.cbd.int/xiansakana-blog-img/202401262301045.png)

按照我自己的尝试，其实会发现之后装 Obsidian Git 的插件仍然无法链接到仓库,会显示 Git is not ready，最后才发现可能是没有安装 git 的原因，所以还是建议安装一下[Git](https://gitforwindows.org/)。

具体的安装过程可以参考这篇文章：[Git 详细安装教程（详解 Git 安装过程的每一个步骤）](https://blog.csdn.net/mukes/article/details/115693833)

# 安装 Obsidian Git 插件进行后续的同步

打开 Obsidian，在的这个准备好的库中，安装一个名为[Obsidian Git](https://github.com/denolehov/obsidian-git)的插件，具体操作如下。

首先在左下角设置中的第三方插件中关闭安全模式

![](https://cdn.cbd.int/xiansakana-blog-img/202401262302769.png)

然后浏览社区插件市场并搜索 Obsidian Git 选择安装

![](https://cdn.cbd.int/xiansakana-blog-img/202401262302861.png)

![](https://cdn.cbd.int/xiansakana-blog-img/202401262302564.png)

注意要打开插件的开关

![](https://cdn.cbd.int/xiansakana-blog-img/202401262302414.png)

然后在左下角插件的配置中可以设置 backup interval（备份时间间隔）

![](https://cdn.cbd.int/xiansakana-blog-img/202401262302323.png)

安装完成后应该会自动出现一个 Git Control View 的侧边栏。如果没有，则按下 Ctrl + P 打开命令面板，搜索  `Obsidian Git: Open Source Control View` ，就可以打开这个面板。

![](https://cdn.cbd.int/xiansakana-blog-img/202401262302152.png)

有了这个插件，以后的同步操作你都可以在 Obsidian 内部进行了。

这个插件顶部的按钮对应了 Git 中最常见的几个操作。如果你对 Git 有一定的了解，应该对这些操作不会陌生。

1. Backup：备份，提交所有的更改，并且执行推送。
2. Commit：确认提交，但不推送。
3. Stage all：存储当前的变更。
4. Unstage all：取消存储变更。
5. Push：推送到远端，可以理解为推送到 Github。
6. Pull：从远端拉取到本地，可以理解为从 Github 拉取最新数据到本地。
7. Change Layout：改变下方文件的排布方式。
8. Refresh：刷新当前的文件变更情况。

如果你不想了解他们具体是干什么的，只想知道怎么做同步，那其实就两个按键有用。

1. Backup，第一个按钮，一次性完成提交并推送到 Github。
2. Pull，第六个按钮，从 Github 同步到本地。

到这一步就完成了所有的配置工作，第一次使用时，点击 Backup 就可以。
