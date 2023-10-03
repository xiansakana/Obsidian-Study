- [DOM](https://developer.mozilla.org/zh-CN/docs/Glossary/DOM) Tree (Document Object Model)：加载到浏览器中的网页的树状表示。浏览器加载网页时，会创建该页面的DOM Tree。
- [CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) (Cascading Style Sheet)：用来设定网页的样式和布局。Comment语法为`/**/`。

## 基本语法

### 放置位置

- inline styling（优先级最高，但只能特定标签）
```html
<h1 style="color: red;">< /h1>
```

- internal styling（方便撰写，但不适用于多个页面）
```html
<head>
    <style>
        h1{
            color: red;
        }
    </style>
</head>
```

- external styling（外部`style.css`文件，最常见，方便维护）
```html
<link rel="stylesheet" href="./style.css" />
```

```css
h1 {
  color: red;
}
```

### 颜色设定

- Color Keywords([named-color](https://developer.mozilla.org/zh-CN/docs/Web/CSS/named-color)): red, black, purple, green, coral等。
- [rgb](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value/rgb): 红绿蓝0-255
- rgba: a表示alpha，用来储存透明度（0,1）
- [hex-color](https://developer.mozilla.org/zh-CN/docs/Web/CSS/hex-color)
- [HSL](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value/hsl): 色相Hue，饱和度Saturation，亮度Lightness

### CSS Selectors 选择器

- Universal Selector (`*`)
```css
* {
  color: red;
}
```

- Element Selector
```css
h2 {
    color: red;
}
```

- Id Selector （唯一）
```html
<p id="first-paragraph"></p>
```

```css
#first-paragraph{
    color: rgb(66, 128, 194);
}
```

- Class Selector（可重复）
```html
<p class="blue-text" "large-text"></p>
```

```css
.blue-text{
    color: blue;
}

.large-text {
  font-size: large;
}
```

- Element Selector & Class Selector
```html
<a class="large-text" href=""></a>
```

```css
a.large-text {
  font-size: 32px;
}
```

- Grouping Selector
```css
h1,
h2,
h3 {
  color: red;
}
```

- Descendant Selector
```html
<div class="link1">
  <a href="https://www.google.com">Google首页</a>
  <a href="https://www.baidu.com">Baidu首页</a>
</div>
```

```css
div.link1 a {
  color: red;
}
```

- Attribute Selector
```html
<input type="text" />
```

```css
input[type="text"] {
  color: red;
}
```

- [Pseudo-class](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-classes) Selector
[`:hover`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:hover): 鼠标悬停
[`:active`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:active): 鼠标按住
[`:focus`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:focus): 点击选择
```css
input[type="text"]:active {
  color: lightgreen;
}

input[type="text"]:hover {
  color: lightgreen;
}
```

[`:nth-child()`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-child): 用于选择第n个元素

- Pseudo-element Selector
[`::first-line`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::first-line): 更改段落第一行的样式
```css
p::first-line {
  font-size: 32px;
}
```

[::selection](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::selection): 鼠标选择的部分
```css
*::selection{
  background-color: green;
}
```

### CSS概念

#### Inheritance
- Parents and Children
- [Inherited and Non-Inherited Properties](https://www.w3.org/TR/CSS21/propidx.html)
	Inherited: color, font-family, font-size, font-weight, list-style-type, text-align...
	>user styling: Program Setting
	>user agent styling: Browser Default (优先度可能大于inheritance，比如`<a>`颜色通常需要额外设定)
	
#### Conflicting Styling
- 单个或者多个Stylesheet重复设定
- 处理原则：Priority, Specificity, Order Rule。

#### Priority:
1. Inline Styling
2. User Stylesheet (内部顺序由Specificity决定)
3. User Agent Stylesheet
4. Inheritance

#### Specificities
1. id - specificity (1, 0, 0)
2. class - specificity (0, 1, 0)
3. tag - specificity (0, 0, 1)
> Order Rule:
> Specificity相同时，后面样式覆盖前面；后面`<link>stylesheet`覆盖前面。

### CSS单位
- absolute units: px, in, mm, cm等
- relative units

**reletive units**
1. em: 相对于parent element的长度
2. rem (root em): 浏览器预设（一般16px）
3. vw (viewport width): 浏览器视窗宽度的1/100，但100vw通常会略宽于网页宽度
4. vh (viewport height): 浏览器视窗高度的1/100
5. %: 相对于parent element的值

### 文字样式
- [font-size](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size)
- [text-align](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-align): right, left, center
- [text-decoration](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration): underline, line-through, none
- [line-height](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height)
- [letter-spacing](https://developer.mozilla.org/zh-CN/docs/Web/CSS/letter-spacing)
- [font-family](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-family)
- [text-indent](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-indent)
- [font-weight](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-weight): normal, bold, lighter, bolder

### 背景样式
- [background-color](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color)
- [background-image](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image)
- [background-size](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-size): content (平铺), cover (等比缩放不留空白)
- [background-position](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-position): top, left, right, bottom, center
- [background](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background)

### Box Model
- [margin](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin)
```css
/* 应用于所有边 */
margin: 1em;
margin: -3px;
/* 上边下边 | 左边右边 */
margin: 5% auto;
/* 上边 | 左边右边 | 下边 */
margin: 1em auto 2em;
/* 上边 | 右边 | 下边 | 左边 */
margin: 2px 1em 0 auto;
/* 全局值 */
margin: inherit;
margin: initial;
margin: unset;
```

- [border](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border)
```css
/* style */
border: solid;
/* width | style */
border: 2px dotted;
/* style | color */
border: outset #f33;
/* width | style | color */
border: medium dashed green;
/* Global values */
border: inherit;
border: initial;
border: unset;
```

- [padding](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding)
```css
/* 应用于所有边 */
padding: 1em;
/* 上边下边 | 左边右边 */
padding: 5% 10%;
/* 上边 | 左边右边 | 下边 */
padding: 1em 2em 2em;
/* 上边 | 右边 | 下边 | 左边 */
padding: 5px 1em 0 2em;
/* 全局值 */
padding: inherit;
padding: initial;
padding: unset;
```

- [content](https://developer.mozilla.org/zh-CN/docs/Web/CSS/content)

>padding、 border以及margin都可再分别设置上下左右的属性。另外，border可设置[border-radius](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-radius)（圆角外框）。

- 






