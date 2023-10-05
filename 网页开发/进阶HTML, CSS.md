## [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
### [Flex Container](https://developer.mozilla.org/zh-CN/docs/Glossary/Flex_Container)
#### [flex-direcction](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-direction)
- row: 横向
- column: 纵向
- row-reverse: 横向反向
- column-reverse: 纵向反向
#### [flex-wrap](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-wrap)(自动换行)
- nowrap (默认)
- wrap
- wrap-reverse

#### [justify-content](https://developer.mozilla.org/zh-CN/docs/Web/CSS/justify-content)
>浏览器如何沿着弹性容器的[主轴](https://developer.mozilla.org/zh-CN/docs/Glossary/Main_Axis)和网格容器的行向轴分配内容元素之间和周围的空间。
- flex-start (默认)
- flex-end
- center
- space-between
- space-around
- space-evenly
![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310042340682.png)
#### [align-items](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-items)
>控制在cross axis (与main axis垂直)上的对齐方式。
- stretch (默认)
- flex-start
- flex-end
- center
- baseline
![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310042340567.png)

#### [align-content](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-content)
- normal (默认)
- stretch
- flex-start
- flex-end
- center
- space-between
- space-around
- space-evenly
![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202310050016526.png)

### [Flex Item](https://developer.mozilla.org/zh-CN/docs/Glossary/Flex_Item)
- [flex-grow](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-grow): 将flex container中的剩余空间(remaining space)分配给flex items
- [flex-shrink](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-shrink): 定义了flex item在必要时收缩的能力
- [flex-basis](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-basis): 指定了 flex item在主轴方向上的初始大小
>flex可以一次设置grow, shrink, basis
```css
flex: 1 1 100px
```
- [align-self](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-self): 单个flex item设置对齐方式

