## 创建Github仓库

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092235458.png)

然后根据自己需求设置名称，如果想要公开笔记就选public，不想公开就选private。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092237808.png)

## 同步仓库到本地

这里如果熟悉git就用git clone，不熟悉git的话就用[Github Desktop](https://desktop.github.com/)，也就是Github的桌面端。

下载完成后选择clone a repository。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092247855.png)

同步完成后选择刚刚创建的仓库，然后Local Path是我们要clone的地方，随便选个空的文件夹就好，因为后面要把.git目录移动到Obsidian的仓库里面。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092250928.png)

## 合并Obsidian仓库和Git仓库


在clone后的Obsidian-Library的文件夹中可以看到隐藏的.git文件夹，如果看不到可能是因为没有勾选显示隐藏的项目，选择勾选就好。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092256350.png)

然后将.git文件夹移动到Obsidian笔记所在的仓库，使得其和.obsidian文件夹在一起

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092303503.png)

按照我自己的尝试，其实会发现之后装Obsidian Git的插件仍然无法链接到仓库,会显示git is not ready，最后才发现可能是没有安装git的原因，所以还是建议安装一下[git](https://gitforwindows.org/)。

具体的安装过程可以参考这篇文章：[Git 详细安装教程（详解 Git 安装过程的每一个步骤）](https://blog.csdn.net/mukes/article/details/115693833)

## 安装 Obsidian Git 插件进行后续的同步

打开Obsidian[Obsidian Git](https://github.com/denolehov/obsidian-git)



