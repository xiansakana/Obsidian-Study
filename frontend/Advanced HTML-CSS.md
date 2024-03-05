---
title: Advanced HTML, CSS
tags:
  - CSS
  - HTML
  - 前端
categories: 前端
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310200418702.png
abbrlink: e4f80284
date: 2023-10-20 04:13:38
---

# [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

## [Flex Container](https://developer.mozilla.org/zh-CN/docs/Glossary/Flex_Container)

## [flex-direcction](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-direction)

- row: 横向
- column: 纵向
- row-reverse: 横向反向
- column-reverse: 纵向反向

## [flex-wrap](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-wrap)(自动换行)

- nowrap (默认)
- wrap
- wrap-reverse

## [justify-content](https://developer.mozilla.org/zh-CN/docs/Web/CSS/justify-content)

> 浏览器如何沿着弹性容器的[主轴](https://developer.mozilla.org/zh-CN/docs/Glossary/Main_Axis)和网格容器的行向轴分配内容元素之间和周围的空间。

- flex-start (默认)
- flex-end
- center
- space-between
- space-around
- space-evenly
  ![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182250583.png)

## [align-items](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-items)

> 控制在 cross axis (与 main axis 垂直)上的对齐方式。

- stretch (默认)
- flex-start
- flex-end
- center
- baseline
  ![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182251350.png)

## [align-content](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-content)

- normal (默认)
- stretch
- flex-start
- flex-end
- center
- space-between
- space-around
- space-evenly
  ![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310182251312.png)

## [Flex Item](https://developer.mozilla.org/zh-CN/docs/Glossary/Flex_Item)

- [flex-grow](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-grow): 将 flex container 中的剩余空间(remaining space)分配给 flex items
- [flex-shrink](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-shrink): 定义了 flex item 在必要时收缩的能力
- [flex-basis](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-basis): 指定了 flex item 在主轴方向上的初始大小

> flex 可以一次设置 grow, shrink, basis

```css
flex: 1 1 100px;
```

- [align-self](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-self): 单个 flex item 设置对齐方式

# [Media Query](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@media)

```css
@media screen and (max-width: 800px) {
  h1 {
    background-color: red;
  }
}
```

# [Bootstrap](https://getbootstrap.com/)

## User Snippet

[snippet-generator](https://snippet-generator.app/)

## Bookmark

```html
<a href="#id"></a>
```

```css
html {
  scroll-behavior: smooth;
}
```

## [@font-face](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@font-face)

```css
@font-face{
  font-family: "myFont";
  src:url("./font.ttf")
}
```

## [Sass (Syntactically Awesome Stylesheets)](https://sass-lang.com/)

> 一种将 CSS 视为程序语言的网页开发技术

Extension: Live Sass Compiler

- Nested CSS()

```scss
header {
  nav {
    ul {
      display: flex;
      flex-wrap: wrap;
      li {
        list-style-type: none;
        a {
          color: red;
          text-decoration: none;
        }
      }
    }
  }
}
```

```css
header nav ul {
  display: flex;
  flex-wrap: wrap;
}
header nav ul li {
  list-style-type: none;
}
header nav ul li a {
  color: red;
  text-decoration: none;
} /*# sourceMappingURL=style.css.map */
```

- 变量设置

```scss
$themeColor: red;
h1 {
  color: $themeColor;
}
```

```css
h1 {
  color: red;
}
```

- Self Ampersand

```scss
a {
  color: green;
  text-decoration: none;
  &:hover {
	color: blue;
  }
```

```css
a {
  color: green;
  text-decoration: none;
}

a:hover {
  color: blue;
}
```

- Import

> 分类，重复利用

```scss
// 在_header.scss中输入
header {
  nav {
    ul {
      display: flex;
      flex-wrap: wrap;
      li {
        list-style-type: none;
        a {
          color: green;
          text-decoration: none;
          &:hover {
            color: blue;
          }
        }
      }
    }
  }
}

// 在style.scss中引用
@import "./header";
```

```css
header nav ul {
  display: flex;
  flex-wrap: wrap;
}
header nav ul li {
  list-style-type: none;
}
header nav ul li a {
  color: green;
  text-decoration: none;
}
header nav ul li a:hover {
  color: blue;
}
```

- Mixin

> function, method

```scss
@mixin flexbox($direction) {
  display: flex;
  flex-direction: $direction;
}

header {
  nav {
    ul {
      @include flexbox(column);
      flex-wrap: wrap;
      li {
        list-style-type: none;
        a {
          color: green;
          text-decoration: none;
          &:hover {
            color: blue;
          }
        }
      }
    }
  }
}
```

```css
header nav ul {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
header nav ul li {
  list-style-type: none;
}
header nav ul li a {
  color: green;
  text-decoration: none;
}
header nav ul li a:hover {
  color: blue;
}
```
