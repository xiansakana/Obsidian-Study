---
title: Git常用版本控制指令
tags:
  - Git
categories: 杂项
cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202402060822719.jpg'
abbrlink: 23e7f25b
date: 2024-02-06 08:20:26
---

# branch

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

# pull

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


# push

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


# 删除远端commit

先删除本地的几次提交，"HEAD~1"里面的1代表撤回几次提交

```bash
git reset --soft HEAD~1
```

然后强制性将本地覆盖性的提交到远端，达到删除的目的，"branchname"是你的分支名称

```bash
git push origin branchname --force
```


# merge

**切换到`main`分支**：首先确保你当前在`main`分支上。

```bash
git checkout main
```

**拉取最新的`main`分支代码**：确保你的`main`分支是最新的。

```bash
git pull origin main
```

**合并`dev`分支**：将`dev`分支合并到`main`分支上。

```bash
git merge dev
```

如果有冲突发生，在合并过程中Git会提示你进行解决。你需要手动解决冲突，并提交合并后的结果。

**推送到远程仓库**：合并完成后，将更新的`main`分支推送到远程仓库。

```bash
git push origin main
```