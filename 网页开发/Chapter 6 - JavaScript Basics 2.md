## Function 函数

declare function:

```javascript
function name([param]){
    statemets
}
```

> JavaScript Function中，若没有 return 语句的话，function将返回undefined（这是JavaScript 的function默认的return value）。要返回默认值以外的值，函数必须具有指定要返回的值的 return 语句。return 语句结束函式执行并指定要返回给函数调用者的值。任何放在return语句底下的程式码都不会被执行。
>
> 每个 JavaScript 函数实际上都是一个对象。（代表每个function有instance properties以及instance methods）

## Array

Array具有以下核心特征：

- JavaScript Array是可调整大小的，并且可以包含不同资料类型的混合。

- JavaScript Array中的元素必须使用非负整数作为index来访问。

- JavaScript Array的第一个元素在index 0 处，第二个在index 1 处，依此类推。最后一个元素在Array的长度减 1 处。

- JavaScript Array复制会复制reference。

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

常见的Array Instance Methods：

- [push(element)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/push) - 将一个或多个元素添加到数组的末尾，并return数组的新长度。
- [pop()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) - 从数组中删除最后一个元素并返回该元素。
- [shift()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/shift) - 从数组中删除第一个元素并返回删除的元素。
- [unshift(element)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) - 将一个或多个元素添加到数组的开头，并return数组的新长度。

> 当Array内部的元素还有Array时，就被称为是array of arrays。