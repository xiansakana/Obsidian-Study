---
title: Async JavaScript
tags:
  - JavaScript
  - 前端
  - Ajax
categories: 学习
cover: "https://cdn.cbd.int/xiansakana-blog-img/202311140929903.jpg"
abbrlink: 3d61c948
date: 2023-11-14 09:24:21
---

# Ajax

AJAX 即「Asynchronous JavaScript and XML」(非同步的 JavaScript 与 XML 技术)，指的是一套综合了多项技术的浏览器端网页开发技术。

AJAX 在客户端使用各种 Web 技术来创建异步(asynchronous) Web 应用程序。应用程序可以在背景从服务器发送和获得数据，而不干扰现有页面的显示和行为。通过将数据交换层与表示层分离，Ajax 允许网页以及扩展的 Web 应用程序动态地更改内容，而无需重新加载整个页面。在实践中，数据的传送通常使用 JSON 而不是 XML。

常见的 Ajax 应用的例子是，我们在 YouTube 或是 Google 搜寻时，网站会根据我们前面打的几个字，猜想我们想要搜寻的关键字是什么。这就是不干扰现有页面的显示和行为的情况下，从服务器发送和获得数据，并且更新网页的方法。

![](https://cdn.cbd.int/xiansakana-blog-img/202311112120918.png)

# 同步与异步

在计算机程式中，异步(asynchronous)代表着一个 process 独立于其他 process 运行，而同步(synchronous)代表着一个 process 仅在某个其他 process 完成或移交后而运行。

![](https://cdn.cbd.int/xiansakana-blog-img/202311112122765.png)

通常来说，JavaScript 的特性是 single-threaded synchronous，代表 JavaScript 是个一次只会做一件事情的程式语言。然而，JS 有内建的 asynchronous function，例如 setTimeout()。 setTimeout() funtion 设置一个计时器，一旦计时器时间到，该计时器就会执行一个函数或指定的一段代码。 setTimeout()的语法为：

```javascript
setTimeout(code, delay);
```

Code 是 delay 结束时要执行的程式码，delay 是在执行指定的函数或代码之前计时器应等待的时间（以毫秒为单位）。如果省略此参数，则使用值 0，表示“立即”执行。

```javascript
console.log(’start’);
setTimeout(() => {
    console.log(‘Here is the code.’);
}, 2000)
console.log(end’);
// start
// end
// Here is the code.
```

# Promise

Promise 是现代 JavaScript 中异步编程的基础。 Promise 是一个由 asynchronous function 所 return 的对象，主要功能是，Promise 会代理一个建立时不用预先得知结果的值。

Promise 使我们能够系结着发动非同步操作后，最终的成功值(success value)或失败讯息(failure reason)的处理函式（handlers）。我们向服务器传送 request 之后，因为需要等待 response 的时间，所以我们会先得到一个 Promise，而这个 Promise 目前的状态是「搁置」(pending)。

一个 Promise 对象有处于以下三种状态：

1. 搁置 (pending)：初始状态，并不是 fulfilled 与 rejected。
2. 实现 (fulfilled)：表示操作成功地完成。
3. 拒绝 (rejected)：表示操作失败了。

Promise 在 pending 后的几秒之内，状态可能变成 fulfilled 或是 rejected。一个处于搁置(pending)状态的 Promise ，若操作成功，能够将状态变成 fulfilled，或是因为某些原因或错误而被操作失败，变成拒绝(rejected)状态。当上述任一状态转换发生时，那些透过 then 方法所系结的 callback 就会被调用。

例如：

```javascript
let promiseObject = fetch(URL);
promiseObject.then((data) => {
  console.log(data);
});
```

这段程式码中，当 promiseObject 从 pending 变成 fulfilled 之后，.then()内部的 callback function 就会被 JavaScript 自动执行。执行时，带入的参数就是从 URL 获得的 HTTP Response 内容。

![](https://cdn.cbd.int/xiansakana-blog-img/202311112143059.png)

![](https://cdn.cbd.int/xiansakana-blog-img/202311112146306.png)

```javascript
let fetchPromise = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json"
);
fetchPromise.then((response) => {
  response.json().then((data) => {
    console.log(data);
  });
});
// 下面代码等效
// fetchPromise
// .then((response) => response.json())
// .then((data) => {
//  console.log(data);
// })
```

# Catching Errors

为了支持错误处理，Promise 物件提供了一个 catch() 方法，跟 then()很像。我们调用.catch()时，传入一个 callback function 当作参数。传递给 catch() 的处理函数在异步操作失败时自动被 JavaScript 调用。 catch()内部的 callback function 被调用时，参数会被放入错误讯息，通常以变数 e 或是 err 代表错误(error)。

当串连多个.then 语句时，后一个.then()内部的 callback function 被执行时，所用的参数是前一个.then()中的 callback function 所回传的值。

如果将 catch() 添加到 Promise Chain 的末尾，那么当任何异步函数调用失败时都会调用它。

```javascript
fetchPromise
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  })
  .catch((e) => {
    console.log(fetchPromise);
    console.log(e);
  });
```

# Combining Multiple Promises

当我们的操作由多个异步函数组成时，我们需要用到 promise chaining，让我们在开始下一个函数之前完成前一个函数。这种情况下，每个 Promise 都互相依赖。

有时，我们需要所有 Promise 都被 fulfilled，但它们并不相互依赖。在这种情况下，将它们全部一起启动，然后在它们全部 fulfilled 时收到通知会更有效。 JavaScript 当中，提供了 Promise.all() 这个 static method，它接受一个 promise array 并返回一个 promise。

Promise.all() 返回的 promise 是：

- fulfilled - 如果所有在 array 当中的 promises 都变成 fulfilled，则 Promise.all() 所 return 的 promise 状态会变成 fulfilled。 .then()被 JavaScript 调用时，参数是 array of responses，顺序跟 Promise.all()参数的 array of promises 的顺序相同。
- rejected – 当任一个 array 当中的 promises 变成 rejected，则 Promise.all() 所 return 的 promise 状态会变成 rejected 。此时，.catch()被 JavaScript 调用时，参数会是被 rejected 的 promises 的错误讯息。

有时，我们可能需要履行一组 Promise 中的任何一个，而不关心哪一个，那我们就需要使用 Promise.any()。只要 Promise array 中的任何一个变成 fulfilled，就执行.then()，或者如果所有 promises 都被拒绝，则执行.catch()。

```javascript
const fetchPromise1 = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json"
);
const fetchPromise2 = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/not-found"
);
const fetchPromise3 = fetch("https://fhzsdhzrfhbdz.com");

Promise.all([fetchPromise1], [fetchPromise2], [fetchPromise3])
  .then((responses) => {
    responses.forEach((response) => {
      console.log(response.url, response.status);
    });
  })
  .catch((e) => {
    console.log(e);
  });
```

# Async and Await

Async 关键字为我们提供了一种更简单的方式来处理基于 async promise 的代码：

```javascript
async function myFunction() {
  // This is an async function
}
```

在 asynchronous function 中，您可以在调用会 return promise 的函数之前使用 await 关键字。这使得代码在该点等待直到 Promise 被 fulfilled 或是 rejected。 await 关键字只能放在 async function 内部！ ！

特别注意！ ！ JavaScript 设定所有的 async function 都一定会 return 一个 Promise Object，不论我们在 async function 内 return 什么值！ ！在 async function 内部 return 的任何值，在 async function 所 return 的 Promise 变成 fulfilled 时，执行.then()的 callback function 内部自动变成参数。例如：

```javascript
async function myFunction() {
  return 10;
}
let promise = myFunction();
promise.then((data) => {
  console.log(data);
});
```

在最后一行的 data 会是 10。

特别注意，若程式码是：

```javascript
async function fetchSomething() {
  const response = await fetch(URL);
}
```

在这里，我们调用了 await fetch()，response 并不会是一个 Promise！使用了 await 关键字，我们会获得 URL 回应的完整的 Response Object，就像 fetch() 是一个同步函数(synchronous)一样！我们在 asynchronous function 内部甚至可以使用 try...catch 块进行错误处理，就像代码是同步的一样。

```javascript
async function fectchProduct() {
  const response = await fetch(
    "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json"
  );
  console.log(response);
}
fectchProduct();
```

```javascript
async function fectchProduct() {
  try {
    const response = await fetch(
      "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json"
    );
    console.log(response);
    const data = await response.json();
    console.log(data);
  } catch (e) {
    console.log(e);
  }
}
fectchProduct();
```

# Node.js Event Loop

在 Node.js 当中，将凡事有任何需要等待结果的、请求外部资源才能进行的函式，都会被放到 Event Loop 中等待。当运算结果出来了或是资源载入完成后，这些正在等待被执行的函式，都会被 Node.js 依序执行。如此一来，Node.js 可以保持忙碌且维持高效率。

> Node.js 的 Event Loop 与浏览器的 Event Loop 不尽相同。 Event Loop 的结果也跟 JavaScript 引擎的版本有关。

在认识 Event Loop 之前，先来认识一种数据结构 – Queue。 Queue 与 Stack 是两个相似但原则相反的数据结构。 Queue 是一种列队式的结构，采用先进先出(First In First Out, FIFO)为原则。 Stack 则是堆状的结构，采用后进先出为(Last In First Out, LIFO)原则。

![](https://cdn.cbd.int/xiansakana-blog-img/202311130938799.png)

在 Node.js 的 Event Loop 当中，大致可分成以下几种 Queue：

1. 优先级别：nextTick queue 以及 microTask Queue。
   - nextTick Queue – 优先程度最高的 queue。给定的 process.nextTick(callbackFn)的 callbackFn 都会被放入这个 queue 内部。
   - microTask Queue – 优先程度第二高的 queue。当 promise object 的状态，由 pending 转变为 fulfilled 或 rejected 时，.then(callbackFn)或.catch(callbackFn)所执行的 callbackFn 会被排在这个 queue。
2. 普通级别：macrotask queue (或叫做 task queue)。其中， macrotask queue 又有 timers, pending callbacks, Idle, prepare, polling, check, close callbacks 这六种。
   - timers – 当 setTimeout(callbackFn)跟 setInterval(callbackFn)所设定的时间倒数完毕时， callbackFn 会被放来这里等待执行。
   - Pending callbacks – 给作业系统做使用的 queue，例如 socket 连线时的错误，或是传输控制协定层出现错误，相关的 callback functions 会被放到这边来。
   - Idle, prepare – 给 Node.js 内部做使用的 queue，可以略过。
   - Polling – 当 I/O 有 callback function 时使用的 queue。例如，.on(‘data’, callbackFn)当中 callbackFn 就会被放入 polling。
   - Check – 给 setImmediate()的 callback functions 使用的 queue。
   - Close Callbacks – 当 socket 或是档案被关闭或是突然中断连线时，使用的关闭动作 callback 会被放在这里。

Node.js 运行程式码的顺序是：

- 将整份程式码先扫描一次。若遇到同步函式，就马上执行。
- 若遇到异步函式，则将 callback function 分配到各自归属的 queue 内部。例如， setImmediate()的 callback function 就会被放到 Check。
- 当整份程式码完成扫描后，Node.js 会重复 event loop。只要 queue 还有 callback 尚未被触发，Node.js 就会一直循环，不断循环下去。例如，setTimeout()有 callback function，但需要几秒后才触发，那这之间的时间 event loop 就会不断循环。当然，这中间的几秒也有可能有其他的 callback functions 被放入 queue。
- 循环至某个 queue 时，发现 callback 可以被执行了，就把 queue 内部的 callback 依照先进先出的原则处理。
- 如果在循环的过程中， 若 nextTick Queue 有函式可以执行，则优先将 nextTick Queue 清空。
- microtask Queue 也是同样操作，若 microtask Queue 当中有函式可以执行，则优先将 microtask Queue 清空。

![](https://cdn.cbd.int/xiansakana-blog-img/202311131004839.png)

```javascript
console.log("start");

process.nextTick(function () {
  console.log("nextTick1");
});

setTimeout(function () {
  console.log("setTimeout");
}, 0);

new Promise(function (resolve, reject) {
  console.log("promise");
  resolve("resolve");
}).then(function (result) {
  console.log("promise then");
});

(async function () {
  console.log("async");
})();

setImmediate(function () {
  console.log("setImmediate");
});

process.nextTick(function () {
  console.log("nextTick2");
});

console.log("end");

// start
// promise
// async
// end
// nextTick1
// nextTick2
// promise then
// setTimeout
// setImmediate
```

# Race Condition

在计算机科学中，进程(process)是正在执行的程式，线程(thread)是可以由程序调度员(scheduler，一个作业系统内的功能)独立管理的轻量级进程。一个 process 内部可以有多个 threads。

由于绝大多数的时间，我们电脑的许多 CPU 都是闲置的状态(因为 threads 可能会需要等待 I/O，或是可能发生 CPU 正在忙碌，其他的 CPU 却闲得发慌的情况)，因此，我们可以写出内部含有多个 threads 的程式，让 threads 被多个 CPU 并进执行，善用 CPU 资源，提高效率。这就是许多程式语言都支援的 multi-threaded programming。

当两个以上的 thread 访问一个共享资源(shared resource)时，就会发生 race condition。 Race condition 发生时，有可能造成难以预期的状况或 bug。

要避免 Race Condition 的发生，我们可以透过划分 critical region。程式当中，访问 shared resource 的部分，被称为 Critical Region 。每当我们要进去 Critical Region 之前，我们可以先把共享资源上锁。上锁期间，任何其他的 thread 都无法访问这个共享资源。离开 Critical Region 之后，再去做解锁。

> Lock 也称为 mutex (mutual exclusion lock )。在进入 Critical Region 之前，mutex 会检查我们是否可以进入。 Mutex 另一个名字是 binary semaphore 。

在 Node.js 当中，制作 mutex 的方式很简单。

```javascript
let mutex = Promise.resolve();
async function doingSomethingCritical() {
  mutex = mutex
    .then(() => {
      // ... do stuff on the critical path
    })
    .catch(() => {
      // ... manage errors on the critical path
    });
  return mutex;
}
```

```javascript
let balance = 0; // shared resource
let mutex = Promise.resolve(); // return fulfilled Promise object

const randomDelay = () => {
  // return value is a Promise
  // and the time for this promise changing from pending to fulfilled
  // is random (0s-0.1s)
  return new Promise((resolve) => setTimeout(resolve, Math.random() * 100));
};

async function loadBalance() {
  await randomDelay(); // 等個隨機的0s~0.1s
  return balance;
}

async function saveBalance(value) {
  await randomDelay();
  balance = value;
}

async function sellGrapes() {
  mutex = mutex
    .then(async () => {
      const balance = await loadBalance();
      console.log(`賣葡萄前，帳戶金額為: ${balance}`);
      const newBalance = balance + 50;
      await saveBalance(newBalance);
      console.log(`賣葡萄後，帳戶金額為: ${newBalance}`);
    })
    .catch((e) => {
      console.log(e);
    });
  return mutex;
}

async function sellOlives() {
  mutex = mutex
    .then(async () => {
      const balance = await loadBalance();
      console.log(`賣橄欖前，帳戶金額為: ${balance}`);
      const newBalance = balance + 50;
      await saveBalance(newBalance);
      console.log(`賣橄欖後，帳戶金額為: ${newBalance}`);
    })
    .catch((e) => {
      console.log(e);
    });
  return mutex;
}

async function main() {
  await Promise.all([
    sellGrapes(),
    sellOlives(),
    sellOlives(),
    sellOlives(),
    sellGrapes(),
    sellGrapes(),
    sellGrapes(),
  ]);
  const balance = await loadBalance();
  console.log(`賣葡萄與橄欖後的帳戶金額是${balance}`);
}

main();
// 卖葡萄前，帐户金额为: 0
// 卖葡萄后，帐户金额为: 50
// 卖橄榄前，帐户金额为: 50
// 卖橄榄后，帐户金额为: 100
// 卖橄榄前，帐户金额为: 100
// 卖橄榄后，帐户金额为: 150
// 卖橄榄前，帐户金额为: 150
// 卖橄榄后，帐户金额为: 200
// 卖葡萄前，帐户金额为: 200
// 卖葡萄后，帐户金额为: 250
// 卖葡萄前，帐户金额为: 250
// 卖葡萄后，帐户金额为: 300
// 卖葡萄前，帐户金额为: 300
// 卖葡萄后，帐户金额为: 350
// 卖葡萄与橄榄后的帐户金额是350
```

# Promise-Based API

API (Application Programming Interface) 的中文是应用程序编程接口。 Application 是指任何具有功能的程式， Interface(接口)可以被认为是两个程式之间的服务契约。该合约定义了两个程式之间如何相互通信。例如： 当程式甲需要程式乙帮他做某件事，或是取得某些资料的时候，程式乙会定义一套的标准或接口，告诉任何想要程式乙提供服务的对象，如何跟程式乙沟通。这套标准就是 API。

这时程式甲并不需要知道程式乙做了什么，怎么做的。程式甲只需要知道三件事:

1. API 上面要求要提供什么资料，才能向程式乙沟通？
2. 成功的话，程式乙会回复给我什么?
3. 失败的话，程式乙会回复给我什么?

API 上面会把这些情况写得明明白白。至于哪些机构或机关有提供 API 提供大家服务呢？如 Facebook、Google，或是政府机关网站（像是故宫博物院）都会有对应的 API 规格文件可以参考。

透过 API，我们可以连结到其他程式所提供的服务。例如，故宫博物院的 API ，不限用途，不用付费即可公开使用。但使用之前，需要先申请 API key。请见：
https://openapiweb.npm.gov.tw/APP_Prog/cht/overview_cht.aspx

若我们想要制作一个 API，而 API 中的 function 会 return promise object，使得调用这些 function 时，可以使用.then(), .catch()等语法，那我们就必须使用 Promise class 的 constructor。 Promise constructor 接受一个函数作为参数。我们将这个函数称为 executor。

executor 函数本身有两个参数，它们都是函数，通常称为 resolve 和 reject。如果异步函数成功，则调用 resolve，如果失败，则调用 reject 。 Resolve 以及 Reject 这两个函数的 argument 只有一个，并且可以是任何的 data type。

```javascript
const name = document.querySelector("#name");
const delay = document.querySelector("#delay");
const button = document.querySelector("#set-alarm");
const output = document.querySelector("#output");

// return Promise object
// pending的delay秒 => fulfilled
// 若delay < 0 => rejected
function alarm(person, delay) {
  return new Promise((resolve, reject) => {
    if (delay < 0) {
      reject("delay不能小于0");
    } else {
      setTimeout(() => {
        resolve(person + "起床!!");
      }, delay);
    }
  });
}

button.addEventListener("click", async () => {
  try {
    let result = await alarm(name.value, delay.value);
    output.innerHTML = result;
  } catch (e) {
    output.innerHTML = e;
  }
});
```

连接到外部 API

```javascript
let myKey = "8534657fc1c5c6e9b5fd87c3a02eed17";
let city = "New York";
let url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${myKey}`;

async function weather() {
  try {
    let result = await fetch(url);
    let data = await result.json;
    console.log(data);
  } catch (e) {
    console.log(e);
  }
}
weather();
```
