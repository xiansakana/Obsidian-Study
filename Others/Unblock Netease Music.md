[参考项目地址](https://github.com/UnblockNeteaseMusic)
# Windows

## 安装依赖
```
npm install @unblockneteasemusic/server
```
## NPX运行
```
npx -p @unblockneteasemusic/server unblockneteasemusic
```

# IOS

[IOS 食用指南](https://github.com/nondanee/UnblockNeteaseMusic/issues/65)

## 下载 Shadowrocket 并配置 Unblock 代理

- 右上角加号添加节点
- 类型选择 HTTP
- 服务器填写你的服务器公网 [IP](https://ip.cn/)
- 端口填写你启动服务的端口号（默认为 8080）
- 然后底部找到配置 点击本地文件 -> default.conf -> 编辑配置
- 添加三条规则 选项选择你刚刚添加的节点 
    - USER-AGENT: NeteaseMusic*
    - DOMAIN-SUFFIX: 163.com
    - DOMAIN-SUFFIX: 126.net
