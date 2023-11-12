## Ajax

AJAX即「Asynchronous JavaScript and XML」(非同步的JavaScript与XML技术)，指的是一套综合了多项技术的浏览器端网页开发技术。

 AJAX在客户端使用各种 Web 技术来创建异步(asynchronous) Web 应用程序。应用程序可以在背景从服务器发送和获得数据，而不干扰现有页面的显示和行为。通过将数据交换层与表示层分离，Ajax 允许网页以及扩展的 Web 应用程序动态地更改内容，而无需重新加载整个页面。在实践中，数据的传送通常使用 JSON 而不是 XML。

 常见的Ajax应用的例子是，我们在YouTube或是Google搜寻时，网站会根据我们前面打的几个字，猜想我们想要搜寻的关键字是什么。这就是不干扰现有页面的显示和行为的情况下，从服务器发送和获得数据，并且更新网页的方法。

![](https://img.xiansakana.xyz/202311112120918.png)

## 同步与异步

在计算机程式中，异步(asynchronous)代表着一个process独立于其他 process运行，而同步(synchronous)代表着一个process仅在某个其他process完成或移交后而运行。

![](https://img.xiansakana.xyz/202311112122765.png)

通常来说，JavaScript的特性是single-threaded synchronous，代表JavaScript是个一次只会做一件事情的程式语言。然而，JS有内建的asynchronous function，例如setTimeout()。 setTimeout() funtion设置一个计时器，一旦计时器时间到，该计时器就会执行一个函数或指定的一段代码。 setTimeout()的语法为：
```javascript
setTimeout(code, delay)
```

Code是delay结束时要执行的程式码，delay 是在执行指定的函数或代码之前计时器应等待的时间（以毫秒为单位）。如果省略此参数，则使用值 0，表示“立即”执行。

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

## Promise

Promise 是现代 JavaScript 中异步编程的基础。 Promise 是一个由asynchronous function所return的对象，主要功能是，Promise 会代理一个建立时不用预先得知结果的值。

Promise使我们能够系结着发动非同步操作后，最终的成功值(success value)或失败讯息(failure reason)的处理函式（handlers）。我们向服务器传送request之后，因为需要等待response的时间，所以我们会先得到一个Promise，而这个Promise目前的状态是「搁置」(pending)。

一个 Promise 对象有处于以下三种状态：

1. 搁置 (pending)：初始状态，并不是 fulfilled 与 rejected。
2. 实现 (fulfilled)：表示操作成功地完成。
3. 拒绝 (rejected)：表示操作失败了。

Promise在pending后的几秒之内，状态可能变成fulfilled或是rejected。一个处于搁置(pending)状态的 Promise ，若操作成功，能够将状态变成fulfilled，或是因为某些原因或错误而被操作失败，变成拒绝(rejected)状态。当上述任一状态转换发生时，那些透过 then 方法所系结的callback就会被调用。

例如：
```javascript
let promiseObject = fetch(URL);
promiseObject.then((data) => {    
    console.log(data);
})
```

这段程式码中，当promiseObject从pending变成fulfilled之后，.then()内部的callback function就会被JavaScript自动执行。执行时，带入的参数就是从URL获得的HTTP Response内容。

![](https://img.xiansakana.xyz/202311112143059.png)

![](https://img.xiansakana.xyz/202311112146306.png)

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

## Catching Errors

为了支持错误处理，Promise 物件提供了一个 catch() 方法，跟then()很像。我们调用.catch()时，传入一个callback function当作参数。传递给 catch() 的处理函数在异步操作失败时自动被JavaScript调用。 catch()内部的callback function被调用时，参数会被放入错误讯息，通常以变数e或是err代表错误(error)。

当串连多个.then语句时，后一个.then()内部的callback function被执行时，所用的参数是前一个.then()中的callback function所回传的值。

如果将 catch() 添加到 Promise Chain的末尾，那么当任何异步函数调用失败时都会调用它。

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

