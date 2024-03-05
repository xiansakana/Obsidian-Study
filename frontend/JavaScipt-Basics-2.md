---
title: JavaScipt Basics 2
tags:
  - JavaScript
  - 前端
categories: 学习
cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310240401759.png'
abbrlink: ef214ab0
date: 2023-10-24 03:56:41
---

# Function 函数

declare function:

```javascript
function name([param]) {
  statemets;
}
```

> JavaScript Function 中，若没有 return 语句的话，function 将返回 undefined（这是 JavaScript 的 function 默认的 return value）。要返回默认值以外的值，函数必须具有指定要返回的值的 return 语句。return 语句结束函式执行并指定要返回给函数调用者的值。任何放在 return 语句底下的程式码都不会被执行。
>
> 每个 JavaScript 函数实际上都是一个对象。（代表每个 function 有 instance properties 以及 instance methods）

# Array

Array 具有以下核心特征：

- JavaScript Array 是可调整大小的，并且可以包含不同资料类型的混合。

- JavaScript Array 中的元素必须使用非负整数作为 index 来访问。

- JavaScript Array 的第一个元素在 index 0 处，第二个在 index 1 处，依此类推。最后一个元素在 Array 的长度减 1 处。

- JavaScript Array 复制会复制 reference。

  > ```javascript
  > let arr1 = [1, 2, 3];
  > let arr2 = arr1;
  > console.log(arr1 == arr2);
  > //return true
  >
  > let arr3 = [1, 2, 3];
  > let arr4 = [1, 2, 3];
  > console.log(arr3 == arr4);
  > //return false
  > ```

Array Instance Properties：[length](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/length)

常见的 Array Instance Methods：

- [push(element)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/push) - 将一个或多个元素添加到数组的末尾，并 return 数组的新长度。
- [pop()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) - 从数组中删除最后一个元素并返回该元素。
- [shift()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/shift) - 从数组中删除第一个元素并返回删除的元素。
- [unshift(element)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) - 将一个或多个元素添加到数组的开头，并 return 数组的新长度。

> 当 Array 内部的元素还有 Array 时，就被称为是 array of arrays。

# [Object](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object)

每个 JavaScript 对象都有 properties 以及 method。属于对象的 function 被称为 method。 对象的属性与相对应的值是一种 key-value pair。获取对象属性的方式可以透过 dot notation 或是 []。JavaScript Object 是一种 hashtable。在 method 中的 this 关键字指的是调用该方法的对象。若某个 function 没有调用该 function 的对象，则 this 关键字则是指向 window 对象。

```javascript
let person = {
  // properties (key-value pair), methods
  first_name: "Wilson",
  last_name: "Ren",
  age: 26,
  is_married: true,
  spouse: "Grace",

  sayHi() {
    console.log("Wilson say hi.");
  },

  walk() {
    console.log(this.first_name + " is walking...");
  },
};

console.log(person.age);
console.log(person["spouse"]);
person.sayHi();
person.walk();
```

在 JavaScript 当中的 function、array 其实都是对象(Object)。Array 以及 Function 都是 special type of objects。

> 判断 array data type: [Array.isArray()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)
>
> ```javascript
> let arr = [1, 2, 3, 4, 5];
> console.log(Array.isArray(arr));
> // reture true
> ```

# Loop

## [For Loop](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for)

```javascript
for (let i = 0; i < 11; i++) {
  console.log(i);
}
```

## [While Loop](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/while)

```javascript
let i = 0;
while (i < 10) {
  console.log("i");
  i++;
}
```

## [Do while Loop](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/do...while)

```javascript
let j = 0;
do {
  console.log(j);
  i++;
} while (j < 10);
```

## Nested Loop

```javascript
let counter = 0;
for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 500; j++) {
    counter++;
  }
}
console.log(counter);
```

# [Break](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/break)、[Continue](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/continue)

Break 用于终止存在它的循环。如果 break 语句存在于 nested loop 中，它只会终止那些包含 break 语句的 loop 。若要终止 nested loop，则需要使用 return 关键字。

```javascript
for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 500; j++) {
    console.log(j);
    if (j == 3) {
      break;
    }
  }
}
```

Continue 与 break 语句相反； 它不是终止循环，而是强制执行循环的下一次迭代。在 loop 中执行 continue 语句时，将跳过 continue 语句之后的循环内的代码，开始循环的下一次迭代。

```javascript
for (let i = 0; i < 10; i++) {
  if (i == 3) {
    continue;
  }
  console.log(i);
}
```

> for loop 跑 Array
>
> ```javascript
> let arr = ["Mike", "Grace", "Jason", "Jared"];
>
> for (let i = 0; i < arr.length; i++) {
>   console.log(arr[i] + " is my friend");
> }
> ```

# Math Object

- Math 是一个 JavaScript 内建对象，它具有数学常数和函数的属性和方法。(若你有学过 Java， 则可以参考以下说明。Math Class 没有 constructor。 Math Class 的所有 attributes 和 methods 都是 static 的。 常数 𝜋 称为 Math.PI，将正弦函数称为 Math.sin(x)，其中 x 是参数。)
- Math Object 中，常用的 static properties 包含：Math.PI, Math.E。
- 常用的 static methods 包含：[Math.pow(x, y)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/pow), [Math.random()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random), [Math.sqrt(x)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/sqrt), [Math.abs()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/abs), [Math.floor()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)、[Math.ceil()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil)。
