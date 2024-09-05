# Unblock-Netease-Music

---

title: Unblock Netease Music
tags:

- 网易云音乐
- VPN
  categories: 杂项
  cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262307331.jpg
  abbrlink: a66fbac0
  date: 2024-01-26 23:05:37

---

[参考项目地址](https://github.com/UnblockNeteaseMusic)

# Windows

## 安装依赖

```
npm install @unblockneteasemusic/server
```

## NPX 运行

```
npx -p @unblockneteasemusic/server unblockneteasemusic
```

# IOS

[IOS 食用指南](https://github.com/nondanee/UnblockNeteaseMusic/issues/65)

## 使用证书

安装新的 CA 证书，设备上点击链接应该会自动跳转[https://raw.githubusercontent.com/nondanee/UnblockNeteaseMusic/master/ca.crt](https://raw.githubusercontent.com/nondanee/UnblockNeteaseMusic/master/ca.crt)

在设置 > 通用 > 关于本机 > 证书信任设置，手动信任证书

## 下载 Shadowrocket 并配置 Unblock 代理

- 右上角加号添加节点
- 类型选择 HTTP
- 服务器填写你的服务器公网 [IP](https://ip.cn/)
- 端口填写你启动服务的端口号（默认为 8080）
- 然后底部找到配置 点击本地文件 -> default.conf -> 编辑配置
- 添加三条规则 选项选择你刚刚添加的节点
  - USER-AGENT: NeteaseMusic\*
  - DOMAIN-SUFFIX: 163.com
  - DOMAIN-SUFFIX: 126.net
