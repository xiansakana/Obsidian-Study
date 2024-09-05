---
title: Version Control
date: 2024-04-25T19:26:20Z
lastmod: 2024-09-05T13:05:14Z
---

# 版本控制

软件工程师常利用版本控制来跟踪、维护原始码、文件以及设定档等的改动。有时候，一个程式同时存有两个以上的版本有其必要性，例如：发布版本中程式错误已经被修正，但没有加入新功能；而开发版本则有新的功能正在开发、也有新的错误待解决，于是便需要同时维护两个不同的版本。

此外，为了找出只存在于某一特定版本中的程式错误、或找出程式错误出现的版本，开发人员也必须通过比对不同版本的原始码以找出问题的位置。

# Kernel and Shell

整个电脑可以由使用者、Shell、Kernel、硬件相互协助运作的：

- 硬件(Hardware)：整个系统的实体工作者，没有电力系统的话，CPU、SSD 等就无法工作了。
- 核心(kernel)：是内部的核心，听完 Shell 的翻译，再指示硬体要进行的工作。
- Shell：是外部的表壳，接收使用者的讯息，再翻译给 Kernel 请他处理。
- 使用者：将需求或想做的事发出指令给 Shell。

一般来说， Shell 是指作业系统中提供存取核心(Kernel)所提供之服务的程式。 Shell 基本上有两类：

- CLI (Command-Line Interface)
- GUI (Graphical User Interface)

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311072308618.png)

通常认为，CLI 没有图形使用者介面（GUI）那么方便使用者操作。因为，命令列介面的软体通常需要使用者记忆操作的命令，但是，由于其本身的特点，命令列介面要较图形使用者介面节约电脑系统的资源。在熟记命令的前提下，使用命令列介面往往要较使用图形使用者介面的操作速度要快。所以，在现在的图形使用者介面的作业系统中，通常都保留著可选的命令列介面。

Windows 系统中， Command-Line Prompt (cmd.exe)是个 CLI 程式。在 macOS 中，terminal 提供了一个命令行界面 (CLI) 来控制基于 UNIX 作业系统的基础。

# Command Prompt 常用指令

|CMD Command|Description|
| :------------------------| :-----------------------------|
|cd|Change directory|
|mkdir|Make a new directory|
|type nul > "filename.txt"|制作一个新的 filename.txt 文件|
|cls|clear screen|
|dir|list directory content|
|Ctrl + C|强制终止任何正在执行的指令|

# Unix 作业系统

UNIX 作业系统，是一个强大的多使用者、多工作业系统，支援多种处理器架构，源自 AT&T 公司于 1970 年代在贝尔实验室研究中心开发。由于 macOS 是基于 Unix 的作业系统，所以在 Unix 系统上的指令，在 macOS 的 terminal 都可以直接使用。

Unix 作业系统中，常用的指令有：

|Unix Command|Description|
| :-----------| :---------------------------------------------------------------------------|
|cd|Change directory|
|ls|List files or directories in a directory|
|pwd|Stands for "present working directory"|
|mkdir|Make directory|
|touch|Create, change and modify timestamps of a file|
|rm|Remove file|
|rmdir|Remove an empty directory|
|rm -rf|rf stands for remove forcefully; can be used to remove a non-empty directory|

# Git and Git Bash

Git 是一个免费和开源的 version control system (版本控制系统)，旨在以速度和效率处理从小型到大型项目的所有内容。

Git 的核心是一组 command line utility programs，旨在 Unix 风格的命令环境中执行。 Linux 和 macOS 等现代作业系统都包含内建的 Unix 指令。 这就代表， macOS 系统只需要下载 Git 到电脑后，就可以完全使用 Git 来做版本控制了。

Microsoft Windows 若要使用 Unix 指令以及 Git 指令，需要先下载 Git Bash。(Bash 是 Linux 和 macOS 上流行的默认 shell。 )

Git Bash 是一个适用于 Microsoft Windows 环境的应用程序。在 Git bash 内部，我们可以使用 Unix 指令(因为这是一个 bash)，也可以使用 Git 指令，因为 Git bash 自动包含了 Git 指令。

# Git and GitHub

Git 本身是个在个人电脑上可以帮助开发者做版本控制的软体。GitHub 是个网路平台，为使用 Git 的软体开发和版本控制提供託管服务。Git 与 GitHub 协作的流程如下：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311072355701.png)

名词认识：

- Work Directory – 工作的资料夹。内部包含所有 project 的档案。
- Staging Area – 一个 commit 前的缓衝区域。任何我们想要 commit 的档案都可以放入 staging area。
- Local Repository – 指的是本机电脑上包含.git 隐藏文件夹的 Work Directory。git 资料夹在 git init 被执行时，会自动被创建到 work directory 内部。.git 资料夹内部的文件包含与 commit、remote repository address 等相关的所有信息。它还包含一个存储 commit 历史记录的日志。 此日志可以帮助我们回朔到以前版本的 code。
- Remote Repository – 将程式码储存在 GitHub 等程式码托管服务平台上。

工作流程：

1. 在 work directory 用 git init 来开始追踪程式码版本。
2. 在电脑上的 work directory 撰写程式码。
3. Commit 是 Git project 时间线上的里程碑。每个 commit 都被视为是 project 的一个小版本。
4. git add 的功能是将程式码放到 staging area 上面。使用 git add 可以将即将被 commit 的文件让 git 做追踪。
5. 执行 git commit –m 把 staging area 上的文件做 commit。这些 code 的更动会被记录到 Local Repository(.git 资料夹)内。
6. 用 git push 将 local repository 的所有内容都放到远端伺服器(GitHub)。

Git 对 Local Repository 的档案有 4 种主要状态：

1. untracked: 档案是全新的，Git 对此一无所知。 如果我们用 git add <file>，档案将变成：
2. staged: 现在 Git 知道档案(tracked)，但也将档案作为下一个 commit 的一部分。如果我们做 git commit，档案会变成：
3. unchanged: 档案自上次 commit 以来未更改。 如果我们修改档案，档案就变成：
4. unstaged: modified，但还不是下一次 commit 的一部分。 我们可以使用 git add 再次让他变成 staged 状态。

|Git Command|Description|
| -------------------------------------| ---------------------------------------------------------------------------------------------------------------------------------------------|
|git init|Initialize an empty git repository|
|git config --list|Display all configuration settings|
|git --version|Display the current version of Git|
|git config -global user.name "name"|Set username|
|git config -global user.email "email"|Set email address|
|git status|Display the state of the working directory and staging area|
|git add *filename*|Add files to staging area|
|git commit -m "commit message"|Commit all files on staging area|
|git rm --cashed *filename*|Remove files from staging area|
|git log|Review and read commit history|
|git branch *branchName*|Create a new branch from current commit|
|git checkout *branchName*|Switch to another branch|
|git merge *branchName*|Take the independent lines of development created by git branch and integrate them into a single branch|
|git remove add *origin* *gitSSH*|Connect to a remote repository in gitSSh and name the connection *origin*|
|git push -u origin master|Push the commits in the local branch named master to the remote named origin; -u stands for upstream, 通常第一次 push 时，会被要求登入 GitHub|
|git push|Once we set the -u flag, we can use "git push" command|
|git clone *gitSSH*|Get a working copy of the remote repository|
|git pull *gitSSH*|Update that local copy with new commits from the remote repository|
|git remote set-url origin *gitSSH*|Set the remote connection named origin to a new remote repository|
|git remote remove origin|Remove a connection called origin|
