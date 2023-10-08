### 常见JavaScript函数
- [console.log()](https://developer.mozilla.org/zh-CN/docs/Web/API/console/log): 向 Web 控制台输出一条信息。这条信息可能是单个字符串（包括可选的替代字符串），也可能是一个或多个对象。
- [window.alert()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/alert): 令浏览器显示一个带有可选的信息的对话框，并等待用户离开该对话框。
- [window.prompt()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/prompt): 指示浏览器显示一个对话框，其中有一个可选的信息，提示用户输入一些文本，并等待用户提交文本或取消对话框。
```js
let user_name = window.prompt("input your name:");
window.alert("welcome " + user_name);
```

### Lexical Structure
1. Case Sensitive: JavaScript中大小写敏感
2. 1
3. 当行注释//，多行在`/**/`内部