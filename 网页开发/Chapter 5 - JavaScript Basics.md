### 常见JavaScript函数
- [console.log()](https://developer.mozilla.org/zh-CN/docs/Web/API/console/log): 向 Web 控制台输出一条信息。这条信息可能是单个字符串（包括可选的替代字符串），也可能是一个或多个对象。
- [window.alert()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/alert): 令浏览器显示一个带有可选的信息的对话框，并等待用户离开该对话框。
- [window.prompt()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/prompt): 指示浏览器显示一个对话框，其中有一个可选的信息，提示用户输入一些文本，并等待用户提交文本或取消对话框。
```js
let user_name = window.prompt("input your name:");
window.alert("welcome " + user_name);
```

### Lexical Structure
1. Case Sensitive: JavaScript中大小写敏感。
2. 空白键、换行键等等在JavaScript中会全部被忽略。
3. 当行注释//，多行在`/**/`内部。
4. 变量开头可以为文字、underscore(\_) 、dollar sign($)，不能为数字。
5. 内部有关键字(reserved words, keywords)，例如：null, of, if, then, in, finally, for, while, break, continue, switch, try, let, const, var等等，不能作为变量名称。
6. 使用Unicode字元集合，所以String内部可由任何Unicode文字组成。
7. Semicolons(;)可用来分隔语句， Semicolons的使用是optional。

### 变量与赋值
- 声明变量(Declare Variable) 
1. 若值变化，用let
2. 若值不变，用const
3. 请勿用var
>注意：
>1. 用const来声明变量，需要马上赋予初始值(initializer)。let则不需要，若用let宣告了变量，但还没有赋值，则变量的值是undefined。
>2. 