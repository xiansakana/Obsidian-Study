---
title: Next.js
tags:
  - Next.js
  - React
categories: 学习
cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291739583.jpg'
abbrlink: 98531b37
date: 2023-11-29 17:36:34
---

## Next.js

Next.js 是一个构建于 Node.js 之上的开源 Web 开发框架，支援基于 React 的 Web 应用程式功能。初始版本于 2016 年 10 月 25 日发布。 Next.js 是最流行的 React 框架之一。Next.js 在发布之前，会经过以下的步骤:

1. Compiling - 代码需要转换成浏览器可以理解的版本。
2. Minifying - Minifying 是在不更改代码功能的情况下删除不必要的代码格式和注释的过程。目标是通过减小文件大小来提高应用程序的性能。
3. Bundling - Bundling 是将 modules 合并（或“打包”）的过程，目的是减少用户访问网页时对文件的请求数量。
4. Code Splitting - 是将应用程序的 bundle 分为每个 end point 所需的较小块的过程。目标是通过仅加载运行该页面所需的代码来改进应用程序的初始加载时间。

Next.js 内建了 Code Splitting 的功能。在建构 Next.js 网站时， pages/ 目录中的每个文件都会自动将代码拆分为自己的 JavaScript bundle。此外， 不同页面之间共享的任何代码也会被拆分到另一个 bundle 中，以避免在前往另一个页面时，重新下载相同的代码。在初始页面加载后，Next.js 也会自动开始 pre-loading 用户可能导航到的其他页面的代码。

### Compiling

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291434652.png)

### Minifying

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291435221.png)

### Bundling

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291435175.png)

### Code Splitting

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291435075.png)

## 渲染方式

在 React 课程当中，我们学过，React 的运作方式为， 浏览器从服务器接收一个空的 index.html 文件以及用于构建 UI 的 JavaScript 程式码。渲染页面内容的工作发生在用户端的电脑设备上，这被称为 client-side rendering。

在 Next.js 当中，我们可以设定要使用 client-side rendering 还是 pre-rendering。 pre-rendering 有两种方式：

1. Server-Side Rendering - 对于每个 HTTP Request，网页会重复制作。通常在需要重复向 API 请求即时数据的网页会选用此种方法。
2. Static Site Generation - 网页会被制作一次，并且存放在 Content Delivery Networks (CDNs)的服务器上面重复使用。

### Client-Side Rendering

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291437458.png)

### Server-Side Rendering

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291437927.png)

### Content Delivery Network

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291437518.png)

## Routing in Next.js

在 Next.js 当中的 Routing 规则很简单:

1. 每个页面的 routes 与在 pages 资料夹内的路径有关。 pages/index.js 使用的是 / 这个 route。
2. pages/posts/first-post.js 使用的是 pages 资料夹的 posts 这个资料夹当中， /posts/first-post 这个 route。

## 使用`<Link>`标签

在 Next.js 当中，开发者会使用`<Link>`标签当作`<a>`的替代品(需要 import Link from "next/link")。两者的差别在于:

1. 使用`<Link>`标签链接到的新网页是使用 JavaScript 加载的，所以只换变更网页内部需要改变的内容，而不会重整整个网页。
2. Next.js 有”prefetching”的功能。每当`<Link>`出现在浏览器时，Next.js 会自动在后台 prefetch `<Link>`页面的代码。当使用者点击`<Link>`时，目标页面的代码可能已经在后台加载完成。

> 如果我们的网站需要链接到 Next.js 应用程序之外的页面(例如连结到 YouTube)，使用`<a>`即可。

```jsx
<a href="/posts/edit-post">编辑post</a>
<Link href="/posts/edit-post">编辑post</Link>
```

## Metadata

在 Next.js 当中，使用`<Head>`标签可以设定网页的 metadata。 `<Head>` 本身是一个内建在 Next.js 中的 Component，可以用来代替 HTML 当中的`<head>`标签。使用`<Head>`之前，需要先 import Head from “next/head”。

## CSS Modules

Next.js 支援 CSS Modules 的功能。 CSS Modules 是指，我们可以将 CSS 文件做成 module，并且将样式套用给特定的 Next.js Component。

CSS Modules 当中，文件的命名规则是[name].module.css。此外，CSS 样式套用在 Component 上时，会自动生成一个独特的 class 名称。此特性可以让我们避免 CSS 的命名冲突。

如果我们希望某些 CSS 样式套用到所有页面上，我们需要创建一个名为 pages/\_app.js 的文件。 (创建这个文件后，伺服器一定要重新运行。) Next.js 会自动套用\_app.js 的样式到所有页面上。

## Next.js 开发选项

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311291557787.png)
