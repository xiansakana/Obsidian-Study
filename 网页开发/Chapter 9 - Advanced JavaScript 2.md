## Execution Context 执行环境

当JS引擎执行程序码(script)时，便会创建 execution contexts(执行环境) 。 JavaScript 共会建立两种执行环境：

1. 全局执行环境 (Global Execution Context)
2. 函数执行环境 (Function Execution Context)

每种 execution context 都包含两个阶段：创造阶段 creation phase 和 执行阶段 execution phase。

### 全局执行环境

当初次执行一份JavaScript程式码时， JS引擎会创造第一种 execution context，叫 Global Execution Context。在 Global Execution Context 内部，会先进入creation phase：

1. 创建global object。 ( 例如，浏览器中的window object，或Node.js中的 global object。)
2. 建立 scope。
3. 创建 this 关键字，并被绑定至 global object。
4. 将 variables 、class 和 function 分配至记忆体。 (hoisting步骤)

creation phase结束后，会进入execution phase：

1. 逐行( line by line )执行程式码。
2. 遇到递回时，则使用call stack来排定工作顺序。

### 函数执行环境

每次的 function call ，JS引擎也都会创造一个Function Execution Context。 函数执行环境与全局执行环境非常类似，一样也有 creation phase 以及 execution phase，但差别在于，函数执行环境不创建global object，而是创建argument object。 Argument object包含了被放入此函式的parameters的数值参照值(a reference to all the parameters passed into the function)。函数执行环境的creation phase是：

1. 创建argument object。
2. 建立 scope (依照 closure 这个准则)。
3. 创建 this 关键字。
4. 将 variables 、class 和 function 分配至记忆体。 (hoisting步骤)

creation phase结束后，会进入execution phase：

1. 逐行( line by line )执行程式码。
2. 遇到递回时，则使用call stack来排定工作顺序。

![](https://img.xiansakana.xyz/202310182253924.png)

## [Hoisting](https://developer.mozilla.org/zh-CN/docs/Glossary/Hoisting)

JavaScript Hoisting是指JS引擎在执行代码之前，将function、variables或class的declaration移动到其范围顶部的过程。

Hoisting的优点之一是，它允许我们在code中，declare function之前使用这个function 。（但要小心，这个功能只对function declaration有用。）

Hoisting也适用于variables ，因此我们可以在declaration和/或initialization之前在code中使用variables 。然而 JavaScript 只hoist declaration ，而不是initialization ！也就是说，let x = 10; 这段程序码只有let x会被放到程式码顶部。

Hoisting发生时，对于使用 var 做declaration的variable会给定初始值undefined。然而，对于使用 let, const 做declaration的variable并不会给定任何初始值。

let可以declare without initialization，且我们可以用console.log()检查let的变数值是undefined，但这个undefined 的 initialization并不像var是发生在creation phase的hoisting阶段发生的，而是在execution phase的阶段。

## Scope and Closure

Scope是指，在当前的execution context之中，变量的可访问性(accessibility)为何？我们在function A所宣告的变量，在function B内部可以使用(访问)吗？又或者，假定程序码是：

```javascript
let x = 10;
function hello() {
  function hello2() {
    return x + 10;
  }
}
```

hello2()可以访问到的全局变量(global variable)的x = 10吗？（可以）了解Scope可以知道，每个变量在哪些区域或范围是有意义的，或者是说，变量在哪些区域是可访问或可使用的。

JavaScript 的变数有以下几种Scope ：

1. Global scope: The default scope for all code running in the script.

2. Module scope: The scope for code running in module mode.

3. Function scope: The scope is created with a function.

   此外，用let或是const去声明的变量属于下面这个额外的scope：

4. Block scope: The scope created with a pair of curly braces (a block).

在function execution context中，如果发现不在function scope内部的变量，JavaScript 将转到其他地方查找。Closure（闭包）就是指这种将函数与其周围的状态或语词环境结合在一起的组合。在 JavaScript 中，每次function execution context都会在creation phase创建closure。

Closure的规则是：

1. 从Argument Object以及local variable去寻找。
2. 若从1找不到，则从记忆体被分配给函数的位置开始寻找。
3. 若在目前的execution context找不到，就继续往外层、往全局一层一层的去找。

## Call Stack and Recursion

Call stack是JS引擎追踪本身在调用多个函数的程式码中位置的机制（数据结构的一种）。Call stack可以帮助我们知道JS引擎当前正在运行什么函式以及从该函数中调用了哪些函式等。

其机制为：

1. 当执行函式f_1时， JS引擎将其添加到call stack中，然后开始执行该函式。
2. 若该函式内部又调用其他函式f2  ，则将函式f2添加到call stack中，然后开始执行该函式。
3. 当f2执行完毕后， JS引擎将其从call stack中取出，并且从f1停止的位置继续执行。
4. 如果call stack堆叠过高，高出记忆体分配给call stack的最大空间，则导致“stack overflow”的问题。

在数学上, 递回关系 (recurrence relation) 是一种定义数列的方式：数列的每一项目定义为前面项的函数。例如：我们可以定义数列 S :

1. A base case 𝑆(1) = 2
2. 𝑆(𝑛) = 2 ∙ 𝑆(𝑛 − 1) 𝑓𝑜𝑟 𝑛 ≥ 2

以上面的规则可知，S 会是等比数列 2, 4, 8, 16, 32, …

程序语言中，递回演算法(recursive algorithm)有相似的概念。当一个函式内部，执行自己这个函式，这种情况就是递回演算法。(因此，递迴演算法绝对会产生call stack。)

递回演算法的设计上，与数学归纳法以及递回关係 (recurrence relation) 相似。我们需要定义一个base case (基准情况)。 Base case 的用途是为了避免递回演算法产生在call stack上无限叠加的情况。

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

## Constructor Function

在函式执行环境的creation phase当中，每个function都有创建 this 关键字这个步骤。this关键字指的是正在执行当前method的object。 如果被调用的function是常规function 而非method，则this关键字会指向global object (因为closure会向外找this这个字，而在global execution context中可以找到，所以this才会指向global object )。

在JavaScript的语法中，若function被调用时使用了new关键字，则function会被当成constructor function来使用。 Constructor function中的this关键字指的是一个新制作的物件。此外，New关键字可以在分配额外的记忆体给constructor function所新制作的物件。此物件会自动被constructor function给return。

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

透过使用Constructor Function，我们可以大量制造attributes与methods相似的物件。(若有学过Java，这就是Java Class当中的constructor语法。)

Constructor Function制作出的每个物件，是独立的，所以会单独佔据记忆体位置。

## Inheritance and the Prototype Chain

在JavaScript中，每个对象都有一个private attribute叫做`__proto__`。 `__proto__`属性存放的值是另一个对象。若对象A的`__proto__`属性的值是设定成另一个对象B，则物件A就继承了对象B的所有attributes以及methods。

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

每个constructor function都可以设定prototype属性(prototype属性本质上来说，就是一个empty object)。所有从constructor function制作出来的对象， 其`__proto__`属性都是自动指向constructor function的prototype属性。

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

例如，constructor function A制作的对象obj，如果检查`obj.__proto__ == A.prototype`，可以看到true。因为`obj.__proto__`以及 A.prototype都是 reference data type，所以true代表两者指向同个记忆体位置。

```javascript
console.log(wilson.__proto__ == Person.prototype);
// true
```

因为所有从constructor function制作出来的对象， 其`__proto__`属性都是自动指向constructor function的prototype属性，所以物件都会自动继承所有在constructor function的prototype属性内定义的attributes and methods。像这样子从constructor function的prototype属性继承attributes and methods的原理，就叫做“Prototype Inheritance”。

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

我们可以根据这个特性，来节省记忆体空间。若从constructor function制作出的每个物件都有相似的methods，我们可以把methods全部移动到constructor function的prototype属性内部，而不是在个别的对象中重复定义methods。

使用constructor function来做物件的好处在于：

1. 程式码容易撰写且维护。 大量物件可以透过 constructor function 来制作。
2. 节省记忆体空间。两个物件若有可以共用attritubes或methods，但分开制作，则会分别佔用记忆体内的不同位置。若使用constructor function 来制作，则两个物件继承来的attributes以及methods都是指向记忆体的相同位置，所以可以达到节省记忆体的功效。

JS内建的资料类型都有继承其他的Prototype。例如，[1, 2, 3]这个array继承了Array Prototype，而Array Prototype又继承自Object Prototype。这种Prototype不断往上连结的结果就叫做Prototype Chain。

JavaScript中的所有物件最后的 Prototype Chain 都会连到一个叫做 ”Object Prototype“的地方。Object Prototype 是 Prototype Chain 的终点。

## JS Built-in Constructors

在JavaScript中，有许多内建的constructors，例如String, Number, Boolean, Array, Object等等。这些 constructor function 的prototype属性都有设定其他的methods，所以在MDN的文件内标题会看到像是：
```javascript
String.prototype.indexOf()
Number.prototype.toFixed()
Array.prototype.push()
```

等等的写法。许多JavaScript中常见的数据类型，都有内建的constructors。我们制作的资料的`__proto__`属性都指向constructors的prototype属性，所以可以使用JavaScript内建的这些methods。

我们也可以直接调用JS内建的Constructors。例如。在JavaScript使用 new String(“Hello World”)，代表直接制作一个新String Object。但因为JavaScript有coercion功能，所以这样写是非常不好的写法。应该直接写成” Hello World”即可。

但对于new Array([1, 2, 3])来说，却跟[1, 2, 3]这种写法差异不大。(正确来说，不使用Array constructor还是比较好，因为这样写的话，CPU需要执行比较多步骤。)

## Function Methods

在JavaScript中，function是一种特别的对象。(从Prototype inheritance可以看出，所有的function都有继承Object prototype。因此，function也是object的一种)。

在JavaScript中的Function.prototype内有以下三个常用methods：

- [function.bind(obj)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind): 将function 的 this 关键字绑定(bind)为obj 。

```javascript
let Grace = {
  name: "Grace",
  age: 26,
};

function getAge() {
  return this.age;
}

let newFunction = getAge.bind(Grace);
console.log(newFunction())
// 26
```

- [function.call(obj, arg1, /* …, */ argN)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/call): 使用给定的obj当作 this 值来调用函数。 arg1, /* …, */ argN为optional。

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

- [function.apply(obj, argsArray)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/apply): 与call相同，但arguments是使用arguments array。

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

## Prototype Inheritance in Constructors

一个 constructor function A可以透过两个设定来继承另一个constructor function B的prototype对象：

1. 在constructor function A的内部执行B.call(this, args1, …, argsN)。我们可以透过这段程式码直接将B所设定的属性套给A做使用。
2. 设定A.prototype = Object.create(B.prototype)。 Object.create()可以创建一个全新的对象。这样一来，所有在B.prototype内部的attributes与methods都可以套用给A.prototype。所有A.prototype所设定的额外的attributes 与methods都需要写在A.prototype = Object.create(B.prototype)这行程式码的下方。

不能写A.prototype = B.prototype是因为，constructor.prototype是reference data type，如果写
A.prototype = B.prototype;
A.prototype.add = function() {…}
则A, B两个prototype都指向记忆体的相同位置，且两个prototype都有add()这个methods了。

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

## Class

在 ECMAScript 2015 中引入的 JavaScript Class语法，可以用来取代constructor function。Class语法是 JavaScript 基于现有的prototype inheritance的语法糖。(Class语法与constructor function语法可以完全互换)

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

若一个constructor要继承另一个constructor的prototype物件，则可使用extends关键字。

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

Static关键字在class上定义attributes与methods。另外，我们可以透过class本身来访问static variable或是执行static method。 Static关键字所设定的attribute和method属于class本身，不属于每个由class所制作出的物件。(本质上来说，Static关键字就是将attribute与method设定在constructor function这个物件上面，而不是在constructor.prototype这个constructor function的属性上面)

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

## Static Methods and Attributes in JS

JavaScript当中的内建Class (or constructor function)有许多 static properties, static methods, instance properties, instance methods。

例如，Array的Array.isArray()就是Array Class的static method，可用来确认某个资料是不是Array。若我们用typeof operator确认array的数据类型，只能看到object。因此，要确认某个变数是否为array，必须用Array.isArray()。

另一个例子，Math Class内部所有的properties以及methods都是static，所以我们可以使用Math.E、Math.PI、Math.floor()等等的功能。

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

