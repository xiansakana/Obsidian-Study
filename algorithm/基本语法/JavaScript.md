---
title: JavaScript
date: 2024-05-21T15:15:54Z
lastmod: 2024-09-05T13:12:42Z
---

# String

## 拼接

1. 使用加号运算符

```javascript
let a = 'java'
let b = a + 'script'
```

2. 使用\${}配合反引号

```javascript
let a = 'java'
let b = `hello ${a}script`
```

3. 使用concat()函数

```javascript
let a = 'java'
let b = 'script'
let str = a.concat(b)
```

4. 使用join()函数（针对数组中的字符连接）

join() 方法是操作数组，将数组拼接后转为字符串返回一个新字符串，元素将由指定的分隔符分隔。默认分隔符是逗号 (,)。（）里面的separator为分隔符，默认为逗号分隔，join（）方法不会改变原数组。

```javascript
let arr = ['hello','java','script']
let str = arr.join(" ")
```

## split()

​`str.split(separator, limit);`​

* **separator**​ ****：**** 用于指定用于分割字符串的字符或正则表达式。如果未指定分隔符，则整个字符串将成为一个数组元素。当字符串中没有分隔符时也会发生同样的情况。如果分隔符是空字符串（""），则字符串的每个字符都被分隔开。
* ****limit：**** 定义给定字符串中可找到的分割数的上限。如果达到限制后字符串仍未选中，则不会在数组中报告。

```javascript
let str = 'It iS a 5r&amp;e@@t Day.'
let array = str.split(" ");
console.log(array);
// [ 'It', 'iS', 'a', '5r&amp;e@@t', 'Day.' ]
```

# Array

## 拼接

1. concat

```javascript
var a=[1,2,3,4,5];
var b=['lucy','andy','bob'];
var c =a.concat(b)
```

2. for循环​push()​逐个添加

```javascript
var a=[1,2,3,4,5];
var b=['bob','cily','luck'];
for(var i=0;i<b.length;i++){
    a.push(b[i]); 
}
```

3. apply()

```javascript
var a=[1,2,3,4,5];
var b=['bob','cily','luck'];
a.push.apply(a,b);
```

4. ES6扩展运算符

```javascript
var a=[1,2,3,4,5];
var b=['c','d','e','f'];
a.push(...b);
```

## length

```javascript
const len = nums.length
```

## 排序

* 一维数组

```javascript
const months = ['March', 'Jan', 'Feb', 'Dec'];
months.sort();
console.log(months);
// ["Dec", "Feb", "Jan", "March"]

const array1 = [1, 30, 4, 21, 100000];
array1.sort();
console.log(array1);
// [1, 100000, 21, 30, 4]
```

* 二维数组

```javascript
const intervals = [[1,3],[15,18],[2,6],[8,10]]
intervals.sort((a, b) => a[0] - b[0]);
console.log(intervals);
// [[1,3],[2,6],[8,10],[15,18]]
```

# 其他

‍
