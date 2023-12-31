### 常见JavaScript函数

- [console.log()](https://developer.mozilla.org/zh-CN/docs/Web/API/console/log): 向 Web 控制台输出一条信息。这条信息可能是单个字符串（包括可选的替代字符串），也可能是一个或多个对象。
- [window.alert()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/alert): 令浏览器显示一个带有可选的信息的对话框，并等待用户离开该对话框。
- [window.prompt()](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/prompt): 指示浏览器显示一个对话框，其中有一个可选的信息，提示用户输入一些文本，并等待用户提交文本或取消对话框。
```javascript
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

#### 声明变量（Declare Variable）

1. 若值变化，用let。
2. 若值不变，用const。
3. 请勿用var。
>注意：
>1. 用const来声明变量，需要马上赋予初始值(initializer)。let则不需要，若用let宣告了变量，但还没有赋值，则变量的值是undefined。
>2. 用const和let声明的变量，不能重复声明(redeclaration)。
>3. const不能重复赋值(reassignment)。

|   |redeclareation|reassignment|initializer|
|:-:|:-:|:-:|:-:|
|let|&#10003;|&#10003;|不需要|
|const|&#10005;|&#10003;|需要|

### 数据类型（Data Type）

1. Number - 整数和带小数点的数字。
2. BigInt - 任意长度的整数。
3. String - 字符串。
4. Boolean - true或false两种值
5. null - 用来代表某个不存在的值
6. undefined - 未被赋值的变量

> 除了这些数据类型之外，JavaScript还有种叫做object，属于non-primitive data type，object可能是array或是function等等。

#### [Number](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number)

范围：-9,007,199,254,740,992 (-2^253^) 和 9,007,199,254,740,992 (2^253^) 之间的所有整数。

运算符号包含加法、减法、乘法 、除法、remainder operator、exponentiation operator、++、--、 +=、-=、/=、*= 等等。 

#### [String](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String)

- String是由字母或数字串接组成的。String需要使用单引号或双引号。两个String之间的串接是由符号“+”所完成的。String之间的串接被称为concatenation。String与String之间不能做“-”、 “*”、 “/”运算。若尝试做此类运算，则会出现NaN，代表Not a Number。(这是因为，JavaScript还是会尝试算出某个数字结果，但两个operand的值都不是数字，无法算出一个数字结果，所以会出现NaN。)

- String与Number之间，若是做“+”运算，则会变成String与String之间的concatenation。\n可以换行。

#### Number Methods

JavaScript是个面向对象的程序语言，所以JavaScript当中的数字可被视为是对象。以下是数字常见可用的methods：

- [toString()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/toString) – return一个数字的String。
- [toFixed(n)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) – return被转换后的数字，到小数点后第n位数。

> 注意！ 二进制不能精确表示所有小数。 这可能会导致意外结果，例如 0.1 + 0.2 === 0.3 会return false 。

#### String Attributes and Methods

JavaScript中的String有可用的attributes以及methods。常见的有：

- [length](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/length) – return String的长度。
- [n] – return index 第n项的字母。(index从0开始计算)
- [slice(indexStart, indexEnd)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/slice) - 提取字符串的一部分并将其作为新String返回，而不修改原始字符串。 indexStart是inclusive, indexEnd是optional, exclusive。
- [indexOf(substring)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf) – return substring 的index位置。若找不到substring，则return -1。
- [toUpperCase()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)  - return转换为大写的String。 此方法不会影响String本身。
- [toLowerCase()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase) - return转换为小写的String。 此方法不会影响String本身。
- [split(pattern)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/split) - 接受一个pattern并通过搜索将一个字符串分成一个有序的array，然后return该array。 Pattern可以是regular expression。
- [startsWith(s)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith) – 确定String是否以指定字串s开头，根据需要返回 true 或 false。
- [endsWith(s)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith) – 与startsWith()相同，但确认结尾。
- [includes(str)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/includes) – return true如果String内部包含str。
- [charCodeAt(n)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt) - 返回一个介于 0 和 65535 之间的整数，表示给定索引处n的 UTF-16 code unit。

#### [Boolean](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Boolean)

- 在JavaScript当中，Boolean代表两个值之一：true或false。
- Unary operator “!”可以将Boolean的值反转。
- Unary operator "typeof" 可以用来确认类型。

#### Undefined and Null

- [undefined](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/undefined) - 已经声明变量，却没有赋予initializer时，就会出现undefined。undefined也是JavaScript中的functions的预设return value。
- [null](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/null) – 用来代表某个故意不存在的值。

### [JavaScript Operators](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators)

- assignment operator

- comparison operator

  JavaScript当中 comparison operators 的运算元是两个任意数据类型，且运算结果为Boolean值。

  - == returns true if the operands are equal.
  - != returns true if the operands are not equal.
  - === returns true if the operands are equal and of the same data type. 
  - !== returns true if the operands are of the same type but not equal, or are of different type.
  - \> returns true if the left operand is greater than the right operand.
  - \>= returns true if the left operand is greater than or equal to the right operand.
  - < returns true if the left operand is less than the right operand.
  - <= returns true if the left operand is less than or equal to the right operand.

- logical operator

  |   A   |   B   | A && B | A &#124;&#124; B |
  | :---: | :---: | :----: | :--------------: |
  | true  | true  |  true  |       true       |
  | true  | false | false  |       true       |
  | false | true  | false  |       true       |
  | false | false | false  |      false       |

  > - &&: If the left hand side is true, then it evaluates as the right hand side; If the left hand isde is not true, then it ecaluates as the left hand side.
  > - ||: If the left hand side can be converted to true, then returns left hand side; else, return right hand side.

- typeof operator (unary)

- negation operator (unary)

- increment operator (unary)

- bitwise operator

  JavaScript中的Bitwise Operators将数字operand视为32 bits的数字，并且对每个bit进行运算。

  - a & b - 在两个operand的对应位都是 1 的位置返回一个 1。
  - a | b - 在两个operand的对应位都是0的位置返回一个0。
  - a ^ b – 在两个operand的对应位相同的每个位置返回0。(XOR运算)
  - ~a – 反转operand的每个bit。
  - a << b - 将二进制表示中的 a 向左移动 b 位，丢弃任何被移出的bits。
  - a >> b -将二进制表示中的 a 向右移动 b 位，丢弃任何被移出的bits。

  何时会用到 Bitwise Operators？以下为几种范例：

  - 做编码运算
  - 资料传出，sockets programming, ports
  - 资料加密、SHA函数
  - 作业系统、CPU
  - Finite State Machine
  - Graphics，例如影像处理、人工智能

- arithmetic operator

### if statement

```javascript
if (condition) statement1;

if (condition) {
  statement1;
} else {
  statement2;
}

if(condition1){
    statement1;
}else if(condition2){
    statement2;
}else{
    statement3
}
```

### [Truthy](https://developer.mozilla.org/zh-CN/docs/Glossary/Truthy) and [Falsy](https://developer.mozilla.org/zh-CN/docs/Glossary/Falsy) Values

Falsy Values包括：

- false
- 0, -0, 0n (BitInt)
- “”, ‘’, `` (所有的empty string)
- null
- undefined
- NaN

> 除此之外的都是truthy values，包含[] empty array, {} empty object等等。

### Coding Convention and Restrictions

#### Conventions:

- 变量与函数的名称，全部小写。若名称由两个以上的单字组成，则使用camelCase。(或也可使用underline)
- Operators 周围加上空格。
- 用分号结束一个简单的statement。
- Constants全部使用大写。
- Class由大写字母开头。

#### Restrictions:

- 变量、函数名称不可由数字开头。
- 变量、函数名称不可包含hyphen。 Hyphen已经预留给数字做减法运算。
- 变量、函数名称不可使用reserved words。

