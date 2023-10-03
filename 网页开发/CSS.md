- [DOM](https://developer.mozilla.org/zh-CN/docs/Glossary/DOM) Tree (Document Object Model)：加载到浏览器中的网页的树状表示。浏览器加载网页时，会创建该页面的DOM Tree。
- [CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) (Cascading Style Sheet)：用来设定网页的样式和布局。Comment语法为/**/。

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

