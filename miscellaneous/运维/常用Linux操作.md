---
title: 常用Linux操作
date: 2024-05-05T02:45:54Z
lastmod: 2024-05-05T02:49:58Z
---

# 端口

## 端口占用

```powershell
netstat -aon|findstr "8888"
taskkill /T /F /PID 8888
```

‍
