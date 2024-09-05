---
title: Git-bash配置多个Github用户
date: 2024-04-25T19:26:51Z
lastmod: 2024-05-17T00:37:22Z
---

其实有两种方法，第一种比较简单粗暴但是有效，第二种需要配置各种比较麻烦，但是一劳永逸。

# 方案一

对于 windows 系统， 选择控制面板 =》 用户账户 =》凭据管理器 =》windows 凭据，删除里面类似 git 相关的的用户信息（以 git 打头的相关数据）。 这样你在敲 git push 就会弹出对话框让你重新输入用户名和密码。 输入你要更改的用户名和密码就可以了。

# 方案二

## 注册 Github 账号

首先肯定得需要多个 Github 账号，这里用两个作为示范

## 生成新 ssh key

打开 git bash，输入`~/.ssh`进入到.ssh 文件夹

```bash
~/.ssh
```

在.ssh 目录下，可以将原有的 id_rsa 和 id_rsa.pub 删掉，然后输入`ssh-keygen -t rsa -C "你的第一个github邮箱地址"`

```bash
ssh-keygen -t rsa -C 2461298052@qq.com
```

然后输入并回车(这个是私钥的名称，可以随意取)，这里我就用 github 的用户名：id_rsa_xiansakana

```bash
id_rsa_xiansakana
```

之后输入密码和再一次确认密码可以为空，回车。

然后在.ssh 目录下会出现私钥 id_rsd_xiansakana 和公钥 id_rsa_xiansakana.pub。

打开公钥 id_rsa_xiansakana.pub，将内容 copy 到第一个 github 的 SSH keys 中。

同理，配置第二个 github 邮箱地址，并将公钥 id_rsa_saltedfishcj.pub 的内容 copy 到第二个 github 的 SSH keys 中

```bash
ssh-keygen -t rsa -C saltedfishcj@gmail.com
id_rsa_saltedfishcj
```

## 添加 ssh key

默认 SSH 只会读取`id_rsa`，所以为了让 SSH 识别新的私钥，需要将其添加到`SSH agent`。

如果报错：`Could not open a connection to your authentication agent.`无法连接到 ssh agent，可执行`ssh-agent`命令后再执行`ssh-add ~/.ssh/id_rsa_xiansakana`命令。

```bash
ssh-agent bash
ssh-add ~/.ssh/id_rsa_xiansakana
ssh-add ~/.ssh/id_rsa_saltedfishcj
```

## 配置 config 文件

然后在.ssh 目录下，新建一个 config 文件（如果无），命令：`touch config`，再对 config 文件进行编辑

```bash
touch config
```

```
#Default 第一个账号(2461298052@qq.com)
Host xiansakana
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_xiansakana

#second 第二个账号（saltedfishcj@gmail.com）
Host saltedfishcj
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_saltedfishcj
```

> 其中 Host 后的名字可以随意方便自己记忆，但 HostName 必须为 github.com(或者其它 git 地址)。

## 测试配置

使用命令：`ssh -T git@xiansakana`，

```bash
ssh -T git@xiansakana
```

如果看到下面的命令表示配置成功了。

```bash
Hi xiansakana! You've successfully authenticated, but GitHub does not provide shell access.
```

同理

```bash
ssh -T git@saltedfishcj
```

查看当前用户

```bash
ssh -T git@github.com
```

查看当前密钥

```bash
ssh-add -l
```

切换账号

```bash
git config --global user.name "name"
git config --global user.email "email"
```

不过通常应该是可以用上面添加 ssh key 的方法来切换

```bash
ssh-agent bash
ssh-add ~/.ssh/id_rsa_xiansakana
ssh-add ~/.ssh/id_rsa_saltedfishcj
```

查看配置

```bash
git config --global --list
```

‍
