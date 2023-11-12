## Express.js

Express.js是针对Node.js的应用框架(framework)，建构在Node.js之上，其主要目的是为了对Node.js架设的后端伺服器简化程式码并且增加开发速度 (这就是为何Express叫做Express) 。要使用Express，我们只需要在work directory中做：
```bash
npm install express 
```

## Framework and Library

Framework 与 Library是两个开发者常用的词汇。两者并没有学术上的定义，但基本的区别是：

使用 Library 就像从头开始建造你的家。房子可以按照你喜欢的任何风格建造，房间可以按照你喜欢的方式佈置和装饰。另一方面， Framework就像买新房一样。房子已经建好了，所以你不用担心建筑问题，但你不能选择房子的格局以及房间的布置方式。

在Library当中通常会提供许多的功能，开发者可以自行选择所需的部分取用，例如：Bootstrap是HTML, CSS的Library。jQuery是JavaScript的Library。另一方面，Flask是Python的web framework，开发者必须要依照Flask的规则架构进行开发，没有自行选择架构的自由。

## HTTP Request Methods

HTTP协议中，客户端可以向伺服器发出请求(request)。常见的请求method分成以下几种：

- GET – 用于请求指定的数据。使用 GET 的请求只应用于取得数据。
- POST – 用于提交指定的数据，通常会改变伺服器的状态或已储存的数据。

(以上两种request可由HTML的form当中传送)

我们在浏览器中输入网址，请求网页，都是在向伺服器发出GET request。当我们登入某个网页时，则是发出POST request。发出GET request时，额外的资讯会被放在URL的后面，用`?`当作与端点的分隔符号， `&`为多个资讯间的分隔符号。发出POST request时，额外数据则会被藏起来。

例如，在Google上搜寻panda，网址会变成：
https://www.google.com/search?q=panda&oq=what&aqs=chrome..69i57j69i59l3j35i19i39j69i60l3.1158j0j7&sourceid=chrome&ie=UTF-8

![](https://img.xiansakana.xyz/202311080402562.png)

其他常见的request methods是：

- PUT – 用于修改资源的方法，客户端发送更新整个资源的数据。
- PATCH – 用于修改资源的方法，客户端发送要更新的部分数据而不修改整个数据。
- DELETE – 用于删除资源。

以上三种HTTP request皆无法从浏览器发送，只能使用程序语言或是postman等软件发送。

## Express Routing

路由(routing)是指服务器如何回应客户端对特定端点(endpoint)的请求。端点(endpoint)是 URI和特定的 HTTP 请求方法（GET、POST 等）组成的。例如，伺服器上提供气象资讯查询与回报，则伺服器上的endpoint可以有：

- an endpoint that handles GET / weather / taiwan requests.
- an endpoint that handles GET / weather / hongkong requests.
- an endpoint that handles POST / weather / taiwan requests.
- an endpoint that handles POST / weather / hongkong requests

在Express中，制作伺服器端的routing endpoints的语法如下：

- app.listen(port, callbackFn)  - app是个express instance、port是我们可以自行决定的数字，callbackFn是一旦服务器开始监听指定的port， callbackFn就会被执行。
- app.METHOD(PATH, HANDLER) - app是个express instance、METHOD是一个HTTP method，path是endpoint，而handler是一个function，一旦服务器在app.listen()指定的port收到相关method与path的请求，就会执行handler function来回应请求。

当handler function被express执行时，express会自动带入两个对象当作parameter，分别为request object以及response object。这两个对象分别代表HTTP的请求以及回应。因此，handler function通常被写成arrow function expression，且此arrow function一定会有两个parameter：
```javascript
(req, res) => {
    // 从 req拿到资讯
   // 根据拿到的资讯，用 res做回应
}
```

 Response Object常用的methods有：

| Methods                    | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| res.send(body)             | 传送出HTTP Response。Body可以是string, object, array, boolean等等。 |
| res.sendFile(path)         | 将位于path的文件传送出去。                                   |
| res.json(body)             | 发送JSON response。此method会先使用JSON.stringify()将body转换为JSON String后，再发送一个response给客户端。 |
| res.redirect(path)         | 服务器通过发送状态为302的HTTP response要求客户端到path。客户端会重新发送一个HTTP GET response到path。 |
| res.render(view[, locals]) | 将view模板套用locals的文字后，将view发送到客户端。           |
| res.status()               | 设定HTTP Response的status code。                             |

Request object的常用属性为：

| Attributes | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| req.body   | 此属性是一个对象，预设值是undefined，但若使用express.json()或是express.urlencode()这种middleware，可以让内部包含POST request寄来数据信息，并且用key-value pair来表示。 |
| req.params | 此属性是一个对象，内部属性为named route parameters。例如，如果我们有route是/user/:name，则"req.params.name"属性可取得route当中的name的值。此对象默认为{}。 |
| req.query  | 此属性是一个对象，其中包含route中`?`后面的key-value pair。例如，如果我们有route是/api/getUser/?id=1，则req.query.id就会是1。 |

express.json()会去检查requests的header有没有Content-Type: application/json。如果有，就把text-based JSON换成JavaScript能够存取的JSON对象。

express.urlencoded()会去检查requests的header有没有Content-Type: application/x-www-form-urlencoded （也就是去检查是不是带有数据的POST request）。如果有，也把text-based JSON换成JavaScript能够存取的JSON对象。Extended属性设定为true，可以让JSON对象内部储存String以外的数据类型。

总合来说，express.json()以及express.urlencoded()功能一样，只是处理的Content-Type不同。两者转换完成的JSON对象会被放入req.body。

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

## Express Middleware

Middleware(中间件)是指从发出HTTP请求后，到服务器回复回应前，用来做特定用途的程式。每个Middleware可以针对所收到的对象进行修改或解析，处理后再来决定是否要继续把对象继续传递给下一个middleware。在Express.js中，最基础的使用middleware的语法是：
```javascript
app.use(callbackFn)
```

不论是GET request, POST request还是其他种类的request methods，app.use()内部的callbackFn都会被Express.js执行。

callbackFn被Express.js执行时，会使用基本的三个参数：req, res, next。next本身是个function。如果目前的middleware不打算结束客户端的请求、也没有传递回应给客户端，就必须呼叫 next()以便将控制权传递给下一个middleware。否则，若是目前的middleware既没有执行next()，也没有给客户端回应，则客户端的request将会停摆。

> 错误处理中间件（error-handling middleware）是专门用来处理错误状况所使用的。撰写错误处理中介软体时， callbackFn则会使用四个参数，分别为为 err、req、res 与 next。err参数代表，当错误发生时，Express.js会把error object当作argument放入callbackFn内部。

除了自己写出app.use()内部的callbackFn之外，我们也可以使用Express的built-in function，放入app.use()内部，例如：

```javascript
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({extended: true}));
```

## Static Files

静态文件(static files)是客户端可以从服务器下载的文件。例如，404错误讯息网页、CSS文件、网页中的图片、JavaScript文件等等，都是网页服务器不需要通过脚本语言去组成的网页，而是可以直接寄送给客户端的文件。

在Express.js当中，预设的情况下是不允许我们提供Static Files。 我们需要先使用middleware才能向客户端提供static files。
```javascript
app.use(express.static('public'));
```

我们需要在work directory当中创建一个文件夹，名称必须是“public”。所有的static files都可以放进public资料夹内部。

> 注意！！当Express查找public资料夹内部的文件时，使用的是相对路径，且public资料夹名称不是URL的一部份。

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

## HTTP Status Code

HTTP 状态码(Status Code)是服务器对任何HTTP请求的回应代码。 当我们寄送请求到服务器后，服务器会使用一个三位数的代码表明一个 HTTP请求是否已经被完成。HTTP Status Code分为五种：

1. 资讯回应 (Informational responses, 100–199)
2. 成功回应 (Successful responses, 200–299)
3. 重定定向 (Redirects, 300–399)
4. 用户端错误 (Client errors, 400–499)
5. 服务器端错误 (Server errors, 500–599)

最常见与最常使用的HTTP Status Code：

| Code                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| 200 OK                   | 表示请求成功。                                               |
| 201 Created              | 请求成功且新的资源成功被创建，通常用于POST或一些PUT请求后的回应。 |
| 302 Found                | 表示请求资源的URI已临时更改，将来可能会对URI进行新的更改。因此，客户端在以后的请求中应该使用相同的URI。 |
| 400 Bad Request          | 表示服务器因为收到无效语法，而无法理解请求。                 |
| 401 Unauthorized         | 需要授权以回应请求。这有点像403，但这里的授权，是有可能办法到的。 |
| 403 Forbidden            | 用户端并无访问权限，例如未被授权，所以服务器拒绝给予回应。不同于401，服务端知道用户端的身份。 |
| 404 Not Found            | 服务器找不到请求的资源，因为在网路上很常出现，此状态码也许最为人所知。 |
| 500 Internal Sever Error | 服务器端发生未知或无法处理的错误。                           |

![](https://img.xiansakana.xyz/202311080543609.png)

## 302 Found

![](https://img.xiansakana.xyz/202311080544644.png)