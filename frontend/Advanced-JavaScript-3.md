---
title: Advanced JavaScript 3
tags:
  - JavaScript
  - 前端
cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311120954810.jpg'
categories: 学习
abbrlink: 894eaa28
date: 2023-11-12 09:42:25
---

## Ternary Operator

Ternary Operator 是 JavaScript 唯一用到三个运算元的运算子。在一个条件后面会跟著一个问号 (?)，如果条件是 truthy，在冒号(:)前的表达式会被执行，如果条件是 falsy，在冒号后面的表达式会被执行，这个运算子常常被用来当作 if 的简洁写法。 Ternary Operator 的语法为：
condition ? expressionIfTrue : expressionIfFalse

```javascript
let age = 15;
let price = age < 18 ? 50 : 150;
console.log(price);
// 50
```

## Default Parameters

当调用了 function 但没有给定足够数量的 arguments 时，parameter 会被设定成 undefined。 在 function 设定 Default Parameters 可以让 functions 有预设的初始化值。

```javascript
function multiply(a = 1, b = 1) {
  console.log(a, b);
  return a * b;
}
console.log(multiply(5));
// 5 1
// 5
```

## Backtick

```javascript
// backtick
let age = 23;
let address = "New York";
let myyName = `saltedfish的年龄是${age}且来自${address}。`;
console.log(myyName);
// saltedfish的年龄是23且来自New York
```

## Strong Typing and Weak Typing

强弱型别（Strong and weak typing）表示在电脑科学以及程式设计中，经常把程式语言的型别系统分为 strongly typed 和 weakly typed 两种。这两个术语并没有非常明确的定义，但主要用以描述程式语言对于混入不同资料型别的值进行运算时的处理方式。

大致上来说， Strong typing 意味著值的数据类型在有需要时，是必须要被强制改成正确的类别。JavaScript 被认为是个 “weakly typed” or “untyped” 的程式语言。

## Dynamic Typed and Static Typed

Static Typed 语言通常是指，编译器(compiler)会在编译时检查数据类型，而 Dynamic Typed 语言是指运行时才会检查。例如，在 Java 中，声明变量时，若赋值与变量类型不同，则无法编译。在修复问题之前，我们无法运行程式码。 主要优点是编译器可以完成各种检查，因此在很早的阶段就发现了很多琐碎的错误。

Static Typed 语言通常执行得更快，因为当编译器知道正在使用的确切数据类型时，它可以生成优化的机器代码（machine code）来运行程式。也因为程式码的运行不需要一边运行程式码，一边做类型检查，所以 Static Typed 语言使用更少的记忆体。

JavaScript 是个 dynamic typed 语言。

## [IIFE](https://developer.mozilla.org/zh-CN/docs/Glossary/IIFE)

IIFE（ Immediately Invoked Function Expression ）是一个 JavaScript 函数，它在定义后立即运行。 IIFE 的语法为：

```javascript
(function () {
  // …
})();
```

当我们在想要避免污染 global naming space，或是想要立即执行某个匿名 function 时(例如在伺服器的程式码内部)，就可以使用 IIFE。

## Destructuring Assignment

Destructuring Assignment 是一种 JavaScript 语法，它可以将 array 中的值或 object 中的属性 unpack 到不同的变量中。常见的语法为：

```javascript
const [a, b] = array;
const [a, b, ...rest] = array;
const { a, b } = obj;
```

在伺服器的程式码中，常常可以看到 Destructuring Assignment 的语法。

## [Switch Statement](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/switch)

Switch Statement 是 if statement 的另一种选项。两者的功能性完全相同，但对于有非常多 else if 的 if statement 来说，改写成 Switch Statement 可增加程式码的可阅读性（某些人这样认为，看个人习惯与感觉）。

Switch Statement 会先获得一个 expression，再将 expression 拿去跟一系列的 case 做比对。

在 Switch Statement 中， 如果省略 break，则将继续执行下一个 case ，甚至执行到 default 子句，而不管该 case 的值是否匹配。这种情形被称为“fall-through”。

```javascript
let day = prompt("今天星期几？");

switch (day) {
  case "星期一":
    alert("Today is Monday!");
    break;
  case "星期二":
    alert("Today is Tuesday!");
    break;
  case "星期三":
    alert("Today is Wednesday!");
    break;
  case "星期四":
    alert("Today is Thursday!");
    break;
  case "星期五":
    alert("Today is Friday!");
    break;
  case "星期六":
    alert("Today is Saturday!");
    break;
  case "星期日":
    alert("Today is Sunday!");
    break;
  default:
    alert("Cannot determine your day!");
}
```

## 错误处理

在 JavaScript 当中，如果要执行一段可能会出错的程式码，则可以将程式码放入 try…catch…语句当中。try… catch… 语句常在后端脚本中使用。语法为:

```javascript
try {
  tryStatements;
} catch (exceptionVar) {
  catchStatements;
} finally {
  finallyStatements;
}
```

- tryStatements – 要执行的语句。
- catchStatements –如果在 try 中引发异常，则执行的语句。
- exceptionVar (optional) – 一个变量，用于保存 catch 当中已捕获的错误。
- finallyStatements – 在完成 try...catch...语句时，一定会执行的语句。无论是否发生异常， finallyStatements 都会执行。

可使用的语法为:

- try...catch…
- try...finally…
- try...catch...finally…

```javascript
try {
  whatever();
} catch (e) {
  if (e instanceof TypeError) {
    console.log("发生typeError");
  } else if (e instanceof ReferenceError) {
    console.log("发生SyntaxError");
  } else {
    console.log("发生其他类型的Error");
  }
} finally {
  console.log("不管有无错误，都会被执行的");
}
```

```javascript
class NotArrayError extends TypeError {
  constructor(message) {
    super(message);
  }
}

function sumArray(arr) {
  if (!Array.isArray(arr)) {
    throw new TypeError("参数并非array!");
  }
  let result = 0;
  arr.forEach((element) => {
    result += element;
  });
  return result;
}

try {
  sumArray("hello");
} catch (e) {
  console.log(e);
}
```
