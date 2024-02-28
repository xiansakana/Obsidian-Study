---
title: Hexo博客增加书单集
tags:
  - Hexo
categories: Hexo
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202309282106651.jpg
abbrlink: 3acbfff3
date: 2023-09-28 21:05:33
---

前几天突然想给博客添加书单的功能，但是搜了很多教程，大多是那种豆瓣的书单，我想要的是自定义而且能够在线预览的那种。偶然间翻到一位大佬的书单，刚好符合我的想法，就拿过来参考了一下（[hexo 博客增加书单](https://www.mz-zone.cn/2021/11/12/20211112001/)）。

## 创建书单页面

首先创建新页面

```bash
hexo new page book
```

## 插入源代码

直接在生成的 index.md 文件中插入页面的 html 代码

```html
<link rel="stylesheet" href="/css/book.css" />

<div class="page">
  <!-- 每个li标签内容代表一本书籍的所有信息 -->
  <div class="info">
    <div class="image" title="无职转生">
      <img
        src="https://cdn.jsdelivr.net/npm/xiansakana-blog-assets/blog-assets/%E6%97%A0%E8%81%8C%E8%BD%AC%E7%94%9F/images/cover.jpg"
      />
    </div>
    <div class="info-card">
      <!-- <a href="https://cdn.jsdelivr.net/npm/xiansakana-blog-assets@1.0.1/blog-assets/%E6%97%A0%E8%81%8C%E8%BD%AC%E7%94%9FWEB_compressed.pdf" target="_Blank">                           -->
      <h2>
        <a href="无职转生/无职转生.html" target="_Blank"> 《无职转生》 </a>
      </h2>
      <h4>作者：理不尽な孫の手</h4>
      <h4>出版时间：</h4>
      <p>2014-01-24——2022-11-25</p>
      <h4>
        <span>推荐指数：</span>
        <span>
          <!-- 推荐指数，多少个星星就有以下多少个i标签 -->
          <i class="fas fa-star"></i><i class="fas fa-star"></i
          ><i class="fas fa-star"></i><i class="fas fa-star"></i
          ><i class="fas fa-star"></i>
        </span>
      </h4>
      <p class="text">
        34岁无职童贞尼特身无分文地被赶出家门，发现自己的人生已经完全走投无路。刚刚产生后悔的想法，他就被卡车撞死了。然后醒来的地方居然是——剑与魔法的异世界！！重生为名叫卢迪乌斯的婴儿的他下定决心，“这次一定要认真地活下去……！”，一定要度过一段不会后悔的人生。他利用前世的智力很快使得自己的魔法的才能开花结果，结果一位年轻的女孩子成了自己的家庭教师。并且又与一位有着绿宝石般美丽秀发的四分一血统的精灵相遇。他崭新的人生开始前进。——让人憧憬的转生型奇幻小说，在这里开始。
      </p>
    </div>
  </div>
</div>
```

## 插入 css 来改变页面的样式

新建文件 source/css/book.css，插入以下代码

```css
div.info {
  display: flex;
  flex-wrap: wrap;
  padding: 1rem;
}

div.info div.image {
  flex: 1 1 200px;
  display: flex;
  align-items: center;
}

div.info div.image img {
  width: 60%;
}

div.info div.info-card {
  flex: 3 1 500px;
}
```

## 创建预览页面

这里我在根目录的 source 中创建了一个文件夹命名为 book，并将刚刚生成的 index.md 书单页面放进去，然后在源代码的第 8 和 14 行可以自行修改跳转链接。我这里是在 book 文件夹中又新建了一个文件夹然后又创建了该书的目录页面，所以可以直接跳转。

```html
<a href="无职转生/无职转生.html" target="_Blank" class="book-container"></a>
```

为了使得每个章节都能打开和收起功能而且第一章默认打开，又自行添加了一个 script，而且目录中也可以直接跳转到每一小节的内容，只要在该 book 文件夹中加入相应的 html 文件就行。下面是该页面的部分代码，仅供参考。

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>小说目录</title>
    <style>
      .section {
        display: none; /* 默认隐藏部分 */
      }
    </style>
  </head>
  <body>
    <h1>无职转生</h1>

    <h2>目录</h2>
    <ul id="chapter-list">
      <li>
        <span class="toggle" onclick="toggleSection('chapter1')">[-]</span>
        <a href="chapter2.html">第一章 幼年期</a>
        <ul id="chapter1" class="section">
          <li><a href="chapter3.html">序章</a></li>
          <li><a href="chapter4.html">第一话 难道是：异世界</a></li>
          <li><a href="chapter5.html">第二话 感到退缩的女仆</a></li>
          <li><a href="chapter6.html">第三话 魔法课本</a></li>
          <li><a href="chapter7.html">第四话 师傅</a></li>
          <li><a href="chapter8.html">第五话 剑术与魔法</a></li>
          <li><a href="chapter9.html">第六话 尊敬的理由</a></li>
          <li><a href="chapter10.html">第七话 朋友</a></li>
          <li><a href="chapter11.html">第八话 迟钝</a></li>
          <li><a href="chapter12.html">第九话 紧急家族会议</a></li>
          <li><a href="chapter13.html">第十话 瓶颈</a></li>
          <li><a href="chapter14.html">第十一话 离别</a></li>
          <li><a href="chapter15.html">番外 格瑞拉特家的母亲</a></li>
          <li><a href="chapter16.html">文库特典 人生的绿洲</a></li>
        </ul>
      </li>
      <!-- 添加更多章节链接 -->
    </ul>
    <script>
      function toggleSection(sectionId) {
        var section = document.getElementById(sectionId);
        if (section.style.display === "none" || section.style.display === "") {
          section.style.display = "block";
          document.querySelector("#chapter-list li span.toggle").textContent =
            "[-]";
        } else {
          section.style.display = "none";
          document.querySelector("#chapter-list li span.toggle").textContent =
            "[+]";
        }
      }

      // 如果章节或部分数量超过5个，则触发默认展开功能
      var chapters = document.querySelectorAll("#chapter-list li ul.section");
      for (var i = 0; i < chapters.length; i++) {
        if (chapters[i].children.length > 5) {
          chapters[i].style.display = "block";
          chapters[i].previousElementSibling.querySelector(
            ".toggle"
          ).textContent = "[-]";
        }
      }
    </script>
  </body>
</html>
```

## 预览效果

最后 hexo 三连之后就可以预览效果啦

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202310052134977.png)

下面是目录的预览

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202309282146203.png)

## 更新

考虑到 html 的页面需要每次都上传到服务器，而且久而久之会拖慢预览和上传的速度，已经将具体的书页托管到 netlify 然后链接到对应页面即可进行阅读。
