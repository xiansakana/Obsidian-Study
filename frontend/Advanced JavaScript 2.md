---
title: Advanced JavaScript 2
date: 2024-04-25T19:24:49Z
lastmod: 2024-09-05T13:04:37Z
---

# Execution Context 执行环境

当 JS 引擎执行程序码(script)时，便会创建 execution contexts(执行环境) 。 JavaScript 共会建立两种执行环境：

1. 全局执行环境 (Global Execution Context)
2. 函数执行环境 (Function Execution Context)

每种 execution context 都包含两个阶段：创造阶段 creation phase 和 执行阶段 execution phase。

## 全局执行环境

当初次执行一份 JavaScript 程式码时， JS 引擎会创造第一种 execution context，叫 Global Execution Context。在 Global Execution Context 内部，会先进入 creation phase：

1. 创建 global object。 ( 例如，浏览器中的 window object，或 Node.js 中的 global object。)
2. 建立 scope。
3. 创建 this 关键字，并被绑定至 global object。
4. 将 variables 、class 和 function 分配至记忆体。 (hoisting 步骤)

creation phase 结束后，会进入 execution phase：

1. 逐行( line by line )执行程式码。
2. 遇到递回时，则使用 call stack 来排定工作顺序。

## 函数执行环境

每次的 function call ，JS 引擎也都会创造一个 Function Execution Context。 函数执行环境与全局执行环境非常类似，一样也有 creation phase 以及 execution phase，但差别在于，函数执行环境不创建 global object，而是创建 argument object。 Argument object 包含了被放入此函式的 parameters 的数值参照值(a reference to all the parameters passed into the function)。函数执行环境的 creation phase 是：

1. 创建 argument object。
2. 建立 scope (依照 closure 这个准则)。
3. 创建 this 关键字。
4. 将 variables 、class 和 function 分配至记忆体。 (hoisting 步骤)

creation phase 结束后，会进入 execution phase：

1. 逐行( line by line )执行程式码。
2. 遇到递回时，则使用 call stack 来排定工作顺序。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182253924.png)

# [Hoisting](https://developer.mozilla.org/zh-CN/docs/Glossary/Hoisting)

JavaScript Hoisting 是指 JS 引擎在执行代码之前，将 function、variables 或 class 的 declaration 移动到其范围顶部的过程。

Hoisting 的优点之一是，它允许我们在 code 中，declare function 之前使用这个 function 。（但要小心，这个功能只对 function declaration 有用。）

Hoisting 也适用于 variables ，因此我们可以在 declaration 和/或 initialization 之前在 code 中使用 variables 。然而 JavaScript 只 hoist declaration ，而不是 initialization ！也就是说，let x = 10; 这段程序码只有 let x 会被放到程式码顶部。

Hoisting 发生时，对于使用 var 做 declaration 的 variable 会给定初始值 undefined。然而，对于使用 let, const 做 declaration 的 variable 并不会给定任何初始值。

let 可以 declare without initialization，且我们可以用 console.log()检查 let 的变数值是 undefined，但这个 undefined 的 initialization 并不像 var 是发生在 creation phase 的 hoisting 阶段发生的，而是在 execution phase 的阶段。

# Scope and Closure

Scope 是指，在当前的 execution context 之中，变量的可访问性(accessibility)为何？我们在 function A 所宣告的变量，在 function B 内部可以使用(访问)吗？又或者，假定程序码是：

```javascript
let x = 10;
function hello() {
  function hello2() {
    return x + 10;
  }
}
```

hello2()可以访问到的全局变量(global variable)的 x = 10 吗？（可以）了解 Scope 可以知道，每个变量在哪些区域或范围是有意义的，或者是说，变量在哪些区域是可访问或可使用的。

JavaScript 的变数有以下几种 Scope ：

1. Global scope: The default scope for all code running in the script.
2. Module scope: The scope for code running in module mode.
3. Function scope: The scope is created with a function.

   此外，用 let 或是 const 去声明的变量属于下面这个额外的 scope：
4. Block scope: The scope created with a pair of curly braces (a block).

在 function execution context 中，如果发现不在 function scope 内部的变量，JavaScript 将转到其他地方查找。Closure（闭包）就是指这种将函数与其周围的状态或语词环境结合在一起的组合。在 JavaScript 中，每次 function execution context 都会在 creation phase 创建 closure。

Closure 的规则是：

1. 从 Argument Object 以及 local variable 去寻找。
2. 若从 1 找不到，则从记忆体被分配给函数的位置开始寻找。
3. 若在目前的 execution context 找不到，就继续往外层、往全局一层一层的去找。

# Call Stack and Recursion

Call stack 是 JS 引擎追踪本身在调用多个函数的程式码中位置的机制（数据结构的一种）。Call stack 可以帮助我们知道 JS 引擎当前正在运行什么函式以及从该函数中调用了哪些函式等。

其机制为：

1. 当执行函式 f_1 时， JS 引擎将其添加到 call stack 中，然后开始执行该函式。
2. 若该函式内部又调用其他函式 f2 ，则将函式 f2 添加到 call stack 中，然后开始执行该函式。
3. 当 f2 执行完毕后， JS 引擎将其从 call stack 中取出，并且从 f1 停止的位置继续执行。
4. 如果 call stack 堆叠过高，高出记忆体分配给 call stack 的最大空间，则导致“stack overflow”的问题。

在数学上, 递回关系 (recurrence relation) 是一种定义数列的方式：数列的每一项目定义为前面项的函数。例如：我们可以定义数列 S :

1. A base case 𝑆(1) = 2
2. 𝑆(𝑛) = 2 ∙ 𝑆(𝑛 − 1) 𝑓𝑜𝑟 𝑛 ≥ 2

以上面的规则可知，S 会是等比数列 2, 4, 8, 16, 32, …

程序语言中，递回演算法(recursive algorithm)有相似的概念。当一个函式内部，执行自己这个函式，这种情况就是递回演算法。(因此，递迴演算法绝对会产生 call stack。)

递回演算法的设计上，与数学归纳法以及递回关係 (recurrence relation) 相似。我们需要定义一个 base case (基准情况)。 Base case 的用途是为了避免递回演算法产生在 call stack 上无限叠加的情况。

- 费波那契数列

  在数学上，费波那契数列是以递迴的方法来定义：
  𝐹(0) = 0
  𝐹(1) = 1
  𝐹(𝑛) = 𝐹(𝑛−1) + 𝐹(𝑛−2) 𝑓𝑜𝑟 𝑎𝑙𝑙 𝑛 ≥ 2.
  所以，费波那契数列的前几项列出来会是:
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

```javascript
function fsequence(n) {
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  return fsequence(n - 1) + fsequence(n - 2);
}
console.log(fsequence(10));
```

# Constructor Function

在函式执行环境的 creation phase 当中，每个 function 都有创建 this 关键字这个步骤。this 关键字指的是正在执行当前 method 的 object。 如果被调用的 function 是常规 function 而非 method，则 this 关键字会指向 global object (因为 closure 会向外找 this 这个字，而在 global execution context 中可以找到，所以 this 才会指向 global object )。

在 JavaScript 的语法中，若 function 被调用时使用了 new 关键字，则 function 会被当成 constructor function 来使用。 Constructor function 中的 this 关键字指的是一个新制作的物件。此外，New 关键字可以在分配额外的记忆体给 constructor function 所新制作的物件。此物件会自动被 constructor function 给 return。

```javascript
// constructor function
// 在JavaScript当中，constructor function以大写开头
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sayHi = function () {
    console.log(this.name + "说你好");
  };
}
let wilson = new Person("Wilson", 26);
let mike = new Person("Mike Huang", 28);
let grace = new Person("Grace Xie", 26);
console.log(wilson);
grace.sayHi();
// Person { name: 'Wilson', age: 26, sayHi: [Function (anonymous)] }
// Grace Xie说你好
```

透过使用 Constructor Function，我们可以大量制造 attributes 与 methods 相似的物件。(若有学过 Java，这就是 Java Class 当中的 constructor 语法。)

Constructor Function 制作出的每个物件，是独立的，所以会单独佔据记忆体位置。

# Inheritance and the Prototype Chain

在 JavaScript 中，每个对象都有一个 private attribute 叫做`__proto__`。 `__proto__`属性存放的值是另一个对象。若对象 A 的`__proto__`属性的值是设定成另一个对象 B，则物件 A 就继承了对象 B 的所有 attributes 以及 methods。

```javascript
let wilson = {
  name: "Wilson",
  sayHi() {
    console.log("你好");
  },
};

let mike = {
  __proto__: wilson,
};

console.log(mike.name);
mike.sayHi();
```

每个 constructor function 都可以设定 prototype 属性(prototype 属性本质上来说，就是一个 empty object)。所有从 constructor function 制作出来的对象， 其`__proto__`属性都是自动指向 constructor function 的 prototype 属性。

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sayHi = function () {
    console.log(this.name + "说你好");
  };
}
let wilson = new Person("Wilson", 26); // wilson.__proto__ => Person.prototype
let mike = new Person("Mike Huang", 28); // mike.__proto__ => Person.prototype
```

例如，constructor function A 制作的对象 obj，如果检查`obj.__proto__ == A.prototype`，可以看到 true。因为`obj.__proto__`以及 A.prototype 都是 reference data type，所以 true 代表两者指向同个记忆体位置。

```javascript
console.log(wilson.__proto__ == Person.prototype);
// true
```

因为所有从 constructor function 制作出来的对象， 其`__proto__`属性都是自动指向 constructor function 的 prototype 属性，所以物件都会自动继承所有在 constructor function 的 prototype 属性内定义的 attributes and methods。像这样子从 constructor function 的 prototype 属性继承 attributes and methods 的原理，就叫做“Prototype Inheritance”。

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sayHi = function () {
    console.log(this.name + "说你好");
  };
}

Person.prototype.hello = function () {
  console.log(this.name + "说哈喽");
};

let wilson = new Person("Wilson Ren", 26); // wilson.__proto__ => Person.prototype
let mike = new Person("Mike Huang", 28); // mike.__proto__ => Person.prototype
wilson.hello();
// Wilson Ren说哈喽
```

我们可以根据这个特性，来节省记忆体空间。若从 constructor function 制作出的每个物件都有相似的 methods，我们可以把 methods 全部移动到 constructor function 的 prototype 属性内部，而不是在个别的对象中重复定义 methods。

使用 constructor function 来做物件的好处在于：

1. 程式码容易撰写且维护。 大量物件可以透过 constructor function 来制作。
2. 节省记忆体空间。两个物件若有可以共用 attritubes 或 methods，但分开制作，则会分别佔用记忆体内的不同位置。若使用 constructor function 来制作，则两个物件继承来的 attributes 以及 methods 都是指向记忆体的相同位置，所以可以达到节省记忆体的功效。

JS 内建的资料类型都有继承其他的 Prototype。例如，[1, 2, 3]这个 array 继承了 Array Prototype，而 Array Prototype 又继承自 Object Prototype。这种 Prototype 不断往上连结的结果就叫做 Prototype Chain。

JavaScript 中的所有物件最后的 Prototype Chain 都会连到一个叫做 ”Object Prototype“的地方。Object Prototype 是 Prototype Chain 的终点。

# JS Built-in Constructors

在 JavaScript 中，有许多内建的 constructors，例如 String, Number, Boolean, Array, Object 等等。这些 constructor function 的 prototype 属性都有设定其他的 methods，所以在 MDN 的文件内标题会看到像是：

```javascript
String.prototype.indexOf();
Number.prototype.toFixed();
Array.prototype.push();
```

等等的写法。许多 JavaScript 中常见的数据类型，都有内建的 constructors。我们制作的资料的`__proto__`属性都指向 constructors 的 prototype 属性，所以可以使用 JavaScript 内建的这些 methods。

我们也可以直接调用 JS 内建的 Constructors。例如。在 JavaScript 使用 new String(“Hello World”)，代表直接制作一个新 String Object。但因为 JavaScript 有 coercion 功能，所以这样写是非常不好的写法。应该直接写成” Hello World”即可。

但对于 new Array([1, 2, 3])来说，却跟[1, 2, 3]这种写法差异不大。(正确来说，不使用 Array constructor 还是比较好，因为这样写的话，CPU 需要执行比较多步骤。)

# Function Methods

在 JavaScript 中，function 是一种特别的对象。(从 Prototype inheritance 可以看出，所有的 function 都有继承 Object prototype。因此，function 也是 object 的一种)。

在 JavaScript 中的 Function.prototype 内有以下三个常用 methods：

- [function.bind(obj)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind): 将 function 的 this 关键字绑定(bind)为 obj 。

```javascript
let Grace = {
  name: "Grace",
  age: 26,
};

function getAge() {
  return this.age;
}

let newFunction = getAge.bind(Grace);
console.log(newFunction());
// 26
```

- [function.call(obj, arg1, /_ …, _/ argN)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/call): 使用给定的 obj 当作 this 值来调用函数。 arg1, /_ …, _/ argN 为 optional。

```javascript
let Grace = {
  name: "Grace",
  age: 26,
};

function getAge(country, height) {
  console.log("this.name" + "来自" + country + ", 身高为" + height + "cm");
  return this.age;
}
getAge.call(Grace, "台湾", 160);
// Grace来自台湾, 身高为160cm
```

- [function.apply(obj, argsArray)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/apply): 与 call 相同，但 arguments 是使用 arguments array。

```javascript
let Grace = {
  name: "Grace",
  age: 26,
};

function getAge(country, height) {
  console.log(this.name + "来自" + country + ", 身高为" + height + "cm");
  return this.age;
}

getAge.apply(Grace, ["台湾", 160]);
// Grace来自台湾, 身高为160cm
```

# Prototype Inheritance in Constructors

一个 constructor function A 可以透过两个设定来继承另一个 constructor function B 的 prototype 对象：

1. 在 constructor function A 的内部执行 B.call(this, args1, …, argsN)。我们可以透过这段程式码直接将 B 所设定的属性套给 A 做使用。
2. 设定 A.prototype = Object.create(B.prototype)。 Object.create()可以创建一个全新的对象。这样一来，所有在 B.prototype 内部的 attributes 与 methods 都可以套用给 A.prototype。所有 A.prototype 所设定的额外的 attributes 与 methods 都需要写在 A.prototype = Object.create(B.prototype)这行程式码的下方。

不能写 A.prototype = B.prototype 是因为，constructor.prototype 是 reference data type，如果写
A.prototype = B.prototype;
A.prototype.add = function() {…}
则 A, B 两个 prototype 都指向记忆体的相同位置，且两个 prototype 都有 add()这个 methods 了。

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.sayHi = function () {
  console.log(this.name + "说你好");
};

function Student(name, age, major, grade) {
  Person.call(this, name, age);
  this.major = major;
  this.grade = grade;
}

Student.prototype = Object.create(Person.prototype);

Student.prototype.study = function () {
  console.log(this.name + "正在努力读" + this.major);
};

let mike = new Student("Mike Huang", 26, "Chemistry", 3.5);
console.log(mike.name);
mike.sayHi();
mike.study();
// Mike Huang
// Mike Huang说你好
// Mike Huang正在努力读Chemistry
```

# Class

在 ECMAScript 2015 中引入的 JavaScript Class 语法，可以用来取代 constructor function。Class 语法是 JavaScript 基于现有的 prototype inheritance 的语法糖。(Class 语法与 constructor function 语法可以完全互换)

```javascript
class Student {
  constructor(name, age, major) {
    this.name = name;
    this.age = age;
    this.major = major;
  }

  sayHi() {
    console.log(this.name + "说你好");
  }
}
```

若一个 constructor 要继承另一个 constructor 的 prototype 物件，则可使用 extends 关键字。

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHi() {
    console.log(this.name + "说你好");
  }
}

class Student extends Person {
  constructor(name, age, major, grade) {
    super(name, age);
    this.major = major;
    this.grade = grade;
  }

  study() {
    console.log(this.name + "正在努力读" + this.major);
  }
}

let mike = new Student("Mike Huang", 26, "Chemistry", 3.5);
mike.sayHi();
mike.study();
```

Static 关键字在 class 上定义 attributes 与 methods。另外，我们可以透过 class 本身来访问 static variable 或是执行 static method。 Static 关键字所设定的 attribute 和 method 属于 class 本身，不属于每个由 class 所制作出的物件。(本质上来说，Static 关键字就是将 attribute 与 method 设定在 constructor function 这个物件上面，而不是在 constructor.prototype 这个 constructor function 的属性上面)

```javascript
class Student {
  static exampleProperty = 10;

  constructor(name, age, major) {
    this.name = name;
    this.age = age;
    this.major = major;
  }

  sayHi() {
    console.log(this.name + "说你好");
  }

  static exampleFunction() {
    console.log("这是一个没有特别功能的function");
  }
}

let mike = new Student("Mike", 26, "化学");
Student.exampleFunction();
mike.sayHi();
```

# Static Methods and Attributes in JS

JavaScript 当中的内建 Class (or constructor function)有许多 static properties, static methods, instance properties, instance methods。

例如，Array 的 Array.isArray()就是 Array Class 的 static method，可用来确认某个资料是不是 Array。若我们用 typeof operator 确认 array 的数据类型，只能看到 object。因此，要确认某个变数是否为 array，必须用 Array.isArray()。

另一个例子，Math Class 内部所有的 properties 以及 methods 都是 static，所以我们可以使用 Math.E、Math.PI、Math.floor()等等的功能。

```javascript
class Circle {
  static allCircles = [];

  constructor(radius) {
    this.radius = radius;
    Circle.allCircles.push(this);
  }

  getArea() {
    return Math.PI * this.radius * this.radius;
  }

  getPerimeter() {
    return 2 * Math.PI * this.radius;
  }

  // static
  static getAreaFormula() {
    return "圆面积公式为pi * r * r";
  }

  // static method
  static getAllCirclesAreaTotal() {
    let total = 0;
    Circle.allCircles.forEach((circle) => {
      total += circle.getArea();
    });
    return total;
  }
}

let c1 = new Circle(5);
let c2 = new Circle(10);
let c3 = new Circle(15);
console.log(Circle.getAllCirclesAreaTotal());
```
