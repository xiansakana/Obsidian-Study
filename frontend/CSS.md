---
title: CSS
tags:
  - CSS
  - 前端
categories: 学习
cover: https://cdn.cbd.int/xiansakana-blog-img/202310190107034.png
abbrlink: d54bd6b
date: 2023-10-19 01:24:41
---

# 基本概念

- [DOM](https://developer.mozilla.org/zh-CN/docs/Glossary/DOM) Tree (Document Object Model)：加载到浏览器中的网页的树状表示。浏览器加载网页时，会创建该页面的 DOM Tree。
- [CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) (Cascading Style Sheet)：用来设定网页的样式和布局。Comment 语法为`/**/`。

## 基本语法

## 放置位置

- inline styling（优先级最高，但只能特定标签）

```html
<h1 style="color: red;">< /h1></h1>
```

- [flex-wrap](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-wrap)(自动换行)

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

## 颜色设定

- Color Keywords([named-color](https://developer.mozilla.org/zh-CN/docs/Web/CSS/named-color)): red, black, purple, green, coral 等。
- [rgb](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value/rgb): 红绿蓝 0-255
- rgba: a 表示 alpha，用来储存透明度（0,1）
- [hex-color](https://developer.mozilla.org/zh-CN/docs/Web/CSS/hex-color)
- [HSL](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value/hsl): 色相 Hue，饱和度 Saturation，亮度 Lightness

## CSS Selectors 选择器

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

[`:nth-child()`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-child): 用于选择第 n 个元素

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

## CSS 概念

### Inheritance

- Parents and Children

- [Inherited and Non-Inherited Properties](https://www.w3.org/TR/CSS21/propidx.html)
  Inherited: color, font-family, font-size, font-weight, list-style-type, text-align...

  > user styling: Program Setting
  > user agent styling: Browser Default (优先度可能大于 inheritance，比如`<a>`颜色通常需要额外设定)

### Conflicting Styling

- 单个或者多个 Stylesheet 重复设定
- 处理原则：Priority, Specificity, Order Rule。

### Priority

1. Inline Styling
2. User Stylesheet (内部顺序由 Specificity 决定)
3. User Agent Stylesheet
4. Inheritance

### Specificities

1. id - specificity (1, 0, 0)
2. class - specificity (0, 1, 0)
3. tag - specificity (0, 0, 1)

> Order Rule:
> Specificity 相同时，后面样式覆盖前面；后面`<link>stylesheet`覆盖前面。

## CSS 单位

- absolute units: px, in, mm, cm 等
- relative units

**reletive units**

1. em: 相对于 parent element 的长度
2. rem (root em): 浏览器预设（一般 16px）
3. vw (viewport width): 浏览器视窗宽度的 1/100，但 100vw 通常会略宽于网页宽度
4. vh (viewport height): 浏览器视窗高度的 1/100
5. %: 相对于 parent element 的值

## 文字样式

- [font-size](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size)
- [text-align](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-align): right, left, center
- [text-decoration](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration): underline, line-through, none
- [line-height](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height)
- [letter-spacing](https://developer.mozilla.org/zh-CN/docs/Web/CSS/letter-spacing)
- [font-family](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-family)
- [text-indent](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-indent)
- [font-weight](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-weight): normal, bold, lighter, bolder

## 背景样式

- [background-color](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color)
- [background-image](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image)
- [background-size](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-size): content (平铺), cover (等比缩放不留空白)
- [background-position](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-position): top, left, right, bottom, center
- [background](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background)

## Box Model

![](https://cdn.cbd.int/xiansakana-blog-img/202310182246305.png)

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

> padding、 border 以及 margin 都可再分别设置上下左右的属性。另外，border 可设置[border-radius](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-radius)（圆角外框）。

- [overflow](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow): visible, hidden, scroll

- [box-sizing](https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-sizing):
  - border-box: 设置的边框和内边距的值是包含在 width 内，内容区的实际宽度是 width 减去 (border + padding) 的值
  - content-box: 默认值，元素的内容区的宽度就是 width

## [Display](https://developer.mozilla.org/en-US/docs/Web/CSS/display)属性

### Outer dispaly type

- block
- inline
- inline-block

### Inner display type

- flex
- grid

| display type | new line | width, height |       上下 margin, padding        | 左右 margin, padding |                             范例                             |
| :----------: | -------- | :-----------: | :-------------------------------: | :------------------: | :----------------------------------------------------------: |
|    block     | 会换行   |   可以设定    |             可以设定              |       可以设定       |                      `<h1>`, `<p>`等等                       |
|    inline    | 不换行   |   不能设定    | 可以设定，但不会推开其他 elements |       可以设定       |                     `<a>`, `<span>`等等                      |
| inline-block | 不换行   |   可以设定    |             可以设定              |       可以设定       | 只有`<img>`, `<button>`, `<input>`, `<select>`, `<textarea>` |
|  flex item   | 不换行   |   可以设定    |             可以设定              |       可以设定       |                  任何在 flex 之下的 element                  |

## [Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)属性

- static: 预设值，`top`, `right`, `bottom`, `left`  和  `z-index`  属性无效。
- relative: 根据 normal flow 进行定位
- absolute: 从 normal flow 中移除，定位参考为 ancestor（若无则为浏览器视窗）
- fixed: 从 normal flow 中移除，定位参考为 inital containing block
- sticky: 从 relative 超过 threshold 后变成 fixed

[Stacking Context](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_positioned_layout/Understanding_z-index)

> z-index

## 表格样式

- [border-collapse](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-collapse): collapse, seperate（边框合并或者分开）
- [overflow-x](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow-x): visible, hidden, clip, scroll, auto（设置滚动条或溢出内容）

## Opacity（不透明度）和 Cursor

- [opacity](https://developer.mozilla.org/zh-CN/docs/Web/CSS/opacity)
- [cursor](https://developer.mozilla.org/zh-CN/docs/Web/CSS/cursor): help, wait, crosshair, not-allowed, zoom-in, grab...

## [Transition](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition)

- property name | duration | [easy function](https://easings.net/)

```css
h1 {
  transition: all 2s ease-in-out;
}

h1:hover {
  background-color: green;
  color: white;
}
```

## [Transform](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform)

- translate(-50%, -50%)
- rotate(180deg)
- scale

```css
h2:hover {
  transform: translate((-50%, -50%);
  transform: rotate(180deg);
  transform: scale(0.5);
}
```

## [CSS Animation](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation)

- animation-name
- animation-duration
- animation-timing-function
- animation-delay
- animation-iteration-count
- animation-direction, animation-fill-mode, animation-play-state

```css
h2 {
  background-color: green;
  /* animation-name: changeColor;
  animation-duration: 1s;
  transition: ease-in;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  animation-fill-mode: forwards; */
  animation: changeColor 1s ease-in 0s infinite alternate forwards;
}

@keyframes changeColor {
  from {
    background-color: green;
  }
  to {
    background-color: red;
  }
}
```
