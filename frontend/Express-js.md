---
title: Express.js
tags:
  - Express.js
  - 前端
cover: "https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311121025991.jpg"
categories: 学习
abbrlink: fcc95608
date: 2023-11-12 10:24:29
---

# Express.js

Express.js 是针对 Node.js 的应用框架(framework)，建构在 Node.js 之上，其主要目的是为了对 Node.js 架设的后端伺服器简化程式码并且增加开发速度 (这就是为何 Express 叫做 Express) 。要使用 Express，我们只需要在 work directory 中做：

```bash
npm install express
```

# Framework and Library

Framework 与 Library 是两个开发者常用的词汇。两者并没有学术上的定义，但基本的区别是：

使用 Library 就像从头开始建造你的家。房子可以按照你喜欢的任何风格建造，房间可以按照你喜欢的方式佈置和装饰。另一方面， Framework 就像买新房一样。房子已经建好了，所以你不用担心建筑问题，但你不能选择房子的格局以及房间的布置方式。

在 Library 当中通常会提供许多的功能，开发者可以自行选择所需的部分取用，例如：Bootstrap 是 HTML, CSS 的 Library。jQuery 是 JavaScript 的 Library。另一方面，Flask 是 Python 的 web framework，开发者必须要依照 Flask 的规则架构进行开发，没有自行选择架构的自由。

# HTTP Request Methods

HTTP 协议中，客户端可以向伺服器发出请求(request)。常见的请求 method 分成以下几种：

- GET – 用于请求指定的数据。使用 GET 的请求只应用于取得数据。
- POST – 用于提交指定的数据，通常会改变伺服器的状态或已储存的数据。

(以上两种 request 可由 HTML 的 form 当中传送)

我们在浏览器中输入网址，请求网页，都是在向伺服器发出 GET request。当我们登入某个网页时，则是发出 POST request。发出 GET request 时，额外的资讯会被放在 URL 的后面，用`?`当作与端点的分隔符号， `&`为多个资讯间的分隔符号。发出 POST request 时，额外数据则会被藏起来。

例如，在 Google 上搜寻 panda，网址会变成：
https://www.google.com/search?q=panda&oq=what&aqs=chrome..69i57j69i59l3j35i19i39j69i60l3.1158j0j7&sourceid=chrome&ie=UTF-8

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080402562.png)

其他常见的 request methods 是：

- PUT – 用于修改资源的方法，客户端发送更新整个资源的数据。
- PATCH – 用于修改资源的方法，客户端发送要更新的部分数据而不修改整个数据。
- DELETE – 用于删除资源。

以上三种 HTTP request 皆无法从浏览器发送，只能使用程序语言或是 postman 等软件发送。

# Express Routing

路由(routing)是指服务器如何回应客户端对特定端点(endpoint)的请求。端点(endpoint)是 URI 和特定的 HTTP 请求方法（GET、POST 等）组成的。例如，伺服器上提供气象资讯查询与回报，则伺服器上的 endpoint 可以有：

- an endpoint that handles GET / weather / taiwan requests.
- an endpoint that handles GET / weather / hongkong requests.
- an endpoint that handles POST / weather / taiwan requests.
- an endpoint that handles POST / weather / hongkong requests

在 Express 中，制作伺服器端的 routing endpoints 的语法如下：

- app.listen(port, callbackFn) - app 是个 express instance、port 是我们可以自行决定的数字，callbackFn 是一旦服务器开始监听指定的 port， callbackFn 就会被执行。
- app.METHOD(PATH, HANDLER) - app 是个 express instance、METHOD 是一个 HTTP method，path 是 endpoint，而 handler 是一个 function，一旦服务器在 app.listen()指定的 port 收到相关 method 与 path 的请求，就会执行 handler function 来回应请求。

当 handler function 被 express 执行时，express 会自动带入两个对象当作 parameter，分别为 request object 以及 response object。这两个对象分别代表 HTTP 的请求以及回应。因此，handler function 通常被写成 arrow function expression，且此 arrow function 一定会有两个 parameter：

```javascript
(req, res) => {
  // 从 req拿到资讯
  // 根据拿到的资讯，用 res做回应
};
```

Response Object 常用的 methods 有：

| Methods                    | Description                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| res.send(body)             | 传送出 HTTP Response。Body 可以是 string, object, array, boolean 等等。                                              |
| res.sendFile(path)         | 将位于 path 的文件传送出去。                                                                                         |
| res.json(body)             | 发送 JSON response。此 method 会先使用 JSON.stringify()将 body 转换为 JSON String 后，再发送一个 response 给客户端。 |
| res.redirect(path)         | 服务器通过发送状态为 302 的 HTTP response 要求客户端到 path。客户端会重新发送一个 HTTP GET response 到 path。        |
| res.render(view[, locals]) | 将 view 模板套用 locals 的文字后，将 view 发送到客户端。                                                             |
| res.status()               | 设定 HTTP Response 的 status code。                                                                                  |

Request object 的常用属性为：

| Attributes | Description                                                                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| req.body   | 此属性是一个对象，预设值是 undefined，但若使用 express.json()或是 express.urlencode()这种 middleware，可以让内部包含 POST request 寄来数据信息，并且用 key-value pair 来表示。 |
| req.params | 此属性是一个对象，内部属性为 named route parameters。例如，如果我们有 route 是/user/:name，则"req.params.name"属性可取得 route 当中的 name 的值。此对象默认为{}。              |
| req.query  | 此属性是一个对象，其中包含 route 中`?`后面的 key-value pair。例如，如果我们有 route 是/api/getUser/?id=1，则 req.query.id 就会是 1。                                           |

express.json()会去检查 requests 的 header 有没有 Content-Type: application/json。如果有，就把 text-based JSON 换成 JavaScript 能够存取的 JSON 对象。

express.urlencoded()会去检查 requests 的 header 有没有 Content-Type: application/x-www-form-urlencoded （也就是去检查是不是带有数据的 POST request）。如果有，也把 text-based JSON 换成 JavaScript 能够存取的 JSON 对象。Extended 属性设定为 true，可以让 JSON 对象内部储存 String 以外的数据类型。

总合来说，express.json()以及 express.urlencoded()功能一样，只是处理的 Content-Type 不同。两者转换完成的 JSON 对象会被放入 req.body。

```javascript
const express = require("express");
const app = express();

// middlewares
app.use((req, res, next) => {
  console.log("正在经过middleware");
});

// res.send(body)
app.get("/", (req, res) => {
  res.send("欢迎来到网站首页");
});

app.get("/anotherPage", (req, res) => {
  res.send("欢迎来到另一个页面");
});

// res.sendFile(path)
app.get("/sendFile", (req, res) => {
  res.sendFile(__dirname + "/example.html");
});

// res.json(body)
app.get("/json", (req, res) => {
  let obj = {
    title: "Web Design",
    website: "udemy",
  };
  res.json(obj);
});

// res.redirect(path)
app.get("/example", (req, res) => {
  res.redirect("/actualExample");
});

app.get("/actualExample", (req, res) => {
  res.send("真正的网页在这里");
});

// req.body
app.post("/formHandling", (req, res) => {
  let { email, password } = req.body;
  res.send("你的邮箱是" + email);
});

// req.params
app.get("/fruit", (req, res) => {
  res.send("欢迎来到水果页面");
});

app.get("/fruit/:someFruit", (req, res) => {
  res.send("欢迎来到" + req.params.someFruit + "页面");
});

// req.query
app.get("/form", (req, res) => {
  res.sendFile(__dirname + "/form.html");
});

app.get("/formHandling", (req, res) => {
  res.send(
    "服务器已经收到表单，你所提交的数据为：名称：" +
      req.query.name +
      "，年龄：" +
      req.query.age +
      "。"
  );
  console.log(req.query);
});

// Not Found
app.get("*", (req, res) => {
  res.send("Not Found");
});

// port, callback
app.listen(3000, () => {
  console.log("服务器正在port3000运行。。。");
});
```

# Express Middleware

Middleware(中间件)是指从发出 HTTP 请求后，到服务器回复回应前，用来做特定用途的程式。每个 Middleware 可以针对所收到的对象进行修改或解析，处理后再来决定是否要继续把对象继续传递给下一个 middleware。在 Express.js 中，最基础的使用 middleware 的语法是：

```javascript
app.use(callbackFn);
```

不论是 GET request, POST request 还是其他种类的 request methods，app.use()内部的 callbackFn 都会被 Express.js 执行。

callbackFn 被 Express.js 执行时，会使用基本的三个参数：req, res, next。next 本身是个 function。如果目前的 middleware 不打算结束客户端的请求、也没有传递回应给客户端，就必须呼叫 next()以便将控制权传递给下一个 middleware。否则，若是目前的 middleware 既没有执行 next()，也没有给客户端回应，则客户端的 request 将会停摆。

> 错误处理中间件（error-handling middleware）是专门用来处理错误状况所使用的。撰写错误处理中介软体时， callbackFn 则会使用四个参数，分别为为 err、req、res 与 next。err 参数代表，当错误发生时，Express.js 会把 error object 当作 argument 放入 callbackFn 内部。

除了自己写出 app.use()内部的 callbackFn 之外，我们也可以使用 Express 的 built-in function，放入 app.use()内部，例如：

```javascript
app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
```

# Static Files

静态文件(static files)是客户端可以从服务器下载的文件。例如，404 错误讯息网页、CSS 文件、网页中的图片、JavaScript 文件等等，都是网页服务器不需要通过脚本语言去组成的网页，而是可以直接寄送给客户端的文件。

在 Express.js 当中，预设的情况下是不允许我们提供 Static Files。 我们需要先使用 middleware 才能向客户端提供 static files。

```javascript
app.use(express.static("public"));
```

我们需要在 work directory 当中创建一个文件夹，名称必须是“public”。所有的 static files 都可以放进 public 资料夹内部。

> 注意！！当 Express 查找 public 资料夹内部的文件时，使用的是相对路径，且 public 资料夹名称不是 URL 的一部份。

```javascript
const express = require("express");
const app = express();

app.use(express.static("public"));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

// port, callback
app.listen(3000, () => {
  console.log("服务器正在port3000运行。。。");
});
```

# HTTP Status Code

HTTP 状态码(Status Code)是服务器对任何 HTTP 请求的回应代码。 当我们寄送请求到服务器后，服务器会使用一个三位数的代码表明一个 HTTP 请求是否已经被完成。HTTP Status Code 分为五种：

1. 资讯回应 (Informational responses, 100–199)
2. 成功回应 (Successful responses, 200–299)
3. 重定定向 (Redirects, 300–399)
4. 用户端错误 (Client errors, 400–499)
5. 服务器端错误 (Server errors, 500–599)

最常见与最常使用的 HTTP Status Code：

| Code                     | Meaning                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| 200 OK                   | 表示请求成功。                                                                                               |
| 201 Created              | 请求成功且新的资源成功被创建，通常用于 POST 或一些 PUT 请求后的回应。                                        |
| 302 Found                | 表示请求资源的 URI 已临时更改，将来可能会对 URI 进行新的更改。因此，客户端在以后的请求中应该使用相同的 URI。 |
| 400 Bad Request          | 表示服务器因为收到无效语法，而无法理解请求。                                                                 |
| 401 Unauthorized         | 需要授权以回应请求。这有点像 403，但这里的授权，是有可能办法到的。                                           |
| 403 Forbidden            | 用户端并无访问权限，例如未被授权，所以服务器拒绝给予回应。不同于 401，服务端知道用户端的身份。               |
| 404 Not Found            | 服务器找不到请求的资源，因为在网路上很常出现，此状态码也许最为人所知。                                       |
| 500 Internal Sever Error | 服务器端发生未知或无法处理的错误。                                                                           |

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080543609.png)

# 302 Found

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311080544644.png)
