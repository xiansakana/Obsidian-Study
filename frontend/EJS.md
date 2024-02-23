---
title: EJS
tags:
  - EJS
  - 前端
  - Express.js
cover: "https://img.xiansakana.xyz/202311121034957.jpg"
categories: 学习
abbrlink: 71e431f8
date: 2023-11-12 10:45:48
---

VScode extension: EJS language support

## EJS

EJS 的全名是“Embedded JavaScript”，是与 Express.js 搭配的内嵌式的样板引擎。 EJS 可以让我们使用 JavaScript 生成 HTML 页面 。 EJS 文件需要放在“views”文件夹内部。

页面渲染(rendering)就是浏览器将 HTML 变成人眼看到的图像的全过程。Express.js 当中的 View Engine 允许我们使用模板文件渲染网页。这些模板填充了实际数据并从服务器被传送到客户端。

若有使用 app.set(“view engine”, “ejs”)，则使用 res.render()时，就不需要指定文件类别。例如， res.render(“index.ejs”)可以改成 res.render(“index”)。

```javascript
const express = require("express");
const app = express();

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("index");
});

// port, callback
app.listen(3000, () => {
  console.log("服务器正在port3000运行。。。");
});
```

## EJS 语法

- <% 一般标签，用于 control flow，不输出任何的值。
- <%= 将值输出到模板中（不会转换 HTML 语法）。例如： x = “<p>This is a paragraph</p>”，则<%= x %>会是输出<p>This is a paragraph</p>。
- <%- 将转换过的 HTML 语法的值输出到模板中。例如： x = “<p>This is a paragraph</p>”，则<%- x %>会是输出 This is a paragraph。

```javascript
const express = require("express");
const app = express();

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  let myString = "<h1>hello world</h1>";
  res.render("index", { myString });
});

// port, callback
app.listen(3000, () => {
  console.log("服务器正在port3000运行。。。");
});
```

```ejs
<% for (let i = 0; i < 10; i++){ %> <%= myString %> <% } %>
```

- <%# 注释标签，不执行也不输出任何的值。
- %> 普通的结束标签。
- <%- include %> 语法可以镶嵌其他 EJS 文件。

```ejs
<%- include("partials/footer") %>
```

## EJS 应用

```javascript
const express = require("express");
const app = express();

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  const languages = [
    { name: "Python", rating: 9.5, popularity: 9.7, trending: "super hot" },
    { name: "Java", rating: 9.4, popularity: 8.5, trending: "hot" },
    { name: "C++", rating: 9.2, popularity: 7.7, trending: "hot" },
    { name: "PHP", rating: 9.0, popularity: 5.7, trending: "decreasing" },
    { name: "JS", rating: 8.5, popularity: 8.7, trending: "hot" },
  ];
  res.render("index", { languages });
});

// port, callback
app.listen(3000, () => {
  console.log("服务器正在port3000运行。。。");
});
```

```ejs
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="/style.css" />
  </head>
  <body>
    <table>
      <tr>
        <th>名称</th>
        <th>评价</th>
        <th>热门程度</th>
        <th>流行度</th>
      </tr>
      <% languages.forEach(lang =>{%>
      <tr>
        <td><%= lang.name %></td>
        <td><%= lang.rating %></td>
        <td><%= lang.popularity %></td>
        <td><%= lang.trending %></td>
      </tr>
      <%}) %>
    </table>
  </body>
</html>
```

## [MVC 模式](https://developer.mozilla.org/zh-CN/docs/Glossary/MVC)

MVC 模式(Model–View–Controller)是软件工程中的一种 design pattern (软件架构模式)，把软体系统分为三个基本部分：模型（Model）、视图（View）和控制器（Controller）。

MVC 模式的目的是实现一种动态的程式设计，使后续对程式的修改和扩充简化，并且使程式某一部分的重复利用成为可能。除此之外，此模式透过对复杂度的简化，使程式结构更加直觉。软件系统透过对自身基本部分分离的同时也赋予了各个基本部分应有的功能。

现代的网页开发框架，例如 Java Spring、ASP .NET、 Ruby on Rails、 Django、 Laravel 等等，都是使用相当标准的 MVC design pattern。

Model、View、Controller 的分工如下：

- 模型(Model) – 封装与应用程式的逻辑相关的数据以及对数据的处理方法。“ Model ”有对数据直接存取的权力，例如对数据库的存取。
- 视图(View) – 将数据有目的的显示出来。
- 控制器(Controller ) – 用于控制应用程式的流程，处理事件并作出回应。“事件”包括使用者的行为和 Model 上的改变。

![](https://img.xiansakana.xyz/202311101555610.png)

![](https://img.xiansakana.xyz/202311101556554.png)

采用 MVC design pattern 的优点有：

1. 重复使用已写好的程式码：model, view, controller 各司其职，不同的 view 可以使用同一个 model 连结数据库，产出不同的页面，增加开发效率。
2. 容易维护的程式码：由于 MVC 彼此独立，因此，将现有的 project 扩大或是修改都可以不破坏现有架构。
3. 团队分工合作：view、model、 controller 可由不同专业的人分工处理。例如，view 交由前端工程师美化处理、model、controller 则是由后端或资料库人员负责。
