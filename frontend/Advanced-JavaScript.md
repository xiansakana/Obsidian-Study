---
title: Advanced JavaScript
tags:
  - JavaScript
  - 前端
categories: 学习
cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202309232138720.png'
abbrlink: 365c67ca
date: 2023-11-06 15:13:34
---

# JavaScript 引擎

JavaScript 并不是由任何程式语言所写成。它只是一个由欧洲电脑制造协会(ECMA)所订的标准。浏览器内部的 JavaScript 引擎会负责遵从 ECMA 所订的标准，理解与处理 JavaScript 程式码，让 JavaScript 程式码可以运作。

JavaScript 最有名的标准更新在 2015 年，被称为 ECMA2015 或是 ES6。

# [NaN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/NaN), [Infinity](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Infinity)

在 JavaScript 的数字当中，两个最特别的分别是 NaN 以及 Infinity。两者的数据类型都是 number。

NaN 属性表示 Not-A-Number 的值。当我们尝试使用 String 或其他数据类型进行一些数学计算时，若无法计数值，就会出现 NaN。

Infinity 值（正无穷大）值大于其他任何数值。 负无穷大则是-Infinity。任何乘以 Infinity 的正整数都是 Infinity，除以 Infinity 的任何数都是 0。

# [Spread Syntax](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Spread_syntax) and [Rest Parameters](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/rest_parameters)

Spread Syntax 允许在需要零个或多个参数（例如，function invocation）或元素（例如，array 的内部元素 ）的地方，去扩展 array 内部的元素。Spread Syntax 的语法为：

```javascript
myFunction(a, ...iterableObj, b)
[1, ...iterableObj, '4', 'five', 6]
```

```javascript
const parts = ["肩膀", "膝盖"];
const otherParts = ["头", ...parts, "身体", "脚"];
console.log(otherParts);
```

```javascript
// 复制array
const arr = [1, 2, 3];
const arr2 = [...arr];
arr2.push(4);
console.log(arr);
console.log(arr2);
```

```javascript
// 连接array
let arr = [1, 2, 3];
let arr2 = [4, 5, 6];
console.log([...arr, ...arr2]);
```

```javascript
function sum(a, b, c, d, e) {
  return a + b + c + d + e;
}
let arr = [1, 2, 3];
console.log(sum(10, ...arr, 5));
```

Spread Syntax 以及 Rest Parameters 的语法几乎一模一样。然而， Spread Syntax 是扩展 array 中的元素，而 Rest Parameters 是收集多个元素并将它们“压缩”为单个 JS array。Rest Parameters 的语法为：

```javascript
function f(a, b, ...theArgs) {
  // …
}
```

```javascript
function sum(...theArgs) {
  let total = 0;
  for (let i = 0; 0 < theArgs.length; i++) {
    total += theArgs[i];
  }
  return total;
}
console.log(sum(1, 2, 3, 4, 5, 6));
```

# Primitive, Reference Data Types

在 JavaScript 的 Primitive Data Types 代表它们不是 Objects，每个 Primitive Data Type 都没有自己的 attributes 和 methods。此外， 装有 Primitive Data Types 的 variable 确实拥有数值，而不仅仅是对其数值的记忆体位置的 reference。

Objects 和 array 都是 Reference Data Type。 Reference Data Type 变量中，储存的值是 Reference，也就是记忆体的位址 ，指向储存真实内容的记忆体区块的位置。

# Primitive Coercion

既然 Primitive Data Type 没有自己的 attributes 和 methods，为何我们使用 string.length 属性，或是 number.toFixed()这个 method 呢？

当 Primitive Data Type 使用 attributes 和 methods 时，JavaScript 将自动把数值装箱到 wrapper object 中，并改为访问该 wrapper object 上的属性。 例如，”foo”.includes(“f”) 会把”foo”放到 new String(“foo”)当中，并且执行 new String(“foo”)从 String 继承而来的 String.prototype.includes()。

这种自动装箱行为在 JavaScript 代码中是不可观察的。这就叫做 Primitive Coercion。

如果我们愿意，可以在创建 String 的时候，就使用 wrapper object 来制作。但这样做会造成 RAM 的非必要耗损，且 wrapper object 做物件时间远较制作 primitive data type 来的更久，code 完成时间会被拖延，所以 MDN 强烈不推荐使用这种写 code 的方式

```javascript
// wrapper object
let myName = new String("saltedfish");
console.log(typeof myName); // object
```

# JavaScript String Comparison

JavaScript 如同大部分的程序语言一样，String 之间的比较都是采用 compared lexicographically (字典式的比较法)。 在英文字典中，排列单词的顺序是先按照第一个字母以升序排列（即 a、b、c……z 的顺序）；如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。

JavaScript 的 String 之间的比较中，在字典顺序中较后面者会大于较前面者，所以：

”z” > “y” > … > “b” > “a”

”9” > “8” > … > “2” > “1”

因此，我们可以判断出：

```javascript
console.log("abandon" < "apple");
console.log("12" < "2");
//  这两个值都是true。
```

# 进阶 Array Methods

- [arr.map(callbackFn)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map): 创建一个新 array，其中填充了在 arr 中的每个元素上调用 callbackFn 的结果。 每次 callbackFn 执行时，返回的值都会添加到新 array 内部。

```javascript
const languages = [
  { name: "Python", rating: 9.5, popularity: 9.7, trending: "super hot" },
  { name: "Java", rating: 9.4, popularity: 8.5, trending: "hot" },
  { name: "C++", rating: 9.2, popularity: 7.7, trending: "hot" },
  { name: "PHP", rating: 9.0, popularity: 5.7, trending: "decreasing" },
  { name: "JS", rating: 8.5, popularity: 8.7, trending: "hot" },
];

let result = languages.map((lang) => {
  return lang.name.toUpperCase();
});

console.log(result);
// [ 'PYTHON', 'JAVA', 'C++', 'PHP', 'JS' ]
```

- [arr.find(callbackFn)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/find): 返回 arr 中满足 callbackFn 条件的第一个元素(也就是第一个使 callbackFn 做 return true 的元素)。 如果没有值满足 callbackFn 条件，则返回 undefined。

```javascript
const languages = [
  { name: "Python", rating: 9.5, popularity: 9.7, trending: "super hot" },
  { name: "Java", rating: 9.4, popularity: 8.5, trending: "hot" },
  { name: "C++", rating: 9.2, popularity: 7.7, trending: "hot" },
  { name: "PHP", rating: 9.0, popularity: 5.7, trending: "decreasing" },
  { name: "JS", rating: 8.5, popularity: 8.7, trending: "hot" },
];

let result = languages.find((lang) => {
  return lang.popularity > 9.0;
});

console.log(result);
// { name: 'Python', rating: 9.5, popularity: 9.7, trending: 'super hot' }
```

- [arr.filter(callbakcFn)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/filter): 过滤出在给定 arr 中通过在 callbakcFn 会 return true 的元素。Return value 是 A shallow copy of a portion of arr。

```javascript
const languages = [
  { name: "Python", rating: 9.5, popularity: 9.7, trending: "super hot" },
  { name: "Java", rating: 9.4, popularity: 8.5, trending: "hot" },
  { name: "C++", rating: 9.2, popularity: 7.7, trending: "hot" },
  { name: "PHP", rating: 9.0, popularity: 5.7, trending: "decreasing" },
  { name: "JS", rating: 8.5, popularity: 8.7, trending: "hot" },
];

let result = languages.filter((lang) => {
  return lang.rating >= 9.2;
});

console.log(result);
// [
//   {
//     name: 'Python',
//     rating: 9.5,
//     popularity: 9.7,
//     trending: 'super hot'
//   },
//   { name: 'Java', rating: 9.4, popularity: 8.5, trending: 'hot' },
//   { name: 'C++', rating: 9.2, popularity: 7.7, trending: 'hot' }
// ]
```

- [arr.some(callbackFn)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/some): 给定 callbackFn ，测试 arr 中是否至少有一个元素，通过 callbackFn 的测试(是否至少有一元素会 return true)。some()的 return type 是 boolean。

```javascript
const languages = [
  { name: "Python", rating: 9.5, popularity: 9.7, trending: "super hot" },
  { name: "Java", rating: 9.4, popularity: 8.5, trending: "hot" },
  { name: "C++", rating: 9.2, popularity: 7.7, trending: "hot" },
  { name: "PHP", rating: 9.0, popularity: 5.7, trending: "decreasing" },
  { name: "JS", rating: 8.5, popularity: 8.7, trending: "hot" },
];

let result = languages.some((lang) => lang.popularity <= 6);
console.log(result);
// true
```

- [arr.every(callbackFn)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/every): 给定 callbackFn ，测试 arr 中是否所有的元素都通过 callbackFn 的测试(是否所有的元素都会 return true)。every()的 return type 是 boolean。

```javascript
const languages = [
  { name: "Python", rating: 9.5, popularity: 9.7, trending: "super hot" },
  { name: "Java", rating: 9.4, popularity: 8.5, trending: "hot" },
  { name: "C++", rating: 9.2, popularity: 7.7, trending: "hot" },
  { name: "PHP", rating: 9.0, popularity: 5.7, trending: "decreasing" },
  { name: "JS", rating: 8.5, popularity: 8.7, trending: "hot" },
];

let result = languages.every((lang) => lang.popularity > 5);
console.log(result);
// ture
```

# JS 內建排序函式

若想要把 array 内部的元素由小到大排序，可用 JS 内建排序的 sort()方法。

sort() 方法对 array 的元素进行就地排序，也就是说，array 会被永久改变 (注意，绝大多数的 JS 内建 method 并不会改变调用此 method 的变量的值。例如，String 的 toUpperCase()就是其中一种)。若希望保留未经过排序的 array，则需要先制作一个完整的複制品。sort()的语法为：

```javascript
sort();
sort(compareFn);
```

compareFn 是定义排序顺序的函数。 如果省略，则将 array 元素按照 JavaScript 预设方式排序。若我们要自己提供 compareFn，则此 function 需要有两个 parameter a, b，而 sort()会根据 compareFn 的 return value 来决定排序顺序。若 return a - b，则採用升序排序。若 return b - a，则採用降序排序。其他 return 值为:

| compareFn(a, b) return value | sort order                     |
| ---------------------------- | ------------------------------ |
| > 0                          | sort a after b                 |
| < 0                          | sort a before b                |
| === 0                        | keep original order of a and b |

> 进阶内容
>
> 排序的时间和空间複杂度不能被保证，因为它取决于每个浏览器的 JS 引擎如何实现 sort()。但以下为几个参考方向：
>
> - V8 引擎： Quicksort or Insertion Sort (for smaller arrays)，或使用 AVL Tree。
> - Firefox： Merge sort
> - Safari： Quicksort, Merge Sort, or Selection Sort (depending on the type of array)

# for...of Loop

for...of Loop 创建一个回圈，去循环可迭代对象(iterable)内的每个元素。可迭代对象包括：string、array、 array-like object（例如：NodeList、HTMLCollection）、TypedArray、Map、Set 和 user-defined 的 iterable。

```javascript
let numbers = [10, 20, 30];
for (let n of numbers) {
  console.log(n);
}
// 10
// 20
// 30
```

```javascript
let numbers = [10, 20, 30];

for (let n of numbers) {
  console.log(numbers[n]);
}
// undefined
// undefined
// undefined
```

> 注意，object 并不是 iterable。

# for... in Loop

for...in Loop 创建一个回圈，去循环一个 JS 物件中所有的可枚举属性(enumerable properties)。

- 对于 object 来说，enumerable properties 就是 keys。
- 对于 array 来说，enumerable properties 就是 indices。
- 对于 String 来说，enumerable properties 也是 indices。

```javascript
let numbers = [10, 20, 30];
for (let n in numbers) {
  console.log(numbers[i]);
}
// 10
// 20
// 30
```

```javascript
let Wilson = {
  name: "Wilson Ren",
  age: 25,
};

for (let i in Wilson) {
  console.log(i);
}
console.log();
for (let i in Wilson) {
  console.log(Wilson[i]);
}
// name
// age

// Wilson Ren
// 25
```
