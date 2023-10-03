---
title: Hexo博客增加书单集
tags:
  - Hexo
categories: 学习
cover: 'https://img.xiansakana.xyz/202309282106651.jpg'
abbrlink: 3acbfff3
date: 2023-09-28 21:05:33
---

前几天突然想给博客添加书单的功能，但是搜了很多教程，大多是那种豆瓣的书单，我想要的是自定义而且能够在线预览的那种。偶然间翻到一位大佬的书单，刚好符合我的想法，就拿过来参考了一下（[hexo博客增加书单](https://www.mz-zone.cn/2021/11/12/20211112001/)）。

## 创建书单页面

首先创建新页面

``` bash
hexo new page book
```

## 插入源代码

直接在生成的index.md文件中插入页面的html代码

```html

<div id="book">
        <div class="page">
            <ul class="content">
                <!-- 每个li标签内容代表一本书籍的所有信息 -->
                <li>
                    <div class="info">
                        <a href="无职转生/无职转生.html" target="_Blank" class="book-container">
                            <div class="book" title="无职转生">
                                <img src="https://cdn.jsdelivr.net/npm/xiansakana-blog-assets/blog-assets/%E6%97%A0%E8%81%8C%E8%BD%AC%E7%94%9F/images/cover.jpg" class="lazyload">
                            </div>
                        </a>
                        <div class="info-card">                            
                            <a href="无职转生/无职转生.html" target="_Blank"> 
                            <h2>《无职转生》</h2>
                            <h4>作者：理不尽な孫の手</h4>
                            <h4>出版时间：<br/>2014-01-24——2022-11-25</h4>
                            <h4>
                                <span>推荐指数：</span>
                                <span></span>
                                <!-- 推荐指数，多少个星星就有以下多少个i标签 -->
                                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i> 
                            </h4>                            
                            <h5>
                                <p class="text">34岁无职童贞尼特身无分文地被赶出家门，发现自己的人生已经完全走投无路。刚刚产生后悔的想法，他就被卡车撞死了。然后醒来的地方居然是——剑与魔法的异世界！！重生为名叫卢迪乌斯的婴儿的他下定决心，“这次一定要认真地活下去……！”，一定要度过一段不会后悔的人生。他利用前世的智力很快使得自己的魔法的才能开花结果，结果一位年轻的女孩子成了自己的家庭教师。并且又与一位有着绿宝石般美丽秀发的四分一血统的精灵相遇。他崭新的人生开始前进。——让人憧憬的转生型奇幻小说，在这里开始。</p>                                                               
                            </h5>
                            </a>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
```

## 插入css来改变页面的样式

新建文件source/css/book.css，插入以下代码

```html
<style>
    @media screen and (max-width: 877px) {
        #book .page .content {
            flex-direction: column;
            align-items: center;
        }
    }

    #book {
        width: 100%;
    }

    #book .info .info-card {
        position: relative;
        width: 1000px;
        overflow: hidden;
        transition: .3s
    }

    #book .info-card h3 {
        position: unset;
        background: none;
        display: block;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }

    #book .info-card h3:before {
        display: none;
    }

    #book .page {
        overflow: hidden;
        border-radius: 3px;
        width: 100%;
    }

    @media screen and (min-width: 768px) {
        #book .content {
            grid-template-columns: 1fr 1fr;
        }
    }

    #book .content {
        display: flex;
        align-items: center;
        width: 100%;
        margin: 0;
        justify-content: space-between;
        flex-wrap: wrap;
        padding: 16px;
        text-align: justify;
    }

    #book .content li {
        width: 1280px;
        list-style: none;
        margin-bottom: 16px;
        border-radius: 8px;
        transition: all .3s ease 0s, -webkit-transform .6s cubic-bezier(.6, .2, .1, 1) 0s;
        transition: all .3s ease 0s, transform .6s cubic-bezier(.6, .2, .1, 1) 0s;
        transition: all .3s ease 0s, transform .6s cubic-bezier(.6, .2, .1, 1) 0s, -webkit-transform .6s cubic-bezier(.6, .2, .1, 1) 0s;
    }

    #book .content li .info {
        border-radius: 8px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-pack: start;
        -ms-flex-pack: start;
        justify-content: flex-start;
        padding: 16px 12px;
        line-height: 1.7;
        list-style: none;
    }

    .book-container {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        -webkit-perspective: 600px;
        perspective: 600px;
    }

    .book {
        position: relative;
        width: 100px;
        height: 150px;
        -webkit-transform-style: preserve-3d;
        transform-style: preserve-3d;
        -webkit-transform: rotateY(-30deg);
        transform: rotateY(-30deg);
        -webkit-transition: 1s ease;
        transition: 1s ease;
        -webkit-animation: bookRotate 0s 1s ease 0s;
        animation: bookRotate 0s 1s ease 0s;
        list-style: none;
    }

    .book:before {
        content: " ";
        position: absolute;
        left: 0;
        top: 2px;
        width: 23px;
        height: 146px;
        -webkit-transform: translateX(84.5px) rotateY(90deg);
        transform: translateX(84.5px) rotateY(90deg);
        background: -webkit-gradient(linear, left top, right top, from(#fff), color-stop(5%, #f9f9f9), color-stop(10%, #fff), color-stop(15%, #f9f9f9), color-stop(20%, #fff), color-stop(25%, #f9f9f9), color-stop(30%, #fff), color-stop(35%, #f9f9f9), color-stop(40%, #fff), color-stop(45%, #f9f9f9), color-stop(50%, #fff), color-stop(55%, #f9f9f9), color-stop(60%, #fff), color-stop(65%, #f9f9f9), color-stop(70%, #fff), color-stop(75%, #f9f9f9), color-stop(80%, #fff), color-stop(85%, #f9f9f9), color-stop(90%, #fff), color-stop(95%, #f9f9f9), to(#fff));
        background: linear-gradient(90deg, #fff, #f9f9f9 5%, #fff 10%, #f9f9f9 15%, #fff 20%, #f9f9f9 25%, #fff 30%, #f9f9f9 35%, #fff 40%, #f9f9f9 45%, #fff 50%, #f9f9f9 55%, #fff 60%, #f9f9f9 65%, #fff 70%, #f9f9f9 75%, #fff 80%, #f9f9f9 85%, #fff 90%, #f9f9f9 95%, #fff);
    }

    .book>:first-child {
        position: absolute;
        top: 0;
        left: 0;
        width: 100px;
        height: 150px;
        -webkit-transform: translateZ(12.5px);
        transform: translateZ(12.5px);
        border-radius: 0 2px 2px 0;
        -webkit-box-shadow: 5px 5px 20px #666;
        box-shadow: 5px 5px 20px #666;
    }

    .book:after {
        content: " ";
        position: absolute;
        top: 0;
        left: 0;
        width: 100px;
        height: 150px;
        -webkit-transform: translateZ(-12.5px);
        transform: translateZ(-12.5px);
        background-color: #555;
        border-radius: 0 2px 2px 0;
    }

    #book .content li .info>div {
        margin-left: 26px;
    }

    #book .content li .info h3 {
        font-size: 16px;
    }

    #book .content li .info p a {
        position: relative;
        color: #b854d4;
    }

    #book .content li .info p a:before {
        content: " "attr(href);
        position: absolute;
        padding: 0 4px;
        width: -webkit-max-content;
        width: -moz-max-content;
        width: max-content;
        pointer-events: none;
        font-family: Fontello;
        font-size: 12px;
        -webkit-box-shadow: 0 14px 38px rgba(0, 0, 0, .08), 0 3px 8px rgba(0, 0, 0, .06);
        box-shadow: 0 14px 38px rgba(0, 0, 0, .08), 0 3px 8px rgba(0, 0, 0, .06);
        border-radius: 3px;
        background-color: #fff;
        opacity: 0;
        -webkit-transform: scale(.7) translateY(-75%);
        transform: scale(.7) translateY(-75%);
        -webkit-transform-origin: left center;
        transform-origin: left center;
        -webkit-transition: all .3s ease 0s;
        transition: all .3s ease 0s;
    }

    #book .content li .info p a:after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 1.5px;
        background-color: #b854d4;
        -webkit-transform: scaleX(0);
        transform: scaleX(0);
        -webkit-transform-origin: bottom right;
        transform-origin: bottom right;
        -webkit-transition: -webkit-transform .3s ease-out;
        transition: -webkit-transform .3s ease-out;
        transition: transform .3s ease-out;
        transition: transform .3s ease-out, -webkit-transform .3s ease-out;
    }

    #book .content li .info .fa-star {
        margin-right: 4px;
        color: #d68fe9;
    }

    .icon-star:before {
        content: "\e80b";
    }

    [class*=" icon-"]:before,
    [class^=icon-]:before {
        font-family: Fontello;
        font-style: normal;
        font-weight: 400;
        display: inline-block;
        text-decoration: inherit;
        width: 1em;
        text-align: center;
        font-variant: normal;
        text-transform: none;
        line-height: 1em;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    #book .content li .description {
        padding: 12px;
        font-size: 14px;
        line-height: 1.7;
    }

    #book .content li .info p {
        font-size: 14px;
        line-height: 1.7;

    }

    @media screen and (min-width: 768px) {
    #book .content li:hover {
        -webkit-transform: translateY(-4px);
        transform: translateY(-4px);
        -webkit-box-shadow: 0 14px 38px rgba(0, 0, 0, .14), 0 3px 8px rgba(0, 0, 0, .12);
        box-shadow: 0 14px 38px rgba(0, 0, 0, .14), 0 3px 8px rgba(0, 0, 0, .12);
    }
}


    #book .content li:hover .book {
        -webkit-transform: rotateY(0deg);
        transform: rotateY(0deg);
    }    
</style>
```

## 创建预览页面

这里我在根目录的source中创建了一个文件夹命名为book，并将刚刚生成的index.md书单页面放进去，然后在源代码的第8和14行可以自行修改跳转链接。我这里是在book文件夹中又新建了一个文件夹然后又创建了该书的目录页面，所以可以直接跳转。

```html
 <a href="无职转生/无职转生.html" target="_Blank" class="book-container">
```

为了使得每个章节都能打开和收起功能而且第一章默认打开，又自行添加了一个script，而且目录中也可以直接跳转到每一小节的内容，只要在该book文件夹中加入相应的html文件就行。下面是该页面的部分代码，仅供参考。

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
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
                document.querySelector('#chapter-list li span.toggle').textContent = '[-]';
            } else {
                section.style.display = "none";
                document.querySelector('#chapter-list li span.toggle').textContent = '[+]';
            }
        }
        
        // 如果章节或部分数量超过5个，则触发默认展开功能
        var chapters = document.querySelectorAll('#chapter-list li ul.section');
        for (var i = 0; i < chapters.length; i++) {
            if (chapters[i].children.length > 5) {
                chapters[i].style.display = "block";
                chapters[i].previousElementSibling.querySelector('.toggle').textContent = '[-]';
            }
        }
    </script>
</body>
</html>    
```

## 预览效果

最后hexo三连之后就可以预览效果啦

![](https://img.xiansakana.xyz/202309282124790.png)

下面是目录的预览

![](https://img.xiansakana.xyz/202309282146203.png)
