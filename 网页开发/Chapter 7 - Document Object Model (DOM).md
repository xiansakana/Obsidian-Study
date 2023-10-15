## Document Object Model ([DOM](https://developer.mozilla.org/zh-CN/docs/Glossary/DOM))

文件对象模型（Document Object Model, DOM) 是 HTML的程序介面。它提供了一个文件（树）的结构化表示法，并定义让程序可以存取并改变文件架构、风格和内容的方法。DOM 提供了文件以拥有属性与函式的节点与物件组成的结构化表示。节点也可以附加事件处理程序，一旦触发事件就会执行处理程序。 本质上，它将网页与脚本或程序语言连结在一起。

简单来说， DOM允许我们在 JavaScript 当中操作 HTML 元素。 （如果 JS 无法存取 DOM，那么它与其他程序语言相比没有什么区别。）

所谓的Document Object Model，顾名思义，可知HTML也被视为是个物件。这种架构被称之为是模型(Model)。我们知道：

1. document是一个object，是 window object的一个属性。
2. document是指 HTML document 。
3. 这个模型意味着所有document内部的 HTML 元素都是object。每个HTML标签都有其属性和方法。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310141449137.png)

在Document Object Model这颗树上的每个点被称之为节点(node)。节点分为三种：

1. HTML元素节点(称为element nodes or element objects)
2. 文字节点(text node)
3. 注解节点(comment node)

DOM提供2种节点集合：[HTMLCollection](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCollection) (element nodes) 以及[NodeList](https://developer.mozilla.org/zh-CN/docs/Web/API/NodeList) (所有三种nodes)。

### [Window Object](https://developer.mozilla.org/zh-CN/docs/Web/API/Window)

在 JavaScript 当中的window object代表目前程序码正在运行的电脑视窗 (通常就是指我们的浏览器视窗)。Window Object可使用的常见methods包含：

- [window.alert()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/alert): 在视窗显示对话框。
- [window.addEventListener()](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener): 将事件监听程序码附加到Window Object 。
- [window.clearInterval()](https://developer.mozilla.org/zh-CN/docs/Web/API/clearInterval): 将 setInterval() 所重复执行的程序暂停。
- [window.prompt()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/prompt): return 用户在提示对话框中输入的文字。
- [window.setInterval()](https://developer.mozilla.org/zh-CN/docs/Web/API/setInterval): 每次经过给定的毫秒数时安排一个函数执行。

(面向对象程序概念：一个Object可以是另一个Object的attribute。例如，人的配偶也是一个人。)
Window Object可使用的常见properties包含：

- [window.console](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/console): return一个console object。console object可以对浏览器的debugging console进行控制与访问。常用的methods为log(), error()。
- [window.document](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/document): return window包含的文档，也就是HTML文件。
- [window.localStorage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage): return一个local storage对象。
- [window.sessionStorage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/sessionStorage): return一个session storage对象。

### Document Object

Document Object常用的methods有：

- [window.document.addEventListener()](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener)
- [window.document.createElement(tagName)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createElementNS)
- [window.document.getElementById(id)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/getElementById): 第一个id相符合的element object。
- [window.document.getElementsByClassName(className)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/getElementsByClassName): return一个动态的HTMLCollection， 内部元素包含所有具有给定className的元素。
- [querySelector(selectors)](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelector): return 第一个符合特定选择器群组的element object。採用深度优先搜寻演算法。

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

HTMLCollection是动态的；Nodelist是静态的

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

### 差别比较

Element Object是三种节点的其中一种。每个节点(Node)有childNodes的属性。Return type为NodeList，内部包含此节点在DOM Tree之下第一层的所有节点的所有节点。

每个Element Object有children属性。 Return type为HTMLCollection，内部包含此节点在DOM Tree之下第一层的所有Element Object 。

因此，我们知道，Element objects这种node可以同时使用childNodes以及children属性，但其他两种node却只有能够使用childNodes属性。若其他两种node使用children属性，只会看到undefined。

| Methods                           | Return Type                                |
| --------------------------------- | ------------------------------------------ |
| getElementById(id)                | Element Object                             |
| getElementsByClassName(className) | HTMLCollection (内部元素为Element Objects) |
| querySelector(selector)           | Element Object                             |
| querySelectorAll(selector)        | NodeList (内部元素为Nodes)                 |

|            | NodeList                                                     | HTMLCollection                                               |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Feature    | Array-like, but not array. No push, pop, shift, unshift methods | Array-like, but not array. No push, pop, shift, unshift methods |
| Motion     | static                                                       | dynamic                                                      |
| Elements   | Nodes                                                        | Element Objects                                              |
| Attributes | length, index                                                | length, index                                                |
| forEach    | Allowed                                                      | Not allowed                                                  |

## Function Declaration and Expression

Function Express的用途主要在于：

1. 创建一个未命名的 Function，之后再把这个Function放置到其他的变数内部，让程式码更有弹性。

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

2. 当作higher order function的callback function使用。例如，forEach或是addEventListener。

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

> 1. 如果我们程序码中有许多callback function都是采用function declaration，命名变量时，都需要避开function declaration。
> 2. callback function名称意义其实没有意义
> 3. 程序码变干净

3. 使用IIFE(Immediately Invokied Function Expression)的功能。

```javascript
(function (a, b) {
  console.log(a + b);
})(10, 5);
```

## Arrow Function Expression

JavaScript 中的函数是first-class objects (一等对象)。所谓的function是first-class objects 是指，我们可以：

1. 将function分配给变量。例如，let hello = function() {…}; 
2. 将function当作argument传给其他function (等同于数学上的composite function) 。 Higher Order function的argument被称为callback function。

在许多情况下，若要把function当作argument传给其他function，那么对此函数命名则变得没有意义。因此，选用Function Expression会是个好的选项。JavaScript当中，Arrow Function Expression是Function Expression的简化语法。

Arrow Function Expression的语法为：

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

- param *=>* expression
  - param => expression
  - (param1, param2, ...) => expression

-  param *=>* {return expression}

```javascript
let addition = (a, b) => a + b;
console.log(addition(10, 20));
```

> 1. 若Arrow Function Expression只有一个parameter，则不需要加上括号（可加可不加）。
> 2. 若有零个或是两个以上的parameters，则一定要加上括号。
> 3. Arrow Function Expression的主体若不加上 curly brackets ，则return expression的值。
> 4. 若主体有多个计算式，则一定需要加上 curly brackets。
> 5. 若Arrow Function Expression有加上 curly brackets，则一定需要加return关键字才会回传一个值。
> 6. Arrow Function Expression没有 this关键字绑定，不应该用作Objects的methods。

## forEach() Method

forEach() 为每个阵列元素执行一次提供函数。 forEach()与arrow function协作的语法为：

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

若只放入一个callback function，语法则是：

- forEach(callbackFn)

```javascript
let myLuckyNumbers = [1, 2, 3, 4, 5, 6, 7];
myLuckyNumbers.forEach((n) => {
  console.log(n + 3);
});
```

> forEach()方法可以在NodeList中使用，但不能在HTMLCollection中使用。

```javascript
// NodeList
let hellos = document.querySelectorAll(".hello");
hellos.forEach((hello) => {
  console.log(hello);
});
```

## Element Objects

在DOM Tree当中，每个HTML 元素（可能）有自己独特的properties和methods。除了这些独特的属性之外，所有Element Objects都必须具有此列表中的属性和方法：

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

    **`add()`** 方法将给定的标记添加到列表中

    ```javascript
    let firstP = document.querySelector("p");
    firstP.classList.add("blue", "red");
    ```

  - [remove()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/remove)

    **`remove()`** 方法从 [`DOMTokenList`](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList) 中移除指定标记。

    ```javascript
    let firstP = document.querySelector("p");
    firstP.classList.add("blue", "red");
    firstP.classList.remove("red");
    ```

  - [toggle()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/toggle)

    接口的 **`toggle()`** 方法从列表中删除一个给定的标记并返回 `false`。如果标记不存在，则添加并且函数返回 `true`。

    ```javascript
    let firstP = document.querySelector("p");
    firstP.addEventListener("click", () => {
      firstP.classList.toggle("red");
    });
    ```

  - [contains()](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMTokenList/contains)

    **`contains()`** 方法返回 [`Boolean` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) 类型。若传入的参数 `token` 包含在列表中时则返回`true`，否则返回 `false`。

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
myH1.innerHTML = "<a>这是我的h1</a>"
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

- [style](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement/style): 可以用来改变element object的inline styling。因为JS 中不允许使用hyphen，因此， JS 中的 CSS 属性都被更改为 camelCase。

```javascript
let button = document.querySelector("button");
button.style = "background-color: green; color: white";
```

```javascript
let button = document.querySelector("button");
button.style.backgroundColor = "green";
button.style.color = "white";
```

## Inheritance 继承

在面向对象的程序语言当中，我们可以将attributes和methods从一个class继承到另一个class。用更简单的方式来说，从一个对象继承到另一个对象，这个过程称为inheritance。

1. subclass (子类) - 从另一个class继承的class。也被称作child class。
2. superclass (父类) - 继承自的class。也被称作parent class。

所有 HTML 元素都从“element object”继承attributes和methods。除了继承来的属性与方法，其中某些HTML 元素有自己独特的attributes和methods 。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310142145792.png)

```javascript
let button = document.querySelector("button");
button.addEventListener("click", () => {
  let form = document.querySelector("form");
  form.reset();
});
```

## JavaScript Events

addEventListener() 可以让我们在window object, document object以及element object上面挂一个事件监听器(Event Listener)。事件监听器会不断的等待特定事件的发生。当有特定事件发生时，事件监听器就会执行所被赋予的function。

addEventListener(type, listener);

type是指事件的类型。例如，一个button可以挂著click这种事件的事件监听器、window object可以挂著resize这种事件的事件监听器。
listener通常为一个一般的function，或更常见的是一个arrow function expression。当事件发生在HTML element上面时，JavaScript会自动执行listener这个callback function。Callback function被执行时， JavaScript会在把event object当作argument，放进listener内部去执行函式。

### JavaScript Events Objects

JavaScript Events Objects的继承关系如下：

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310142155137.png)

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

- [stopPropagation()](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation): 可防止在event bubbling进一步传播当前事件。

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

### Event Bubbling

Event Bubbling的概念是指，当一个事件发生在一个元素上时，它首先在其上运行event handler ，然后运行其parent element的event handler ，然后一直往上运行其他祖先的event handler 。

之所以称作Event Bubbling是因为，这个过程被称为就像冒泡一样，事件像水中的气泡从内部元素向上通过parent element往上走。

## [Local Storage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage) and [Session Storage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/sessionStorage)

Storage是在浏览器中一个存储数据的地方(这个地方并不是数据库)。在Storage内部储存的数值都是key-value pair，且不论是key还是value，资料型态都必须是String。如果我们将要储存在Storage的资料不是String，那麽资料会先被强制转换为String ，再被储存到Storage内部。

sessionStorage 跟 localStorage 很相似：唯一不同的地方是存放在 localStorage 的资料并没有过期的时效。即使把浏览器关了，电脑也关机， localStorage的资料仍然在浏览器内。另一方面，一旦用户关闭浏览器， sessionStorage就会被销毁。

Local Storage 以及 Session Storage所使用的methods都是一模一样的：

- [setItem(key, value)](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/setItem): 当传递一个key和value时，会将该key-value pair添加到给定的 Storage，或者如果该key的值已经存在于，则更新该key的value。

```javascript
localStorage.setItem("name", "Wilson");
```

- [getItem(key)](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/getItem): 从给定的 Storage 中返回该key的value值。如果该key不存在，则返回 null。

```javascript
localStorage.setItem("name", "Wilson");
localStorage.setItem("age", 26);
let myName = localStorage.getItem("name");
let myAge = localStorage.getItem("age");
console.log(myName);
console.log(typeof myAge);
```

- [removeItem(key)](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/removeItem): 从给定的 Storage 中删除该key-value pair（如果key-value pair 存在的话）。

```javascript
localStorage.removeItem("name");
```

- [clear()](https://developer.mozilla.org/zh-CN/docs/Web/API/Storage/clear): 清除存储在给定 Storage 中的所有key-value pair。

```javascript
localStorage.clear();
```

由于 Storage 只能储存 String，我们若想要把object, array等等资料类型存放在 Storage 内部，需要用到JSON Object。 JSON 代表 JavaScript Object Notation，是一种资料交换格式 。

JSON Object有两个method：

- [JSON.stringify(value)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify): 将value转换为 JSON String。
- [JSON.parse(text)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse): 解析 JSON String，制作出JSON String描述的 JavaScript 值或Object。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310150044472.png)



