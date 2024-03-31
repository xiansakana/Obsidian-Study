---
title: Node.js
tags:
  - Node.js
  - NPM
  - 后端
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311120957148.png
categories: 后端
abbrlink: 747d7228
date: 2023-11-12 09:56:07
---

# 静态与动态网页

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080137624.png)

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080137252.png)

静态网站(static websites)由使用 HTML、CSS 和 JavaScript 创建的网页组成。静态网站上的每个页面都存储为单个 HTML 文件，该文件完全按原样从服务器直接传送到用户端。

静态网页的优点在于：

1. 更快的页面加载速度。由于网页都以预先制作完成，服务器的工作只是传送文件， 无需从数据库找资料或在 server side script 做验证等工作，所以加载速度会比动态网页快速。由于页面加载速度是谷歌评估网站性能的关键部分(对 SEO 和排名性能有影响)，这个优点不应被低估。
2. 创建与部署快速。静态网站的创建和发布速度更快，因为它们复杂度较低，并且不需要有组织的连接到数据库。网页制作完成后，静态网页的部署较简单，因为只需要将文件放置到服务器上即可。相对的，动态网页需要避免数据库被黑客入侵、攻击，设定服务器端脚本与数据库都需要额外工作。
3. 安全性较高。 静态网页不与数据库连接，也不使用外部套件。数据库与外部套件都可以成为攻击的常见入口点。

静态网页的缺点在于：

1. 有限的可扩展性。虽然可以使用静态网站构建数百个页面，但这始终是一个缓慢而漫长的过程。网页因为没有连结储存使用者信息的数据库，无法针对每个使用者提供客制化的内容。
2. 管理效率低。静态网站的创建速度可能更快，但管理起来可能更耗时。 因为需要逐页编辑静态网站，并且随著网站页面更多，不断大量更新快速变化的内容耗时又耗力。

使用服务器端脚本(server-side script)和技术构建的动态网站允许根据用户行为，即时地显示每个页面的不同内容，例如，每个人的 YouTube 首页显示的推荐影片都不相同，因为 YouTube 会根据数据库中储存的使用者的观看纪录、习惯、订阅内容等等的因素改变推荐影片。

通常，动态网站用于内容繁重且与用户互动频繁的网站。假设我们要架设的网站是房地产网站。我们需要生成数百个页面来列出数百个房市资讯，且这些页面上的内容需要反映即时的可用资讯，我们就需要选择用动态网页。电子商务网站、社群网站、在线论坛、会员网站、串流影音平台等等是其他常见的动态网页类型。

动态网页的优点在于：

1. 维护更容易且更快。使用数据库来储存数据，每个网页的制作依赖服务器端脚本(server-side script)去抓取资讯并且生成网站。
2. 可扩展性。 若从一开始就没有计划建立一个大型网站，动态网站的架构也可以让我们在必要时进行扩展。
3. 更好的用户体验。动态网站提供根据用户需求量身定制的内容。
4. 功能更强大。服务器端脚本可用更多更强大的演算法来增加网页功能性。

动态网页的缺点在于：

1. 需要更多资源才能建立。由于设定数据库并将其连接到正确页面所需的额外步骤，动态网站的设置和运行可能会更加复杂，这也意味着成本更高。
2. 性能问题。动态网站比静态网站有更多的处理指令，不断从数据库提取信息以显示网页内容都需要时间来处理和执行。

# 后端网页开发工具

- PHP、Laravel (PHP Framework)
- Node.js, Express.js (Server-Side JavaScript)
- Java 、Java Spring Framework
- Ruby on Rails
- Python Django、Flask Framework

# Node.js

Node.js 是能够在服务器端运行 JavaScript 的开放原始码、跨平台执行环境。在 Node.js 出现之前，JavaScript 通常作为浏览器上的客户端程式设计语言使用，以 JavaScript 写出的程式通常能够在使用者的浏览器上执行。Node.js 的出现使 JavaScript 也能用于服务器端脚本编写。

Node.js 内部采用 V8 JavaScript 执行引擎作为核心引擎。

## Module Wrapper

在 Node.js 当中，module 是指一组的程式码，组织成简单或複杂功能，可被用来与外部其他程式码连结。Module 可以是单个文件，或是多个文件与文件夹的集合。

在执行 module 的程式码之前，Node.js 将使用如下所示的函数包装器来包装它：

```javascript
(function (exports, require, module, __filename, __dirname) {
  // Module code actually lives in here
});
```

这样做的好处有：

1. 让使用这个 module 的文件中，所使用的 global variable 不会被 module 内部的变量影响。
2. 让 module 内部所定义的 global variable 变成 function scope。
3. 让 module 内部的 JS 文件可以使用某些实用的变数，例如 module、exports 可以用来输出本身 module，而 require 可以用来获得其他 module。
4. \_\_filename, \_\_dirname 等等变量在开发上变得方便，因为两者包含 module 的绝对路径名称与文件夹路径。

## Node.js Modules

Node.js 的 modules 分成三种：

1. Node.js 内建的 modules，可以直接拿来使用。

   fs (file system) module

   ```javascript
   // fs (file system)
   const fs = require("fs");

   // fs.writeFile("myFile.txt", "今天月色真美", (e) => {
   //   if (e) throw e;
   //   console.log("写完啦");
   // });

   fs.readFile("myFile.txt", "utf-8", (e, data) => {
     if (e) throw e;
     console.log(data);
   });
   ```

2. 我们自己制作的 modules。

3. 网路上第三方制作的 modules，可以透过 npm (node package manager)下载来使用。

## Self-Made Modules

在 Module Wrapper 中提供的变量：

- module 变数是个对象，此物件包含此文件的内部信息，包含 id, path, exports, parent, filename 等等信息。
- exports 是 module 对象的属性，本身是个 empty object。
- require 是一个 function，可以读取一个 JavaScript 文件，执行该文件，然后 return 这个文件的 exports object。若读取的是一个文件夹，则读取该文件夹内的 index.js 文件，执行该文件，然后 return 这个文件的 exports object。

# IP, DNS, Port

IP 地址（英语：IP Address，全称 Internet Protocol Address），又译为国际网路协定地址，是网际协定中用于标识传送或接收资料的装置的一串数字。（相当于每个在网路上的电脑的地址）

常见的 IP 位址分为 IPv4 与 IPv6 两大类，IP 位址由一串数字组成。IPv4 为 32 位元长，通常书写时以四组十进位数字组成，并以点分隔，如：172.16.254.1 ；IPv6 为 128 位元长，通常书写时以八组十六进位数字组成，以冒号分割，如：`2001:db8:0:1234:0:567:8:1`。

IPv4 中的每 8 个 digit 都会被转换为 0 到 255 之间的整数； 因此，IPv4 通常是 168.1.7.0 而不 10101000.00000001.00000111.00000000。用前者更容易让人记忆。

根据 IPv4 地址的格式，全世界有多少个不同的设备可以同时上网？32bits 可以制作出 2^32 个不同的 IP 地址。 2^32=4294967296, ，约 43 亿。 但是，这个世界上大约有 72 亿人，且每个人可能拥有超过 1 个与网路连接的设备，所以用 IPv4 地址的格式可能会有一天不够用。
因此，IPv6 于 1990 年代引入； IPv6 使用 128 位元，将确保地球上的每一个人、装置、每一块岩石和沙子都能够拥有一个 IPv6 地址。

Domain Name System，缩写：DNS，是网际网路的一项服务。它作为将域名(Domain Name)和 IP 位址相互对映的一个分散式资料库，能够使人更方便地存取网际网路。DNS 旨在让人们记住域名，而不是无意义的数字。 例如，记住www.youtube.com比记住168.112.0.12更容易。一个简单的DNS系统可以是：

| Domain Name | IP Address   |
| ----------- | ------------ |
| youtube.com | 168.112.0.15 |
| example.com | 167.3.22.19  |
| google.com  | 168.0.1.3    |

服务器中的 port 是网路通讯连接时，逻辑上的端点(endpoint)，用于在服务器和客户端之间交换信息。 每个 port 被分配一个唯一的数字来单独识别它们。一些最常用的端口及其相关的网络协议是：

| Port 号码 | 用途                                                                                                                 |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| 20, 21    | File Transfer Protocol (FTP). FTP is for transferring files between a client and a server.                           |
| 22        | Secure Shell (SSH). SSH is one of many protocols that create secure network connections.                             |
| 25        | Simple Mail Transfer Protocol (SMTP). SMTP is used for email.                                                        |
| 80        | Hypertext Transfer Protocol (HTTP).                                                                                  |
| 443       | HTTP secure (HTTPS). All HTTPS web traffic goes to port 443.                                                         |
| 3389      | Remote Desktop Protocol (RDP). RDP enables users to remotely connect to their desktop computers from another device. |

例如，若 Google 服务器是https://www.google.com，我们希望发出HTTPs Request，则可以对著[https://www.google.com:443](https://www.google.com/)发出请求，即可连线到 Google 服务器上处理 HTTPs 请求的 port。因为没有必要显示，所以网址后面的*:443*通常在网页浏览器上是看不到的。

另一方面，Google 服务器有著 24 小时不停止运作的脚本语言，在处理任何来自 port 443 的请求。脚本的 Pseudocode 如下：

```javascript
app.listen(20, () => {}); // return a file to client, 处理FTP请求

app.listen(25, () => {}); // return an email to client, 处理SMTP请求

app.listen(443, () => {}); // return a webpage to client, 处理HTTPs请求
```

# localhost:3000

在电脑网络中，localhost (意为“本地主机”，指“这台电脑”)是给迴路网络接口（loopback）的一个标准主机名，相对应的 IP 位址为 127.0.0.1（IPv4）。在 DNS 中，localhost 这个 domain name 会被换成 127.0. 0.1。

我们可以在自己的电脑上面架设并且运行服务器。当我们要使用同一台电脑连结到在自己的电脑上面服务器，可以透过寄送请求到 localhost 到自己的电脑上，这就是回路网络接口（loopback） 。

通常我们在本机上的网页服务器，都是使用 port 3000 或是 8080(但基本上，也可以设定任何 1000 到 9999 内的数字)。

# HTTP Request and Response Header

HTTP Request 以及 Response 的基本规定格式如下：

- Request-Line for HTTP Request, Status-Line for HTTP Response
- Header
- An empty line indicating the end of the header fields
- Optionally a message section

一个基础的 Get Request 会是：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080243338.png)

一个基础的 Response 会是：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080244184.png)

如果网页交出表格数据，且使用 GET request 的话，会是：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080244765.png)

Post Request 内部有表格数据的话，会是：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080245363.png)

带有 cookie 设定的 response：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080246400.png)

带有 cookie 设定的 request：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080246175.png)

# NPM

NPM 是 Node Package Manager，是 Node.js 预设的套件管理系统。 npm 会随着 Node.js 自动安装。透过 npm，我们可以在 CLI (Command-Line Interface)下指令，命令电脑从网路上下载别的开发者发佈到网路上的 node packages。Module 是指具有一些功能的单个 JavaScript 文件。 Package 是一个文件夹，其中包含一个或多个 modules。

若我们希望目前的 work directory 可以使用 npm 来下载别的开发者发佈到网路上的 node packages，并且管理这些 packages，需要先做指令：

```bash
npm init
```

所有 npm 管理的 packages 可以在 package.json 的文件中找到名称以及版本。

指令的语法是：

```bash
npm install <package>
```

若要安装特定版本的 package，指令的语法是：

```bash
npm install <package>@<version>
```

以上的 npm 安装语法，都只会将 package 安装在 work directory 中，名为 node_modules 的资料夹中。若使用

```bash
npm install –g <package>
```

则可以将 package 放到作业系统内部。这代表，我们可以在任何的 work directory 内部使用这个 package。
