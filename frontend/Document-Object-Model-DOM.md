# Document-Object-Model-DOM

---

title: Document Object Model (DOM)
tags:

- JavaScript
- 前端
- DOM
  categories: 前端
  cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311010813961.png
  abbrlink: 5fb72f5f
  date: 2023-11-01 05:15:52

---

# Document Object Model ([DOM](https://developer.mozilla.org/zh-CN/docs/Glossary/DOM))

文件对象模型（Document Object Model, DOM) 是 HTML 的程序介面。它提供了一个文件（树）的结构化表示法，并定义让程序可以存取并改变文件架构、风格和内容的方法。DOM 提供了文件以拥有属性与函式的节点与物件组成的结构化表示。节点也可以附加事件处理程序，一旦触发事件就会执行处理程序。 本质上，它将网页与脚本或程序语言连结在一起。

简单来说， DOM 允许我们在 JavaScript 当中操作 HTML 元素。 （如果 JS 无法存取 DOM，那么它与其他程序语言相比没有什么区别。）

所谓的 Document Object Model，顾名思义，可知 HTML 也被视为是个物件。这种架构被称之为是模型(Model)。我们知道：

1. document 是一个 object，是 window object 的一个属性。
2. document 是指 HTML document 。
3. 这个模型意味着所有 document 内部的 HTML 元素都是 object。每个 HTML 标签都有其属性和方法。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182251952.png)

在 Document Object Model 这颗树上的每个点被称之为节点(node)。节点分为三种：

1. HTML 元素节点(称为 element nodes or element objects)
2. 文字节点(text node)
3. 注解节点(comment node)

DOM 提供 2 种节点集合：[HTMLCollection](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCollection) (element nodes) 以及[NodeList](https://developer.mozilla.org/zh-CN/docs/Web/API/NodeList) (所有三种 nodes)。

## [Window Object](https://developer.mozilla.org/zh-CN/docs/Web/API/Window)

在 JavaScript 当中的 window object 代表目前程序码正在运行的电脑视窗 (通常就是指我们的浏览器视窗)。Window Object 可使用的常见 methods 包含：

- [window.alert()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/alert): 在视窗显示对话框。
- [window.addEventListener()](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener): 将事件监听程序码附加到 Window Object 。
- [window.clearInterval()](https://developer.mozilla.org/zh-CN/docs/Web/API/clearInterval): 将 setInterval() 所重复执行的程序暂停。
- [window.prompt()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/prompt): return 用户在提示对话框中输入的文字。
- [window.setInterval()](https://developer.mozilla.org/zh-CN/docs/Web/API/setInterval): 每次经过给定的毫秒数时安排一个函数执行。

(面向对象程序概念：一个 Object 可以是另一个 Object 的 attribute。例如，人的配偶也是一个人。)
Window Object 可使用的常见 properties 包含：

- [window.console](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/console): return 一个 console object。console object 可以对浏览器的 debugging console 进行控制与访问。常用的 methods 为 log(), error()。
- [window.document](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/document): return window 包含的文档，也就是 HTML 文件。
- [window.localStorage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage): return 一个 local storage 对象。
- [window.sessionStorage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/sessionStorage): return 一个 session storage 对象。

## Document Object

Document Object 常用的 methods 有：

- [window.document.addEventListener()](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener)
- [window.document.createElement(tagName)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createElementNS)
- [window.document.getElementById(id)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/getElementById): 第一个 id 相符合的 element object。
- [window.document.getElementsByClassName(className)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/getElementsByClassName): return 一个动态的 HTMLCollection， 内部元素包含所有具有给定 className 的元素。
- [querySelector(selectors)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelector): return 第一个符合特定选择器群组的 element object。採用深度优先搜寻演算法。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <p class="my-p"></p>
    <script src="add.js"></script>
  </body>
</html>
```

```javascript
let first_found = document.querySelector(".my-p");
console.log(first_found);
```

- [querySelectorAll(selectors)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelectorAll): return 一个静态（not live）NodeList，表示与指定选择器组匹配的元素列表。

```javascript
let found_elements = document.querySelectorAll(".my-p");
console.log(found_elements);
```

> HTMLCollection 和 Nodelist 是 array-like Object

HTMLCollection 是动态的；Nodelist 是静态的

```javascript
// HTMLCollection 动态 Dynamic
// Nodelist 静态 Static

let hellos = document.getElementsByClassName("hello");
let helloss = document.querySelectorAll(".hello");
console.log(hellos.length);
console.log(helloss.length);

let body = document.querySelector("body");
let p = document.createElement("p");
p.innerText = "this is a new p";
p.classList.add("hello");
body.appendChild(p);

console.log("改变DOM之后");
// helloss = document.querySelectorAll(".hello");
console.log(hellos.length); // 3
console.log(helloss.length); // 2
```

## 差别比较

Element Object 是三种节点的其中一种。每个节点(Node)有 childNodes 的属性。Return type 为 NodeList，内部包含此节点在 DOM Tree 之下第一层的所有节点的所有节点。

每个 Element Object 有 children 属性。 Return type 为 HTMLCollection，内部包含此节点在 DOM Tree 之下第一层的所有 Element Object 。

因此，我们知道，Element objects 这种 node 可以同时使用 childNodes 以及 children 属性，但其他两种 node 却只有能够使用 childNodes 属性。若其他两种 node 使用 children 属性，只会看到 undefined。

|Methods|Return Type|
| ---------------------------------| -------------------------------------------|
|getElementById(id)|Element Object|
|getElementsByClassName(className)|HTMLCollection (内部元素为 Element Objects)|
|querySelector(selector)|Element Object|
|querySelectorAll(selector)|NodeList (内部元素为 Nodes)|

||NodeList|HTMLCollection|
| ----------| ---------------------------------------------------------------| ---------------------------------------------------------------|
|Feature|Array-like, but not array. No push, pop, shift, unshift methods|Array-like, but not array. No push, pop, shift, unshift methods|
|Motion|static|dynamic|
|Elements|Nodes|Element Objects|
|Attributes|length, index|length, index|
|forEach|Allowed|Not allowed|

# Function Declaration and Expression

Function Express 的用途主要在于：

1. 创建一个未命名的 Function，之后再把这个 Function 放置到其他的变数内部，让程式码更有弹性。

```javascript
let addition = function (a, b) {
  return a + b;
};
console.log(addition(10, 5));
```

```javascript
let Wilson = {
  name: "Wilson",
  greet() {
    console.log(this.name + "打招呼");
  },
  walk: function () {
    console.log(this.name + "正在走路");
  },
};

Wilson.greet();
Wilson.walk();

// Output:
// Wilson打招呼
// Wilson正在走路
```

2. 当作 higher order function 的 callback function 使用。例如，forEach 或是 addEventListener。

```javascript
function react() {
  alert("有人正在点击画面");
}
// addEventListener本身是一个higher order function
// react是一个callback function
window.addEventListener("click", react);
```

以上程序还可以这样写

```javascript
window.addEventListener("click", function () {
  alert("有人正在点击画面");
});
```

> 1. 如果我们程序码中有许多 callback function 都是采用 function declaration，命名变量时，都需要避开 function declaration。
> 2. callback function 名称意义其实没有意义
> 3. 程序码变干净

3. 使用 IIFE(Immediately Invokied Function Expression)的功能。

```javascript
(function (a, b) {
  console.log(a + b);
})(10, 5);
```

# Arrow Function Expression

JavaScript 中的函数是 first-class objects (一等对象)。所谓的 function 是 first-class objects 是指，我们可以：

1. 将 function 分配给变量。例如，let hello = function() {…};
2. 将 function 当作 argument 传给其他 function (等同于数学上的 composite function) 。 Higher Order function 的 argument 被称为 callback function。

在许多情况下，若要把 function 当作 argument 传给其他 function，那么对此函数命名则变得没有意义。因此，选用 Function Expression 会是个好的选项。JavaScript 当中，Arrow Function Expression 是 Function Expression 的简化语法。

Arrow Function Expression 的语法为：

- () => expression

```javascript
let hello = () => {
  console.log("hello wolrd");
};
hello();
```

```javascript
window.addEventListener("click", () => {
  alert("有人正在点击画面");
});
```

```javascript
let Wilson = {
  name: "Wilson",
  walk1() {
    console.log(this.name + " is walking");
  },
  walk2: function () {
    console.log(this.name + " is walking");
  },
  // arrow function expression没有this keyword绑定
  walk3: () => {
    console.log("Wilson is walking");
  },
};
Wilson.walk1();
Wilson.walk2();
Wilson.walk3();
```

- param  *=&gt;*  expression

  - param => expression
  - (param1, param2, ...) => expression
- param  *=&gt;*  {return expression}

```javascript
let addition = (a, b) => a + b;
console.log(addition(10, 20));
```

> 1. 若 Arrow Function Expression 只有一个 parameter，则不需要加上括号（可加可不加）。
> 2. 若有零个或是两个以上的 parameters，则一定要加上括号。
> 3. Arrow Function Expression 的主体若不加上 curly brackets ，则 return expression 的值。
> 4. 若主体有多个计算式，则一定需要加上 curly brackets。
> 5. 若 Arrow Function Expression 有加上 curly brackets，则一定需要加 return 关键字才会回传一个值。
> 6. Arrow Function Expression 没有 this 关键字绑定，不应该用作 Objects 的 methods。

# forEach() Method

forEach() 为每个阵列元素执行一次提供函数。 forEach()与 arrow function 协作的语法为：

- forEach(element => …)

```javascript
let myLuckyNumbers = [1, 2, 3, 4, 5, 6, 7];
myLuckyNumbers.forEach((n) => {
  console.log(n + 3);
});
```

- forEach((element, index) => …)

```javascript
let myLuckyNumbers = [1, 2, 3, 4, 5, 6, 7];
myLuckyNumbers.forEach((n, index) => {
  console.log(n + " is at index " + index);
});
```

若只放入一个 callback function，语法则是：

- forEach(callbackFn)

```javascript
let myLuckyNumbers = [1, 2, 3, 4, 5, 6, 7];
myLuckyNumbers.forEach((n) => {
  console.log(n + 3);
});
```

> forEach()方法可以在 NodeList 中使用，但不能在 HTMLCollection 中使用。

```javascript
// NodeList
let hellos = document.querySelectorAll(".hello");
hellos.forEach((hello) => {
  console.log(hello);
});
```

# Element Objects

在 DOM Tree 当中，每个 HTML 元素（可能）有自己独特的 properties 和 methods。除了这些独特的属性之外，所有 Element Objects 都必须具有此列表中的属性和方法：

- [addEventListener(event, callbackFn)](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener)

```javascript
let myButton = document.querySelector("#my-btn");
myButton.addEventListener("click", () => {
  alert("你点击了button");
});
```

- [appendChild(element)](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/appendChild)

```javascript
let body = document.querySelector("body");
let myH1 = document.createElement("h1");
body.appendChild(myH1);
```

- [children](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/children)

```javascript
let body = document.querySelector("body");
// body.children is a HTMLCollection
console.log(body.children[0].children[0]);
```

- [childNodes](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/childNodes)
- [parentElement](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/parentElement)

```javascript
let firstP = document.querySelector("p");
console.log(firstP.parentElement.parentElement);
```

- [classList](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/classList)

  ```javascript
  let firstP = document.querySelector("p");
  console.log(firstP.classList);
  ```

  - [add()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/add)

    **​`add()`​**  方法将给定的标记添加到列表中

    ```javascript
    let firstP = document.querySelector("p");
    firstP.classList.add("blue", "red");
    ```
  - [remove()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/remove)

    **​`remove()`​**  方法从 [`DOMTokenList`](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList) 中移除指定标记。

    ```javascript
    let firstP = document.querySelector("p");
    firstP.classList.add("blue", "red");
    firstP.classList.remove("red");
    ```
  - [toggle()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/toggle)

    接口的 **​`toggle()`​**  方法从列表中删除一个给定的标记并返回 `false`。如果标记不存在，则添加并且函数返回 `true`。

    ```javascript
    let firstP = document.querySelector("p");
    firstP.addEventListener("click", () => {
      firstP.classList.toggle("red");
    });
    ```
  - [contains()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/contains)

    **​`contains()`​**  方法返回 [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)​[ (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) 类型。若传入的参数 `token` 包含在列表中时则返回`true`，否则返回 `false`。

    ```javascript
    let firstP = document.querySelector("p");
    console.log(firstP.classList.contains("green"));
    ```
- [getAttribute(attributeName)](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/getAttribute)

```javascript
let a = document.querySelector("a");
console.log(a.getAttribute("href"));
```

- [innerHTML](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/innerHTML)

```javascript
myH1.innerHTML = "<a>这是我的h1</a>";
```

- [innerText](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement/innerText)

```javascript
myH1.innerText = "这是我的h1";
```

- [querySelector(selector)](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/querySelector)
- [querySelectorAll(selector)](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/querySelectorAll)
- [remove()](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/remove)

```javascript
let button = document.querySelector("button");
button.addEventListener("click", () => {
  let a = document.querySelector("a");
  a.remove();
});
```

- [style](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement/style): 可以用来改变 element object 的 inline styling。因为 JS 中不允许使用 hyphen，因此， JS 中的 CSS 属性都被更改为 camelCase。

```javascript
let button = document.querySelector("button");
button.style = "background-color: green; color: white";
```

```javascript
let button = document.querySelector("button");
button.style.backgroundColor = "green";
button.style.color = "white";
```

# Inheritance 继承

在面向对象的程序语言当中，我们可以将 attributes 和 methods 从一个 class 继承到另一个 class。用更简单的方式来说，从一个对象继承到另一个对象，这个过程称为 inheritance。

1. subclass (子类) - 从另一个 class 继承的 class。也被称作 child class。
2. superclass (父类) - 继承自的 class。也被称作 parent class。

所有 HTML 元素都从“element object”继承 attributes 和 methods。除了继承来的属性与方法，其中某些 HTML 元素有自己独特的 attributes 和 methods 。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182252836.png)

```javascript
let button = document.querySelector("button");
button.addEventListener("click", () => {
  let form = document.querySelector("form");
  form.reset();
});
```

# JavaScript Events

addEventListener() 可以让我们在 window object, document object 以及 element object 上面挂一个事件监听器(Event Listener)。事件监听器会不断的等待特定事件的发生。当有特定事件发生时，事件监听器就会执行所被赋予的 function。

addEventListener(type, listener);

type 是指事件的类型。例如，一个 button 可以挂著 click 这种事件的事件监听器、window object 可以挂著 resize 这种事件的事件监听器。
listener 通常为一个一般的 function，或更常见的是一个 arrow function expression。当事件发生在 HTML element 上面时，JavaScript 会自动执行 listener 这个 callback function。Callback function 被执行时， JavaScript 会在把 event object 当作 argument，放进 listener 内部去执行函式。

## JavaScript Events Objects

JavaScript Events Objects 的继承关系如下：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182252783.png)

所有的 Events Objects 中，最常用到的几个属性与方法是：

- [target](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/target): 指向最初触发事件的 DOM 物件。

```javascript
let button = document.querySelector("button");
button.addEventListener("click", (e) => {
  console.log(e.target);
});
```

- [preventDefault()](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/preventDefault): 如果事件可以被取消，就取消事件（即取消事件的预设行为）。但不会影响事件的传递，事件仍会继续传递。

```javascript
let form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault;
});
```

- [stopPropagation()](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation): 可防止在 event bubbling 进一步传播当前事件。

```html
<style>
  .a {
    width: 300px;
    height: 300px;
    background-color: red;
  }
  .b {
    width: 150px;
    height: 150px;
    background-color: blue;
  }
</style>
<div class="a">
  <div class="b"></div>
</div>
```

```javascript
let a = document.querySelector(".a");
let b = document.querySelector(".b");

a.addEventListener("click", () => {
  alert("红色框的时间监听器正在被执行");
});
b.addEventListener("click", (e) => {
  e.stopPropagation();
  alert("蓝色框的时间监听器正在被执行");
});
```

## Event Bubbling

Event Bubbling 的概念是指，当一个事件发生在一个元素上时，它首先在其上运行 event handler ，然后运行其 parent element 的 event handler ，然后一直往上运行其他祖先的 event handler 。

之所以称作 Event Bubbling 是因为，这个过程被称为就像冒泡一样，事件像水中的气泡从内部元素向上通过 parent element 往上走。

# [Local Storage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage) and [Session Storage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/sessionStorage)

Storage 是在浏览器中一个存储数据的地方(这个地方并不是数据库)。在 Storage 内部储存的数值都是 key-value pair，且不论是 key 还是 value，资料型态都必须是 String。如果我们将要储存在 Storage 的资料不是 String，那麽资料会先被强制转换为 String ，再被储存到 Storage 内部。

sessionStorage 跟 localStorage 很相似：唯一不同的地方是存放在 localStorage 的资料并没有过期的时效。即使把浏览器关了，电脑也关机， localStorage 的资料仍然在浏览器内。另一方面，一旦用户关闭浏览器， sessionStorage 就会被销毁。

Local Storage 以及 Session Storage 所使用的 methods 都是一模一样的：

- [setItem(key, value)](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/setItem): 当传递一个 key 和 value 时，会将该 key-value pair 添加到给定的 Storage，或者如果该 key 的值已经存在于，则更新该 key 的 value。

```javascript
localStorage.setItem("name", "Wilson");
```

- [getItem(key)](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/getItem): 从给定的 Storage 中返回该 key 的 value 值。如果该 key 不存在，则返回 null。

```javascript
localStorage.setItem("name", "Wilson");
localStorage.setItem("age", 26);
let myName = localStorage.getItem("name");
let myAge = localStorage.getItem("age");
console.log(myName);
console.log(typeof myAge);
```

- [removeItem(key)](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/removeItem): 从给定的 Storage 中删除该 key-value pair（如果 key-value pair 存在的话）。

```javascript
localStorage.removeItem("name");
```

- [clear()](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/clear): 清除存储在给定 Storage 中的所有 key-value pair。

```javascript
localStorage.clear();
```

由于 Storage 只能储存 String，我们若想要把 object, array 等等资料类型存放在 Storage 内部，需要用到 JSON Object。 JSON 代表 JavaScript Object Notation，是一种资料交换格式 。

JSON Object 有两个 method：

- [JSON.stringify(value)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify): 将 value 转换为 JSON String。
- [JSON.parse(text)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse): 解析 JSON String，制作出 JSON String 描述的 JavaScript 值或 Object。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182252739.png)

```javascript
let myLuckyNumbers = [1, 2, 3, 4, 5, 6];
localStorage.setItem("myNumbers", JSON.stringify(myLuckyNumbers));

let myArr = JSON.parse(localStorage.getItem("myNumbers"));
myArr.forEach((n) => {
  console.log(n);
});
```
