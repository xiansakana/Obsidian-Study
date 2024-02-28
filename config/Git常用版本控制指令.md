---
title: Git常用版本控制指令
tags:
  - Git
categories: 杂项
cover: 'https://img.xiansakana.xyz/202402060822719.jpg'
abbrlink: 23e7f25b
date: 2024-02-06 08:20:26
---

## branch

git clone获取指定分支

```bash
git clone -b <分支名> <仓库地址>
```

查看全部分支

```bash
git branch -a
```

将本地分支与远程同名分支相关联

```bash
git push -u origin <本地分支名>
```

创建本地分支

```bash
git checkout -b <本地分支名>
```

拉取指定的某一个分支

```bash
git checkout -b <本地分支名> origin/<远程分支名>
```

> 该命令的作用是：checkout远程仓库origin的分支“dev”，在本地起名为“dev”分支，并切换到本地的“dev”分支。

拉取该分支的最新代码

```bash
git pull origin dev
```





## pull

将远程指定分支拉取到本地指定分支上

```bash
git pull origin <远程分支名>:<本地分支名>
```

将远程指定分支拉取到本地当前分支上

```bash
git pull origin <远程分支名>
```

将与本地当前分支同名的远程分支拉取到本地当前分支上，需先关联远程分支。

```bash
git pull
```

git强制覆盖本地命令

```bash
git fetch --all
git reset --hard origin/master
```



## push

将本地当前分支推送到远程指定分支上

```bash
git push origin <本地分支名>:<远程分支名>
```

将本地当前分支推送到与本地当前分支同名的远程分支上

```bash
git push origin <本地分支名>
```

将本地当前分支推送到与本地当前分支同名的远程分支上，需先关联远程分支

```bash
git push
```

