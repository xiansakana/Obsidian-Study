## vscode扩展

- live server（注意要信任工作区）
- Prettier - Code formatter （设置中搜索Format On Save，然后勾选Editor: Format On Save；搜索Default Formatter，然后选择Prettier- Code formatter）
- Auto Rename Tag
- Code Runner

## 基本语法

- [`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)anchor tag可以设定target属性
```html
<a href="" target="_blank"></a>
```

- [`<base>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/base)可以设定所有`<a>`标签的target
```html
<base target="_blank" /> 
```

- [`<img>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img)插入图像，`<src>`图像来源，`<alt>`图像无法显示时替代文字
```html
<img src="" alt="" />
```

- [`<ul>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ul)是unordered list

- [`<ol>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol)是ordered list，可设置编号类型type属性
	- `a` 表示小写英文字母编号
	- `A` 表示大写英文字母编号
	- `i` 表示小写罗马数字编号
	- `I` 表示大写罗马数字编号
```html
<ol type=""></ol>
```

- block elements: `<p>` `<div>` 
	不会嵌套在inline elements中，但是可能嵌套在其他block elements中。
	块级元素总是从新行开始，浏览器会自动在元素前后添加一些空格（边距）块级元素始终占据可用的全部宽度（尽可能向左和向右延伸）。

- inline elements: `<a>` `<span>`
	放在block elements中的内容。
	内联元素不会从新行开始，内联元素仅占用必要的宽度。

## [表格Table](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/table)

`<table>` `<tr>` `<th>` `<td>` `<th>` `<thead>` `<tbody>`
`<colspan>` `<rowspan>`: 合并表格项

```html
<table>
  <thead>
	<tr>
	  <th colspan="3">國立故宮博物院資訊</th>
	</tr>
	<tr>
	  <th>所屬部門</th>
	  <th>員額</th>
	  <th>授權法源</th>
	</tr>
  </thead>
  <tbody>
	<tr>
	  <td>行政院</td>
	  <td>502人</td>
	  <td>《行政院組織法》、《國立故宮博物院組織法》</td>
	</tr>
  </tbody>
</table>
```

## [表单Form](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form)

```html
<form action="">
  <label for="名字">姓名</label>
  <input id="名字" type="text" name="姓名" />
  <button type="submit">提交表单</button>
</form>
```

```html
<form action="" method="POST">
  <label for="email">账号：</label>
  <input id="email" type="text" name="email" />
  <label for="password">密码：</label>
  <input id="password" type="password" name="password" />
  <button type="submit">登陆</button>
</form>
```
### method属性

- [GET](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods/GET)：表单数据会附加在 `action` 属性的 URL 中，并以 '?' 作为分隔符，[没有副作用](https://developer.mozilla.org/zh-CN/docs/Glossary/Idempotent) 时使用这个方法。
- [POST](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods/POST)：用来隐藏信息，表单数据会包含在表单体内然后发送给服务器。

- [`<input>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input)标签的type属性有[`checkbox`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/checkbox) [`email`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/email) [`file`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/file) [`number`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/number) [`password`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/password) [`radio`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/radio) [`range`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/range)。其他属性有`checked` `max` `min` `maxlength` `minlength` `placeholder` `required` `value` `step` 等等。
	- checkbox--方框打勾，checked --默认勾选
	- number--输入数字，value--默认值，max和min--设置上限和下限，step--分度
	- minlength--最短长度，maxlength--最长长度
	- placeholder--输入提示符
	- range--滑杆
	- radio--多选一
	- required--必须选择
- [`<button>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/button)在`<form>`标签内预设type是`<submit>`

```html
<form action="">
      <label for="名字">姓名</label>
      <input
        id="名字"
        type="text"
        name="name"
        minlength="5"
        maxlength="50"
        placeholder="请输入您的姓名"
        required
      />
      <input id="male" type="radio" name="gender" value="male" required />
      <label for="male">男性</label>
      <input id="female" type="radio" name="gender" value="female" />
      <label for="female">女性</label>
      <input id="other" type="radio" name="gender" value="other" />
      <label for="other">其他</label>  
      <label for="gender">性别</label>
      <label for="邮箱">邮箱</label>
      <input id="邮箱" type="email" name="email" required />
      <label for="密码">密码</label>
      <input
        id="密码"
        type="password"
        name="password"
        minlength="8"
        maxlength="40"
        required
      />
      <label for="年龄">年龄</label>
      <input
        id="年龄"
        type="number"
        name="age"
        value="18"
        min="0"
        max="125"
        step="1"
        required
      />
      <label for="SSR">SSR订阅</label>
      <input id="SSR" type="checkbox" checked name="SSR" value="订阅" />
      <label for="地区">地区</label>
      <input id="地区" type="text" name="area" list="area-list" required />
      <datalist id="area-list">
        <option value="北京市">北京市</option>
        <option value="上海市">上海市</option>
        <option value="天津市">天津市</option>
        <option value="深圳市">深圳市</option>
        <option value="重庆市">重庆市</option>
      </datalist>
      <button type="submit">提交</button>
    </form>
```

- 关于[`select`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/select) [`option`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/option) 选择器
```html
      <label for="gender">性别</label>
      <select name="gender" id="gender" required>
        <option value=""></option>
        <option value="male">男性</option>
        <option value="female">女性</option>
        <option value="other">其他</option>
      </select>
```

- 关于[datalist](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/datalist)数据列表
```html
      <label for="地区">地区</label>
      <input id="地区" type="text" name="area" list="area-list" required />
      <datalist id="area-list">
        <option value="北京市">北京市</option>
        <option value="上海市">上海市</option>
        <option value="天津市">天津市</option>
        <option value="深圳市">深圳市</option>
        <option value="重庆市">重庆市</option>
      </datalist>
```

- 关于[textarea](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/textarea)文本区
```html
      <label for="suggestion">给网站的建议</label>
      <textarea
        name="suggestion"
        id="suggestion"
        cols="30"
        rows="10"
        placeholder="请填写给网站的建议"
      ></textarea>
```

## 其他

- [`<br />`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br) break换行
- [`<hr />`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/hr) 主题分割（水平分割线）
- `favicon` 
```html
<link rel="icon" href="./favicon.ico">
```

