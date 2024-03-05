---
title: React
tags:
  - React
  - JSX
  - SPA
categories: 前端
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311222305271.jpg
abbrlink: d8a440d1
date: 2023-11-22 23:04:10
---

# SPA

若我们有一个后端的网路服务(Web Service)已经能够正常运作且受到保护，只有经过身份验证和授权的用户才能调用这个 API，则我们可以使用网页前端的框架来架设网站，并且连结到此 API。

在大多数网站上，当我们点击链接或提交表单时，浏览器会向伺服器发出 request 并下载一个完整的新页面。我们通常会看到白色闪烁，因为当前页面消失并加载了新页面。若使用 AJAX 技术，我们可以编写一些在浏览器上运行的 JavaScript。 JavaScript 将向服务器发出 request ，接收 response 并使用新数据更新当前 HTML 页面。整个过程中，只有数据通过网络传输，而不是一个全新的 HTML 页面。
像这样的页面，就被称为 Single Page Application(SPA)。

这样做有几个优点：

1. 我们减少了服务器的负载。为每个 reqeust 生成一个 HTML 页面需要大量的处理能力。如果我们的服务器的 CPU 太忙，我们的网站就会变慢，并可能变成反应迟钝使我们的网站关闭。在使用网页浏览器时，大多数客户端的 CPU（可能有 8 个或更多）都处于空闲状态。因此，我们可以将数据传到客户端，让客户端的 CPU 驱动浏览器来渲染(render)页面。
2. 我们还减少了需要通过网络传输的数据量，因为只发送新数据，而不是完整的 HTML 页面。

虽然 SPA 有很多优点，但这并不意味着每个网站都应该是 SPA。 SPA 的缺点有：

1. SPA 非常复杂。 SPA 越大，添加的功能越多时，会变得越复杂。最终，复杂性会影响我们网站的性能，并增加 bug 出现的机率。
2. 搜索引擎优化(SEO)会出问题。谷歌和其他搜索引擎有自动扫描程式， 但是，这些自动扫描程式不会运行 JS 代码来加载数据。因此，搜索引擎可能无法正确定位我们的网站。

市面上有几个热门框架可以制作 SPA，包括 React.js（由 Facebook 开发和使用）、Angular.js （ 由 Google 的 Angular 团队以及社群共同领导 ）和 Vue.js。

# React

React（也称为 React.js 或 ReactJS）是一个免费和开源的前端 JavaScript 框架，用 UI 组件来架构使用者介面。它由 Meta（以前的 Facebook）和个人开发人员社区维护。 React 可用作于开发 SPA 网页。 React 的基本原理是，用 JavaScript 来生成 HTML。

> - React Native 是一个 Facebook 研发的开放源码的应用程序框架。 React Native 开发的程序可用于 iOS 和 Android 手机平台。
> - React 常与另一个框架 Next.js 合作使用。
> - 因为 React 还是个相对年轻的框架（初始版本在 2013 的 9 月发布），所以功能上、语法上、套件上都会不断更新。

使用 React 的好处在于：

1. 可重复使用的组件(Reusable Components) – Component 是 React 的核心架构；使用 React 建构的每个应用程序的 UI， 都可以分解为彼此独立的小部分。这些小部分称为 Components。每一个 Component 中的都有自己的程式逻辑，可以单独编辑，然后在最终的 UI 中合并到一起，这使得创建应用程序 UI 的任务更简单，更易于管理。 Component 也可以在其他页面和应用程序上重复使用，从而节省大量的写程式时间。
2. React 最有用的特性之一是，它能够更改网站上的 Components，而无需更新整个 DOM。这是通过虚拟 DOM (virtual DOM)完成的。虚拟 DOM 是 DOM 的虚拟表示(virtual representation)或副本(copy)。每当用户执行操作时，例如点击按钮，React 都会更新虚拟 DOM，将更新后的与之前的版本进行比较，检测差异，然后只更新受影响的对象而不是刷新整个 DOM。这使得网站反应速度更快、性能更高。
3. JSX 代表 JavaScript XML，是 JavaScript 的语法扩展，它允许写程式的人在 JavaScript 代码中，嵌入类似 HTML 语法的程式码。 React 的工作就是将 JSX 换成 DOM 元素。

# Get Started with React

用指令 npx create-react-app app-name 就可以生成一个 React 的专案。 (npx 代表 Node Package Execution，是 npm 内建的功能。Npx 是一个 npm package 运行程序，可以从 npm 拿到 package 并且直接执行，甚至无需在电脑上安装该 package。)
React 专案内的基本架构如下图：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311221652326.png)

文件夹与档案的基本用途如下：

- public folder – 内部放置静态文件，例如 index.html、JavaScript 文件、图片、favicon.ico 和其他档案等等。
  - Public 资料夹内部的 index.html 文件非常重要。用 React 所制作的 Single Page Application 当中所使用的单一页面就是这个 index.html 文件。
- src folder – 是我们 React 应用程序的核心文件夹，包含 Components、index.js、App.js 等等文件。
  - index.js 文件的功能是，将最主要的 React Component 渲染到在 index.html 当中 id 为 root 的标签。
  - App.js 文件的功能是，制作「App Component」。 App Component 的功能是担任其他所有 Component 的容器。因为 React 制作出的网站是一页式的网页，所以网页内容会根据 URL 改变。根据不同的 URL 去做相对应的 route 是 App.js 的责任。
- node_modules – 目录包含所有 React 专案所依赖的 packages，例如 react 、 react-dom 等等。
- .gitignore – 任何列出的文件或资料夹，都不会被 push 上 GitHub。
- package.json – 用来保存与 Project 相关的数据，用于管理 Project 的 dependencies、scripts、versions 等等。
- README.md – 为其他开发人员提供了 GitHub 上的详细描述。

> 环境设定：
>
> - 在 settings.json 中添加
>   ```json
>   "files.associations": { "*.js": "javascriptreact" },
>   "[javascriptreact]": { "editor.defaultFormatter": "esbenp.prettier-vscode" }
>   ```
> - 安装 extension: ES7+ React/Redux/React-Native snippets

# JSX

JSX 的功能让我们可以在 JavaScript 内部，使用类 HTML 的程式码来制作 Component。 （ React 并不要求使用 JSX，但大部分人觉得在 JavaScript 程式码中撰写使用者界面的同时，这是一个很好的视觉辅助）

> 输入 rafce 即可自动生成模板

由于网页浏览器无法理解 JSX 语法，我们需要先做 JSX Transformation。在 React Project 内部的 node_modules 文件夹内，可以找到一个文件夹「babel」。 Babel 是一个 JavaScript 编译器，它可以将不是每个浏览器都可以理解的最新 JavaScript 功能转换为当前和旧浏览器或环境中向后兼容的 JavaScript 版本。 Babel 在 React 的功能在于将 JSX 语法转换成 React Components。

JSX 的特殊语法如下：

1. 我们可以在大括号`{ }`内编写 expression。在程式语言中， Statements 代表一个动作或是指令，例如打印出某个值或是 if statement。 Expression 是会算出某个值的操作，例如一个变数、数学运算或是执行函数等等。基本的原则是，「 An expression is something, while a statement does something. 」在 JSX 当中使用`{ }`可以执行 expression 本身，并且显示 return value。

2. 在 JSX 当中，HTML 的标签内，class 属性都需要改叫做 className。这是因为 class 这个字在 JavaScript 内部是个保留字，所以不能直接写 class。

   ```jsx
   let friends = ["小明", "小华", "小张"];
   return (
     <div className="info">
       <h1>{5}</h1>
       <h1>{5 * 10}</h1>
       <h1>{Math.random()}</h1>
       <p>我的朋友们是：</p>
       {friends.map((friend) => {
         return <p>{friend}</p>;
       })}
     </div>
   );
   // 5
   // 50
   // 0.8830569129511494
   // 我的朋友们是：
   // 小明
   // 小华
   // 小张
   ```

3. 在 JSX 内做 inline-styling 时，需要给 style 属性一个 expression。这个 expression 内部需要放入一个对象，所以 inline-styling 的语法会变成 `style={{}}`。其中，外部的大括号是 JSX expression 语法，内部的大括号是 JavaScript 物件语法。此外，因为连字符(Hyphen)在 JavaScript 有特殊意义，所以不能在 JavaScript 物件的属性使用连字符。因此，在 CSS 中具有连字符的属性都会被换成 camelCase 的语法。例如：background-color 会需要被写成 backgroudColor。

   ```jsx
   const Nav = () => {
     return (
       <nav style={{ backgroundColor: "lightblue" }}>
         <ul>
           <li>
             <a style={{ color: "red", textDecoration: "none" }} href="#">
               首页
             </a>
           </li>
           <li>
             <a style={{ color: "red", textDecoration: "none" }} href="#">
               另一个页面
             </a>
           </li>
         </ul>
       </nav>
     );
   };
   ```

# Props

在 React 当中，每个 Component 都可以有自己的属性(Props, properties)。 Props 可以由 HTML 标签的 attributes 传递给 Component。例如：

```jsx
<Friend name="saltedfish" />
```

若是 Props 传递时，要使用变量，则需要将变量换成 expression：

```jsx
let myName = “saltedfish”;
<Friend name={myName} />
```

Props 会通过 argument 的方式传递给 Component，所以 Component 使用 Props 的语法为：

```jsx
const Info = (props) => {
  return (
    <div className="info">
      <h1>朋友名称：{props.name}</h1>
      <h1>朋友年龄：{props.age}</h1>
    </div>
  );
};
```

或是，我们也可以用 object destructuring 的语法来取得 props 物件内的属性：

```jsx
const Info = ({ name, age }) => {
  return (
    <div className="info">
      <h1>朋友名称：{name}</h1>
      <h1>朋友年龄：{age}</h1>
    </div>
  );
};
```

App.js 中

```jsx
const App = () => {
  let friends = [
    { name: "小明", age: 16 },
    { name: "小华", age: 17 },
    { name: "小张", age: 18 },
  ];
  return (
    <div>
      <Nav />
      {friends.map((friend) => (
        <Info name={friend.name} age={friend.age} />
      ))}
    </div>
  );
};
```

# 事件处理

使用 React element 处理事件跟使用 DOM element 处理事件是十分相似的。它们有一些语法上的差异：

1. 事件的名称在 React 中都是 camelCase，而在 HTML DOM 中则是小写。
2. 事件的值在 JSX 中是一个 function （也是一个 expression，所以我们需要用`{}`符号），而在 HTML DOM 中则是一个 string。 React 事件处理时，会直接执行 expression 内的 function。

例如，在 HTML 当中对`<button>`监听 click 事件时，语法为：

```html
<button onclick="buttonHandler()">按我一下</button>
<script>
  function buttonHandler() {
    console.log("this is running..");
  }
</script>
```

然而，在 JSX 当中的语法是：

```jsx
const buttonHandler = () => {
  alert("你按了button一次");
};
<button onClick={buttonHandler}>按我一下</button>;
```

若要在事件的 callback function 执行时加入参数，如果写：

```jsx
<button onClick={buttonHandler(1)}>按我一下</button>
```

会造成 React 读取程式码时，直接执行了 running(1)这个 function。

因此，我们可以把带有参数的 buttonHandler(1) 放入一个 arrow function expression 内部，做成 button 的 onClick 事件的值：

```jsx
const buttonHandler = (msg) => {
  alert(msg);
};
<button
  onClick={() => {
    buttonHandler("你按了button一次");
  }}
>
  按我一下
</button>;
```

或是

```jsx
const buttonHandler = () => {
  alert("你按了button一次");
};
<button
  onClick={() => {
    buttonHandler();
  }}
>
  按我一下
</button>;
```

# State

使用 React 的其中一个好处在于，能够只更改网站上必须改变的 Components，而无需更新整个 DOM。实现这个功能的工具是 State。State 是透过 React Hooks 当中的 useState 来完成的。

在 React 当中，State 是 Component 所持有的一个对象，此对象包含有关 Component 的数据或信息。 Component 的 State 是可以改变的。每当 Component 的 State 改变时，持有此 state 的所有 Components 都会全部重新渲染(rerender)。 React Components 在其 props 或 state 改变时，都会重新渲染！

> Hooks 是 React 16.8 版本中引入的新功能。它允许在不编写 class 的情况下使用 State 和其他 React 的功能 (class 是 React 旧版本的常见语法)。 Hooks 在 class 内部无法起作用。我们可以理解为，Hooks 是从 function component 中「钩入」React State 和生命周期特性的函数。

useState 的语法为：

```jsx
const [name, setName] = useState(initialValue);
```

name 是 state 的名称，我们可以随意命名，setName 是更新 state 时所使用的函数，initialValue 是 name 这个 state 的初始值。

```jsx
import React, { useState } from "react";
const Info = () => {
  let [name, setName] = useState("小明");
  let age = 20;

  const changeNameHandler = () => {
    setName("小明先生");
  };
  return (
    <div className="info">
      <h1>朋友名称：{name}</h1>
      <h1>朋友年龄：{age}</h1>
      <button onClick={changeNameHandler}>改名按钮</button>
    </div>
  );
};
```

# State Lifting

我们有时会希望两个 Component 之间可以共享某个 state。如果两个 Component 属于不同链同层级或是不同链不同层级，则我们需要将 state 往两边最近的 common ancestor (ancestor component)的方向移动。这样的做法就叫做「state lifting」。

```jsx
// App.js
import Create from "./Create";
import Info from "./Info";
import React, { useState } from "react";

const App = () => {
  let [messages, setMessages] = useState([]);
  return (
    <div>
      <Create messages={messages} setMessages={setMessages} />
      <Info messages={messages} setMessages={setMessages} />
    </div>
  );
};
export default App;
```

```jsx
// Create.js
import React, { useState } from "react";

const Create = ({ messages, setMessages }) => {
  let [input, setInput] = useState("");

  const submitButtonHandler = (e) => {
    e.preventDefault();
    setMessages([...messages, input]);
    setInput("");
  };

  const inputHandler = (e) => {
    setInput(e.target.value);
  };
  return (
    <form>
      <input onChange={inputHandler} value={input} type="text" />
      <button onClick={submitButtonHandler}>Submit</button>
    </form>
  );
};
export default Create;
```

```jsx
// Info.js
import React, { useState } from "react";
import "./styles/style.css";

const Info = ({ messages, setMessages }) => {
  return (
    <div className="info">
      {messages.map((message, index) => {
        return <p key={index}>学习内容是：{message}</p>;
      })}
    </div>
  );
};
export default Info;
```

# useEffect

在程式语言里，一个函数通常只会做两件事：

1. return value – 计算或找出某个值，并且从函数内回传出来。
2. side effect – 当函数做某事时，我们就说这个函数的功能是做 side effect。例如，函数从数据库读取或写入数据。

在 React 当中，一个 functional component 如果想要做 side effect，则可以使用 useEffect 这个 Hook。常见的 side effect 有： 向 API 去 fetch 数据、使用 setTimeout 等等的计时函数。

useEffect Hook 语法接收两个参数：

```jsx
useEffect(function, dependencies)
```

Dependencies 是一个 array of states：

1. 如果 dependencies 是一个 empty array，则在此 Component 第一次被渲染的时候，就会执行 useEffect 参数的 function 一次。
2. 如果 dependencies 是[name]，则在此 Component 第一次被渲染的时候，就会执行 useEffect 参数的 function 一次。每当 name 这个 state 被更新时，也会执行 useEffect 参数的 function 一次。

```jsx
import React, { useEffect, useState } from "react";

const App = () => {
  let [myName, setMyName] = useState("saltedfish");

  const buttonHandler = () => {
    setMyName("xiansakana");
  };

  useEffect(() => {
    console.log("useEffect内部的function正在被执行");
  }, [myName]);

  return (
    <div>
      <h1>{myName}</h1>
      <button onClick={buttonHandler}>改变名称</button>
    </div>
  );
};
```

# Class Component, Life Cycle

React 16 版本以前，Component 的制作方式只有一种，那就是使用 class component。 Class Component 内部自动带有 State 以及跟 Component 生命周期(Component Life Cycle)有关的函数。

在 React 16.8 出现 Hooks 之后，我们就不需要使用 class component 内的 state 以及生命周期的语法了。然而，现在被维护的 React 程式码中仍参杂许多 class component 的写法，所以认识 Class Component 对写 React 是百利而无一害。

class component 的语法为：

```jsx
class Car extends React.Component {
  render() {
    return <h2>我是一台车</h2>;
  }
```

render 函数可以定义此 Component 的 JSX 架构。
若要在 Class Component 内部初始化某些属性，则需要用到 constructor()：

```jsx
class Car extends React.Component {
  constructor() {
    super();
    this.state = { color: "绿色" };
  }

  render() {
    return <h2>我是一台{this.state.color}的车</h2>;
  }
}
```

当此 Class Component 第一次被渲染时，constructor 就会被 React 执行。

在 Class Component 当中使用 Props 的方式也很简单。先在标签设定属性

```jsx
const App = () => {
  return (
    <div>
      <Car brand="toyota" />
    </div>
  );
};
```

```jsx
class Car extends React.Component {
  constructor(props) {
    super();
    this.state = { color: "绿色" };
  }

  render() {
    return (
      <h2>
        我是一台{this.props.brand}
        {this.state.color}的车
      </h2>
    );
  }
}
```

在 Class Component 当中，如果要改变 state 属性的内容，必须要用 setState()函数：

```jsx
class Car extends React.Component {
  constructor(props) {
    super();
    this.state = { color: "绿色" };
    this.buttonHandler = this.buttonHandler.bind(this);
  }

  buttonHandler() {
    this.setState({ color: "白色" });
  }

  render() {
    return (
      <div>
        <h2>
          我是一台{this.props.brand}
          {this.state.color}的车
        </h2>
        <button onClick={this.buttonHandler}>改变颜色</button>
      </div>
    );
  }
}
```

React 中的每个 Component 都有一个生命周期(Life Cycle)，而我们可以在其三个主要阶段对其进行监控和操作。这三个与生命周期有关的函数(Life Cycle Methods)是：

1. componentDidMount() – 在一个 component 被 mount（加入 DOM tree 中）后，componentDidMount() 会马上被呼叫。
2. componentDidUpdate() – componentDidUpdate() 会在更新后马上被呼叫。这个方法并不会在初次 render 时被呼叫。
3. componentWillUnmount() – componentWillUnmount() 会在ㄧ个 component 即将被 unmount 时呼叫。

> 在 React 的 Development Mode 之下，<React.StrictMode>会让 componentDidMount 执行两次。
>
> 除了这三个 methods 之外，还有许多其他的 Life Cycle Methods，有兴趣再去认识。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311222151079.png)

根据 React 的文件，「如果你熟悉 React class 的生命周期方法，你可以把 useEffect 视为 componentDidMount，componentDidUpdate 和 componentWillUnmount 的组合。」

例如，在 useEffect 的第二个参数放入 empty array，即有 componentDidMount 的效果。在 useEffect 的第二个参数放入[state]，即有 componentDidMount 以及 componentDidUpdate 的效果。

关于 useEffect 如何跟三个生命周期函数互换，可参考 https://zh-hant.reactjs.org/docs/hooks-effect.html。

# React Router

因为 Create React App 并不自动包含 page routing 的功能，所以最有名的解决方案是使用 react-router-dom 这个 package。 React Router Dom 中，App.js 的语法是：

```jsx
// App.js
import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import Homepage from "./Homepage";
import About from "./About";
import Page404 from "./Page404";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Homepage />}></Route>
          <Route path="about" element={<About />}></Route>
          <Route path="*" element={<Page404 />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
```

`<Outlet />`标签会自动在`<Route element={Layout}>`下的其他`<Route>`标签内自动转换。

```jsx
// Layout.js
import React from "react";
import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">首页</Link>
          </li>
          <li>
            <Link to="/about">关于</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </div>
  );
};
export default Layout;
```

> 在 import Layout from "./Layout"; 时，vscode 报错：已包含的文件名 xxx 仅大小写与文件名 xxxx 不同。程序包含该文件是因为:通过 xxxxx 从文件 xxxxxxx 导入为编译指定的根文件 ts(1261)
>
> 产生原因：
> vscode 升级后，本地的 ts 版本和项目的 ts 版本不一致导致
>
> 解决方法：
> vscode 里面 按住 Ctrl + Shift + P ----> 选择 typescript 版本 ----> 选择使用工作区版本
>
> ![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311222236617.png)
