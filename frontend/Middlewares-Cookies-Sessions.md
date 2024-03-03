---
title: 'Middlewares, Cookies, Sessions'
tags:
  - Cookies
  - Sessions
  - 前端
  - Express.js
categories: 学习
cover: 'https://cdn.cbd.int/xiansakana-blog-img/202311222254147.jpg'
abbrlink: faaf9cfa
date: 2023-11-22 22:54:01
---

# Express Middlewares

Express 中的 Middleware(中间件)除了可以放在所有的 routes 之前，也可以放在 route 内部的 path 以及 callbackFn 之间。语法是：

```javascript
app.METHOD(path, middlewareFn, callbackFn);
```

Middleware 中的 callbackFn 内可以有三个参数，分别为 req, res, 以及 next。若我们希望用 middleware 来处理错误，则可以改用包含四个参数的 callbackFn。四个参数分别为：err, req, res, next (顺序不能换)。

在 try catch block 内部，我们可以把 catch()到的错误，用 next()往 middleware 的方向传送。此时，我们在 express 的 app.use()所使用的 callbackFn 则需要四个参数： err, req, res, 以及 next。

# express.Router

随着服务器的扩大，routes 的数量可能变得非常巨大。此时，将 routes 根据功能分类就变得相当重要。 Express.js 提供了 express.Router 的功能，让我们可以将 routes 分门别类。 express.Router 的语法为：

```javascript
const express = require("express");
const router = express.Router();
router.use(...);
router.get("/", (req, res) => {
  res.send("Birds home page");
});
module.exports = router;
```

在主要的 controller 内部，则可以写：

```javascript
const birds = require('./birds’);
// ...
app.use('/birds', birds);
```

# Cookies

Cookies 是服务器传送给浏览器，并在客户端下次访问同一网站时一同发回的一小段文字。

它帮助该网站保留使用者的偏好设置（例如登入账号、语言、字体大小及其他设定），以便使用者再次访问该网站或浏览该网站的不同网页时无需重新填写那些资料。 Cookie 会被放在客户端的浏览器内部（例如，在 Chrome 浏览器内，点选 Settings，点击 Privacy and security，再点击 Cookies and other site data，就可以看到所有的 cookies）。

Cookies 是以 key-value pair 的形式储存于浏览器内的。每个 Cookies 都有绑定特定的网站。若网站 A 给我们一个 cookie，则下次我们访问网站 A 时，这组 cookie 也会被传送到网站 A 的服务器。在 Express 的服务程式码当中，设定 cookie 的语法是：

```javascript
res.cookie(key, value);
```

```javascript
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  return res.send("这是首页。");
});
app.get("/setCookie", (req, res) => {
  res.cookie("yourCookie", "Oreo");
  return res.send("已经设置Cookie...");
});
```

下次同个浏览器传送 HTTP request 到我们的服务器时，我们可以用 cookieParser()这个 middleware，之后就可以透过 req.cookies 这个属性来获取我们的服务器曾经存在客户端的资料。

![](https://cdn.cbd.int/xiansakana-blog-img/202311181819729.png)

```bash
npm install cookie-parser
```

```javascript
const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/seeCookie", (req, res) => {
  return res.send("看一下已经设定好的Cookie..." + req.cookies.yourCookie);
});
```

由于 cookies 可在客户端的浏览器内被自由修改，我们可以在传送 cookie 之前，帮 cookie 做签名(sign)。签名后的 cookie 被称为 signed cookie。若客户端对 signed cookie 做修改的话，我们的 Express 服务器可以抓到这个错误，并且确认修改过的 cookie 为无效 cookie。

在 Express 当中，若要对 cookie 做签名的话，我们需要先下载 cookie parser，并且在 cookieParser()这个 function 内部提供一个参数。此参数为某个秘密 String。在寄送 cookie 之前时，我们需要设定 signed 属性为 true：

```javascript
res.cookie(key, value, { signed: true });
```

下次同个浏览器传送 HTTP request 到我们的服务器时，我们可以用 req.signedCookies 这个属性获得未签名的 cookies。

![](https://cdn.cbd.int/xiansakana-blog-img/202311181821771.png)

```javascript
app.get("/setCookie", (req, res) => {
  // res.cookie("yourCookie", "Oreo");
  res.cookie("yourCookie", "Oreo", { signed: true });
  return res.send("已经设置Cookie...");
});
app.get("/seeCookie", (req, res) => {
  console.log(req.signedCookies);
  return res.send("看一下已经设定好的Cookie..." + req.signedCookies.yourCookie);
});
```

# Signing Cookies

在计算机科学当中，哈希函数的功能是，把信息或数据压缩成摘要(或指纹)，或使得数据量变小或变大，将数据的格式转换，重新建立一个叫做哈希值(hash values)。好的哈希函数应该要有以下的特点：

1. 一致性：每次我们给 hash() 函数提供相同的输入时，我们需要得到相同的输出。不同长度的输入也应该有相同长度的输出。
2. 均匀分布：这样的好处在于，可以减少 hash collision 的发生(hash collision 是指两个不同的 input 却算出相同的 hash value)。
3. 不可逆性：杂凑函数不应该是可逆的，不然很容易被破解。
4. 雪崩效应：输入的微小变化会导致输出的巨大差异。增加 hash function 的不可逆性。

![](https://cdn.cbd.int/xiansakana-blog-img/202311181822963.png)

SHA 演算法是 Secure Hash Algorithm 的缩写，一种密码哈希函式算法标准，由美国国家安全局研发。其下又可再分为六个不同的算法标准，包括了：SHA-224、SHA-256、SHA-384、SHA-512、SHA-512/224、SHA-512/256。以上总称 SHA 家族。

为了确保 Cookies 没有在客户端被篡改过，帮 Cookies 做签名需要用到的演算法叫做 HMAC(Hashed MAC)。根据 RFC 2104，HMAC 的数学公式为：

$$
𝐻𝑀𝐴𝐶(𝐾, 𝑚) = 𝐻((𝐾’ ⨁ 𝑜𝑝𝑎𝑑) || 𝐻((𝐾’ ⨁ 𝑖𝑝𝑎𝑑) || 𝑚))
$$

- H 为密码哈希函数(Cryptographical Hash Function)，例如 SHA 家族。
- K 为密钥(secret key)，而 m 是信息。
- K’是从密钥 K 生成的另一个密钥。如果 K 小于 H 要求的最短长度，则向右填充零。如果大于 H 要求的长度，则对 K 进行哈希运算。
- || 代表串接， ⨁ 代表 XOR 运算。
- opad、 ipad 都是十六进位的常数， opad = 0x5c5c….5c、ipad = 0x3636…36。

实现 HMAC 的虚拟码是：

![](https://cdn.cbd.int/xiansakana-blog-img/202311191431403.png)

Cookie 签名的完整流程是：

1. 服务器将 value 以及 secret 拿去做运算，得到 HMAC 值。 HMAC 就是我们的 Signed Cookies。
2. 服务器将 signed cookies 以及 key 送到客户端。
3. 客户端或许会篡改 signed cookies。
4. 客户端下次发送 HTTP request 到服务器时，服务器会将 value 以及 secret 拿去做运算，得到 HMAC 值。再将 HMAC 值与客户端送来的 signed cookies 对照。如果两者不同，则代表 signed cookies 遭到篡改。服务器即认定此为无效的 signed cookies。

# Cookies and Storage

Cookies 以及 storage (local storage、session storage 的统称) 的差别在于：

|            | Cookies                                | Storage                        |
| ---------- | -------------------------------------- | ------------------------------ |
| Purpose    | 服务器端读取数据，保留使用者的偏好设置 | 运行在用户端的储存空间         |
| HTTP       | 会随着 HTTP 请求送到服务器端           | 不会随着 HTTP 请求送到服务器端 |
| Data Size  | 对每个网站来说，最大 4095Bytes         | 最大 5MB                       |
| Expiration | 有可能会过期                           | 不会过期                       |

# Sessions

使用 Cookies 可能会有以下两个问题：

1. Cookies 能够储存的数据量有限，最多不能超过 4095 bytes。
2. 因为 Cookies 可以被轻易修改，会引发安全性问题。假定我们的网页可以让使用者登入，并且透过 cookie 记住使用者，使得使用者不需要重复登入网页。若我们将 MongoDB 的 id 当作 cookie 放到使用者的浏览器内，此时， 用户可以编辑他浏览器上的 cookie 并成为其他用户，甚至如果够幸运的话，可以变成是网站的管理员。

为了解决这些问题，我们可以在服务器端使用 Sessions。

Session 是在网页服务器上的储存空间。当使用者登入网页时，服务器会制作一个 session id，以及此 session id 所相对应的数据。 Session id 会被当作 cookie 送到用户端。下次用户端造访同一网站时， Session id 会被以 cookie 的形式送到服务器，而服务器使用 session id 找到所相对应的资料，来确认使用者的身份。如此一来，我们可以解决两个 cookie 的隐患：

1. 服务器上的储存空间不受 4095bytes 的容量限制。
2. 如果用户篡改了自己的 session id，有没有可能冒充其他使用者呢？有可能，但是 session id 通常是非常长的 String，可能性非常的多，比密码更难猜。

随意修改 session id 只会造成服务器无法辨认 session id。若要靠修改 session id 来冒称他人，与尝试猜测 session_id 相比，他们尝试猜测其他人的密码会更有可能达成冒充他人的意图。

另外，在发出 session id 之前，我们可以对 session id 签名。若有人篡改 cookie 内的 session id，我们可以快速识别出来。

![](https://cdn.cbd.int/xiansakana-blog-img/202311191444376.png)

![](https://cdn.cbd.int/xiansakana-blog-img/202311191444947.png)

在 Express 所架设的伺服器内，若要使用 sessions，则可以使用套件 express-sessions。 express-sessions 的语法为

```javascript
app.use(
  session({
    secret: "keyboard cat",
    resave: false,
    saveUninitialized: false,
    cookie: { secure: true },
  })
);
```

- secret – 用来帮 session ID 做成的 cookie 签名。
- resave – 强制将此 session 重新保存回服务器上的 session 存储区，即使在上次到本次的 HTTP request 期间，从未修改过此 session 。预设值为 true，但建议使用 false。使用 true 的话，可能会在服务器上导致 race condition。例如，客户端向服务器发出两个并行 request，则某个 request 对 session 所做的改变会在另一个 request 结束时被覆盖。
- saveUninitialized – 当 request 送到服务器时，如果 request 的 header 内部没有包含 session id 的 cookie 的话，服务器会
  1. 生成独特的 session id。
  2. 将 session id 存到 cookie 内，寄给用户端。
  3. 创建一个 empty session object
  4. 根据 saveUninitialized 的值，在 request 结束时， session object 可能会被储存在服务器内。

> 若在 request 的整个生命周期内， session object 都没有被修改的话，那么在请求结束时，如果 saveUninitialized 为 false 时，则 session object 不会被存在数据库内。 Uninitialized 的意思是指 new but not modified。
>
> saveUninitialized 的预设值是 true，但建议使用 false。使用 false 的好处在于， 服务器可以防止在系统中存储大量 empty session object。由于没有任何有用的信息需要用 session 来储存， session object 在 request 结束时被删除。
>
> 何时会 modify session object 呢？例如，使用者登入系统时， session object 会更新最近一次登入的时间。如果某个使用我们网站的人，只是走走逛逛没有登入，那么 session object 从被创建到 request 结束都不会被更改，所以属于 new but not modified，也就是 Uninitialized 。
>
> 此外，在 saveUninitialized 使用 false 也可以降低伺服器出现 race condition 的情况。

- cookie: { secure: true } – 若设定 secure 为 true，则 cookies 只有在 HTTPs 的协议下才会进行传输。任何不安全的传输通道上，cookie 都不会被传递。

```javascript
const cookieParser = require("cookie-parser");
const session = require("express-session");
app.use(cookieParser("熊猫很可爱"));
app.use(
  session({
    secret: "熊猫跟猫熊哪个是对的",
    resave: false,
    saveUninitialized: false,
    cookie: { secure: false }, // localhost
  })
);
```

# express-sessions

如果我们想要获得 session id 所相对应的 session data，我们只需要在 Express 当中取得 request object 的 session 属性即可：

```javascript
req.session;
```

```javascript
app.get("/setSessionData", (req, res) => {
  req.session.example = "something not important...";
  return res.send("在服务器设置session数据，在浏览器设置签名后的session id");
});
```

另外，express-sessions 给客户端设定的 cookie 名称是 connect.sid，而 value 则是签名过的 session id。

```javascript
app.get("/seeSessionData", (req, res) => {
  console.log(req.session);
  return res.send("看一下已经设定好的Session数据");
});
```

```javascript
const checkUser = (req, res, next) => {
  if (!req.session.isVerified) {
    return res.send("请先登入系统，才能看到秘密。");
  } else {
    next();
  }
};

app.get("/verifyUser", (req, res) => {
  req.session.isVerified = true;
  return res.send("你已经被验证了。。。");
});

app.get("/secret", checkUser, (req, res) => {
  return res.send("秘密是，柴犬很可爱。。。");
});

app.get("/secret2", checkUser, (req, res) => {
  return res.send("秘密是2，骆驼很可爱。。。");
});
```

# 环境变量

直接在程序码内储存秘密是一个不好的习惯。通常来说，我们会把秘密存在环境变量内部。环境变量(environment variable)是一个动态的值，可以影响电脑上运行的程序。它们是正在运行程序的一部分。

例如，一个正在运行的程序可以查询 TEMP 环境变量的值来发现一个合适的位置，来存储临时的文件，或者查询 HOME 变量来找到运行该程序的用户所拥有的目录结构。

在 Node.js 当中，我们使用 dotenv 套件，透过 process 对象的 env 属性，来获得环境变量。 (除此之外，如果我们在云端上部署服务器，通常云端提供商应该有某种秘密管理工具，例如 AWS Secrets Manager。)

```javascript
require("dotenv").config();
const cookieParser = require("cookie-parser");
const session = require("express-session");
app.use(cookieParser(process.env.MYCOOKIESECRETKEY));
app.use(
  session({
    secret: process.env.MYSESSIONSECRETKEY,
    resave: false,
    saveUninitialized: false,
    cookie: { secure: false }, // localhost
  })
);
```

```env
MYCOOKIESECRETKEY="熊貓很可愛"
MYSESSIONSECRETKEY="熊貓跟貓熊哪個是對的?"
```

```gitignore
.env
```

# Flash

Flash 是在 session 当中一个特别的储存空间，可以用来储存一些简短的信息。例如，登入成功或是登入失败的信息。如果要使用 flash，可以使用 connect-flash 套件。

```javascript
app.use(flash());

app.get("/", (req, res) => {
  req.flash("message", "欢迎来到网页。。。");
  return res.send("这是首页。" + req.flash("message"));
});
```
