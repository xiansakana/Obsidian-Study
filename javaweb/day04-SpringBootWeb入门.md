---
title: day04-SpringBootWeb入门
date: 2024-04-25T19:19:17Z
lastmod: 2024-04-25T19:19:17Z
---

## 前言

![image-20221130095316032](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221130095316032.png)

下面我们将进入 SpringBoot 基础阶段的学习。

在没有正式的学习 SpringBoot 之前，我们要先来了解下什么是 Spring。

我们可以打开 Spring 的官网(https://spring.io)，去看一下Spring的简介：Spring makes Java simple。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220617222738668.png)

Spring 的官方提供很多开源的项目，我们可以点击上面的 projects，看到 spring 家族旗下的项目，按照流行程度排序为：

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220617222925923.png)

Spring 发展到今天已经形成了一种开发生态圈，Spring 提供了若干个子项目，每个项目用于完成特定的功能。而我们在项目开发时，一般会偏向于选择这一套 spring 家族的技术，来解决对应领域的问题，那我们称这一套技术为**spring 全家桶**。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220617222609699.png)

而 Spring 家族旗下这么多的技术，最基础、最核心的是 SpringFramework。其他的 spring 家族的技术，都是基于 SpringFramework 的，SpringFramework 中提供很多实用功能，如：依赖注入、事务管理、web 开发支持、数据访问、消息服务等等。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220617224427947.png)

而如果我们在项目中，直接基于 SpringFramework 进行开发，存在两个问题：配置繁琐、入门难度大。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823185227296.png)

所以基于此呢，spring 官方推荐我们从另外一个项目开始学习，那就是目前最火爆的 SpringBoot。

通过 springboot 就可以快速的帮我们构建应用程序，所以 springboot 呢，最大的特点有两个 ：

- 简化配置
- 快速开发

**Spring Boot 可以帮助我们非常快速的构建应用程序、简化开发、提高效率 。**

接下来，我们就直接通过一个 SpringBoot 的 web 入门程序，让大家快速感受一下，基于 SpringBoot 进行 Web 开发的便捷性。

## 1. SpringBootWeb 快速入门

### 1.1 需求

需求：基于 SpringBoot 的方式开发一个 web 应用，浏览器发起请求/hello 后，给浏览器返回字符串 “Hello World ~”。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823191003444.png)

### 1.2 开发步骤

第 1 步：创建 SpringBoot 工程项目

第 2 步：定义 HelloController 类，添加方法 hello，并添加注解

第 3 步：测试运行

#### 1.2.1 创建 SpringBoot 工程（需要联网）

基于 Spring 官方骨架，创建 SpringBoot 工程。

<div>
<img src="https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201184702136.png" alt="image-20221201184702136" style="zoom:80%;" />
</div>

基本信息描述完毕之后，勾选 web 开发相关依赖。

<div>
<img src="https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201184850248.png" alt="image-20221201184850248" style="zoom:80%;" />
</div>

点击 Finish 之后，就会联网创建这个 SpringBoot 工程，创建好之后，结构如下：

- ==注意：在联网创建过程中，会下载相关资源(请耐心等待)==

![image-20221201185910596](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201185910596.png)

#### 1.2.2 定义请求处理类

在 com.itheima 这个包下创建一个子包 controller

<div>
<img src="https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201190541295.png" alt="image-20221201190541295" style="zoom:80%;" />
</div>

然后在 controller 包下新建一个类：HelloController

<div>
<img src="https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201190825439.png" alt="image-20221201190825439" style="zoom:80%;" />
</div>

```java
package com.itheima.controller;
import org.springframework.web.bind.annotation.*;

@RestController
public class HelloController {

    @RequestMapping("/hello")
    public String hello(){
        System.out.println("Hello World ~");
        return "Hello World ~";
    }

}
```

#### 1.2.3 运行测试

运行 SpringBoot 自动生成的引导类

![image-20221201191028124](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201191028124.png)

![image-20221201191348924](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201191348924.png)

打开浏览器，输入 `http://localhost:8080/hello`

![image-20220823195048415](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823195048415.png)

### 1.3 Web 分析

![image-20221201224603497](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221201224603497.png)

浏览器：

- 输入网址：`http://192.168.100.11:8080/hello`

  - 通过 IP 地址 192.168.100.11 定位到网络上的一台计算机

    > 我们之前在浏览器中输入的 localhost，就是 127.0.0.1（本机）

  - 通过端口号 8080 找到计算机上运行的程序

    > `localhost:8080` , 意思是在本地计算机中找到正在运行的 8080 端口的程序

  - /hello 是请求资源位置

    - 资源：对计算机而言资源就是数据
      - web 资源：通过网络可以访问到的资源（通常是指存放在服务器上的数据）

    > `localhost:8080/hello` ，意思是向本地计算机中的 8080 端口程序，获取资源位置是/hello 的数据
    >
    > - 8080 端口程序，在服务器找/hello 位置的资源数据，发给浏览器

服务器：（可以理解为 ServerSocket）

- 接收到浏览器发送的信息（如：/hello）
- 在服务器上找到/hello 的资源
- 把资源发送给浏览器

> 我们在 JavaSE 阶段学习网络编程时，有讲过网络三要素：
>
> - IP ：网络中计算机的唯一标识
> - 端口 ：计算机中运行程序的唯一标识
> - 协议 ：网络中计算机之间交互的规则
>
> **问题：浏览器和服务器两端进行数据交互，使用什么协议？**
>
> **答案：http 协议**

## 2. HTTP 协议

### 2.1 HTTP-概述

#### 2.1.1 介绍

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823200024507.png)

HTTP：Hyper Text Transfer Protocol(超文本传输协议)，规定了浏览器与服务器之间数据传输的规则。

- http 是互联网上应用最为广泛的一种网络协议
- http 协议要求：浏览器在向服务器发送请求数据时，或是服务器在向浏览器发送响应数据时，都必须按照固定的格式进行数据传输

如果想知道 http 协议的数据传输格式有哪些，可以打开浏览器，点击`F12`打开开发者工具，点击`Network`来查看

![image-20221202105735230](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202105735230.png)

浏览器向服务器进行请求时：

- 服务器按照固定的格式进行解析

![image-20221202111044434](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202111044434.png)

服务器向浏览器进行响应时：

- 浏览器按照固定的格式进行解析

![image-20221202111307819](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202111307819.png)

**所以，我们学习 HTTP 主要就是学习请求和响应数据的具体格式内容。**

#### 2.2.2 特点

我们刚才初步认识了 HTTP 协议，那么我们在看看 HTTP 协议有哪些特点：

- **基于 TCP 协议: ** 面向连接，安全

  > TCP 是一种面向连接的(建立连接之前是需要经过三次握手)、可靠的、基于字节流的传输层通信协议，在数据传输方面更安全

- **基于请求-响应模型:** 一次请求对应一次响应（先请求后响应）

  > 请求和响应是一一对应关系，没有请求，就没有响应

- **HTTP 协议是无状态协议:** 对于数据没有记忆能力。每次请求-响应都是独立的

  > 无状态指的是客户端发送 HTTP 请求给服务端之后，服务端根据请求响应数据，响应完后，不会记录任何信息。
  >
  > - 缺点: 多次请求间不能共享数据
  > - 优点: 速度快
  >
  > 请求之间无法共享数据会引发的问题：
  >
  > - 如：京东购物。加入购物车和去购物车结算是两次请求
  > - 由于 HTTP 协议的无状态特性，加入购物车请求响应结束后，并未记录加入购物车是何商品
  > - 发起去购物车结算的请求后，因为无法获取哪些商品加入了购物车，会导致此次请求无法正确展示数据
  >
  > 具体使用的时候，我们发现京东是可以正常展示数据的，原因是 Java 早已考虑到这个问题，并提出了使用会话技术(Cookie、Session)来解决这个问题。具体如何来做，我们后面课程中会讲到。

  刚才提到 HTTP 协议是规定了请求和响应数据的格式，那具体的格式是什么呢?

### 2.2 HTTP-请求协议

浏览器和服务器是按照 HTTP 协议进行数据通信的。

HTTP 协议又分为：请求协议和响应协议

- 请求协议：浏览器将数据以请求格式发送到服务器
  - 包括：**请求行**、**请求头** 、**请求体**
- 响应协议：服务器将数据以响应格式返回给浏览器
  - 包括：**响应行** 、**响应头** 、**响应体**

在 HTTP1.1 版本中，浏览器访问服务器的几种方式：

| 请求方式 | 请求说明                                                                                                                                                                                              |
| :------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GET**  | 获取资源。<br />向特定的资源发出请求。例：http://www.baidu.com/s?wd=itheima                                                                                                                           |
| **POST** | 传输实体主体。<br />向指定资源提交数据进行处理请求（例：上传文件），数据被包含在请求体中。                                                                                                            |
| OPTIONS  | 返回服务器针对特定资源所支持的 HTTP 请求方式。<br />因为并不是所有的服务器都支持规定的方法，为了安全有些服务器可能会禁止掉一些方法，例如：DELETE、PUT 等。那么 OPTIONS 就是用来询问服务器支持的方法。 |
|   HEAD   | 获得报文首部。<br />HEAD 方法类似 GET 方法，但是不同的是 HEAD 方法不要求返回数据。通常用于确认 URI 的有效性及资源更新时间等。                                                                         |
|   PUT    | 传输文件。<br />PUT 方法用来传输文件。类似 FTP 协议，文件内容包含在请求报文的实体中，然后请求保存到 URL 指定的服务器位置。                                                                            |
|  DELETE  | 删除文件。<br />请求服务器删除 Request-URI 所标识的资源                                                                                                                                               |
|  TRACE   | 追踪路径。<br />回显服务器收到的请求，主要用于测试或诊断                                                                                                                                              |
| CONNECT  | 要求用隧道协议连接代理。<br />HTTP/1.1 协议中预留给能够将连接改为管道方式的代理服务器                                                                                                                 |

在我们实际应用中常用的也就是 ：**GET、POST**

**GET 方式的请求协议：**

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823200708026.png)

- 请求行 ：HTTP 请求中的第一行数据。由：`请求方式`、`资源路径`、`协议/版本`组成（之间使用空格分隔）

  - 请求方式：GET
  - 资源路径：/brand/findAll?name=OPPO&status=1
    - 请求路径：/brand/findAll
    - 请求参数：name=OPPO&status=1
      - 请求参数是以 key=value 形式出现
      - 多个请求参数之间使用`&`连接
    - 请求路径和请求参数之间使用`?`连接
  - 协议/版本：HTTP/1.1

- 请求头 ：第二行开始，上图黄色部分内容就是请求头。格式为 key: value 形式

  - http 是个无状态的协议，所以在请求头设置浏览器的一些自身信息和想要响应的形式。这样服务器在收到信息后，就可以知道是谁，想干什么了

  常见的 HTTP 请求头有:

  ```
  Host: 表示请求的主机名
  
  User-Agent: 浏览器版本。 例如：Chrome浏览器的标识类似Mozilla/5.0 ...Chrome/79 ，IE浏览器的标识类似Mozilla/5.0 (Windows NT ...)like Gecko
  
  Accept：表示浏览器能接收的资源类型，如text/*，image/*或者*/*表示所有；
  
  Accept-Language：表示浏览器偏好的语言，服务器可以据此返回不同语言的网页；
  
  Accept-Encoding：表示浏览器可以支持的压缩类型，例如gzip, deflate等。
  
  Content-Type：请求主体的数据类型
  
  Content-Length：数据主体的大小（单位：字节）
  ```

> 举例说明：服务端可以根据请求头中的内容来获取客户端的相关信息，有了这些信息服务端就可以处理不同的业务需求。
>
> 比如:
>
> - 不同浏览器解析 HTML 和 CSS 标签的结果会有不一致，所以就会导致相同的代码在不同的浏览器会出现不同的效果
> - 服务端根据客户端请求头中的数据获取到客户端的浏览器类型，就可以根据不同的浏览器设置不同的代码来达到一致的效果（这就是我们常说的浏览器兼容问题）

- 请求体 ：存储请求参数
  - GET 请求的请求参数在请求行中，故不需要设置请求体

**POST 方式的请求协议：**

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823201303601.png)

- 请求行(以上图中红色部分)：包含请求方式、资源路径、协议/版本
  - 请求方式：POST
  - 资源路径：/brand
  - 协议/版本：HTTP/1.1
- 请求头(以上图中黄色部分)
- 请求体(以上图中绿色部分) ：存储请求参数
  - 请求体和请求头之间是有一个空行隔开（作用：用于标记请求头结束）

GET 请求和 POST 请求的区别：

| 区别方式     | GET 请求                                                        | POST 请求            |
| ------------ | --------------------------------------------------------------- | -------------------- |
| 请求参数     | 请求参数在请求行中。<br />例：/brand/findAll?name=OPPO&status=1 | 请求参数在请求体中   |
| 请求参数长度 | 请求参数长度有限制(浏览器不同限制也不同)                        | 请求参数长度没有限制 |
| 安全性       | 安全性低。原因：请求参数暴露在浏览器地址栏中。                  | 安全性相对高         |

### 2.3 HTTP-响应协议

#### 2.3.1 格式介绍

与 HTTP 的请求一样，HTTP 响应的数据也分为 3 部分：**响应行**、**响应头** 、**响应体**

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220823202344149.png)

- 响应行(以上图中红色部分)：响应数据的第一行。响应行由`协议及版本`、`响应状态码`、`状态码描述`组成

  - 协议/版本：HTTP/1.1
  - 响应状态码：200
  - 状态码描述：OK

- 响应头(以上图中黄色部分)：响应数据的第二行开始。格式为 key：value 形式

  - http 是个无状态的协议，所以可以在请求头和响应头中设置一些信息和想要执行的动作，这样，对方在收到信息后，就可以知道你是谁，你想干什么

  常见的 HTTP 响应头有:

  ```
  Content-Type：表示该响应内容的类型，例如text/html，image/jpeg ；
  
  Content-Length：表示该响应内容的长度（字节数）；
  
  Content-Encoding：表示该响应压缩算法，例如gzip ；
  
  Cache-Control：指示客户端应如何缓存，例如max-age=300表示可以最多缓存300秒 ;
  
  Set-Cookie: 告诉浏览器为当前页面所在的域设置cookie ;
  ```

* 响应体(以上图中绿色部分)： 响应数据的最后一部分。存储响应的数据
  - 响应体和响应头之间有一个空行隔开（作用：用于标记响应头结束）

#### 2.3.2 响应状态码

| 状态码分类 | 说明                                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| 1xx        | **响应中** --- 临时状态码。表示请求已经接受，告诉客户端应该继续请求或者如果已经完成则忽略                   |
| 2xx        | **成功** --- 表示请求已经被成功接收，处理已完成                                                             |
| 3xx        | **重定向** --- 重定向到其它地方，让客户端再发起一个请求以完成整个处理                                       |
| 4xx        | **客户端错误** --- 处理发生错误，责任在客户端，如：客户端的请求一个不存在的资源，客户端未被授权，禁止访问等 |
| 5xx        | **服务器端错误** --- 处理发生错误，责任在服务端，如：服务端抛出异常，路由出错，HTTP 版本不支持等            |

参考: 资料/SpringbootWeb/响应状态码.md

关于响应状态码，我们先主要认识三个状态码，其余的等后期用到了再去掌握：

- 200 ok 客户端请求成功
- 404 Not Found 请求资源不存在
- 500 Internal Server Error 服务端发生不可预期的错误

### 2.4 HTTP-协议解析

将资料中准备好的 Demo 工程，导入到我们的 IDEA 中，有一个 Server.java 类，这里面就是自定义的一个服务器代码，主要使用到的是`ServerSocket`和`Socket`

> 说明：以下代码大家不需要自己写，我们主要是通过代码，让大家了解到服务器针对 HTTP 协议的解析机制

```java
package com.itheima;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

/*
 * 自定义web服务器
 */
public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket ss = new ServerSocket(8080); // 监听指定端口
        System.out.println("server is running...");

        while (true){
            Socket sock = ss.accept();
            System.out.println("connected from " + sock.getRemoteSocketAddress());
            Thread t = new Handler(sock);
            t.start();
        }
    }
}

class Handler extends Thread {
    Socket sock;

    public Handler(Socket sock) {
        this.sock = sock;
    }

    public void run() {
        try (InputStream input = this.sock.getInputStream();
             OutputStream output = this.sock.getOutputStream()) {
                handle(input, output);
        } catch (Exception e) {
            try {
                this.sock.close();
            } catch (IOException ioe) {
            }
            System.out.println("client disconnected.");
        }
    }

    private void handle(InputStream input, OutputStream output) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(input, StandardCharsets.UTF_8));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output, StandardCharsets.UTF_8));
        // 读取HTTP请求:
        boolean requestOk = false;
        String first = reader.readLine();
        if (first.startsWith("GET / HTTP/1.")) {
            requestOk = true;
        }
        for (;;) {
            String header = reader.readLine();
            if (header.isEmpty()) { // 读取到空行时, HTTP Header读取完毕
                break;
            }
            System.out.println(header);
        }
        System.out.println(requestOk ? "Response OK" : "Response Error");

        if (!requestOk) {// 发送错误响应:
            writer.write("HTTP/1.0 404 Not Found\r\n");
            writer.write("Content-Length: 0\r\n");
            writer.write("\r\n");
            writer.flush();
        } else {// 发送成功响应:
            //读取html文件，转换为字符串
            InputStream is = Server.class.getClassLoader().getResourceAsStream("html/a.html");
            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            StringBuilder data = new StringBuilder();
            String line = null;
            while ((line = br.readLine()) != null){
                data.append(line);
            }
            br.close();
            int length = data.toString().getBytes(StandardCharsets.UTF_8).length;

            writer.write("HTTP/1.1 200 OK\r\n");
            writer.write("Connection: keep-alive\r\n");
            writer.write("Content-Type: text/html\r\n");
            writer.write("Content-Length: " + length + "\r\n");
            writer.write("\r\n"); // 空行标识Header和Body的分隔
            writer.write(data.toString());
            writer.flush();
        }
    }
}

```

启动 ServerSocket 程序：

![image-20221202170430928](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202170430928.png)

浏览器输入：`http://localhost:8080` 就会访问到 ServerSocket 程序

- ServerSocket 程序，会读取服务器上`html/a.html`文件，并把文件数据发送给浏览器
- 浏览器接收到 a.html 文件中的数据后进行解析，显示以下内容

![image-20221202171204705](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202171204705.png)

现在大家知道了服务器是可以使用 java 完成编写，是可以接受页面发送的请求和响应数据给前端浏览器的，而在开发中真正用到的 Web 服务器，我们不会自己写的，都是使用目前比较流行的 web 服务器。如：**Tomcat**

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824233452167.png)

## 3. WEB 服务器-Tomcat

### 3.1 简介

#### 3.1.1 服务器概述

**服务器硬件**

- 指的也是计算机，只不过服务器要比我们日常使用的计算机大很多。

![image-20221202173148317](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202173148317.png)

服务器，也称伺服器。是提供计算服务的设备。由于服务器需要响应服务请求，并进行处理，因此一般来说服务器应具备承担服务并且保障服务的能力。

服务器的构成包括处理器、硬盘、内存、系统总线等，和通用的计算机架构类似，但是由于需要提供高可靠的服务，因此在处理能力、稳定性、可靠性、安全性、可扩展性、可管理性等方面要求较高。

在网络环境下，根据服务器提供的服务类型不同，可分为：文件服务器，数据库服务器，应用程序服务器，WEB 服务器等。

服务器只是一台设备，必须安装服务器软件才能提供相应的服务。

**服务器软件**

服务器软件：基于 ServerSocket 编写的程序

- 服务器软件本质是一个运行在服务器设备上的应用程序
- 能够接收客户端请求，并根据请求给客户端响应数据

![1530625192392](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/1530625192392.png)

#### 3.1.2 Web 服务器

Web 服务器是一个应用程序(软件)，对 HTTP 协议的操作进行封装，使得程序员不必直接对协议进行操作(不用程序员自己写代码去解析 http 协议规则)，让 Web 开发更加便捷。主要功能是"提供网上信息浏览服务"。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824233614686.png)

Web 服务器是安装在服务器端的一款软件，将来我们把自己写的 Web 项目部署到 Tomcat 服务器软件中，当 Web 服务器软件启动后，部署在 Web 服务器软件中的页面就可以直接通过浏览器来访问了。

**Web 服务器软件使用步骤**

- 准备静态资源
- 下载安装 Web 服务器软件
- 将静态资源部署到 Web 服务器上
- 启动 Web 服务器使用浏览器访问对应的资源

第 1 步：准备静态资源

- 在提供的资料中找到静态资源文件

![image-20221202180119859](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202180119859.png)

第 2 步：下载安装 Web 服务器软件

![image-20221202181110555](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202181110555.png)

第 3 步：将静态资源部署到 Web 服务器上

![image-20221202180805686](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202180805686.png)

第 4 步：启动 Web 服务器使用浏览器访问对应的资源

![image-20221202181346327](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202181346327.png)

浏览器输入：`http://localhost:8080/demo/index.html`

![image-20221202181651469](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202181651469.png)

上述内容在演示的时候，使用的是 Apache 下的 Tomcat 软件，至于 Tomcat 软件如何使用，后面会详细的讲到。而对于 Web 服务器来说，实现的方案有很多，Tomcat 只是其中的一种，而除了 Tomcat 以外，还有很多优秀的 Web 服务器，比如:

![image-20220824233728524](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824233728524.png)

Tomcat 就是一款软件，我们主要是以学习如何去使用为主。具体我们会从以下这些方向去学习:

1. 简介：初步认识下 Tomcat
2. 基本使用: 安装、卸载、启动、关闭、配置和项目部署，这些都是对 Tomcat 的基本操作
3. IDEA 中如何创建 Maven Web 项目
4. IDEA 中如何使用 Tomcat,后面这两个都是我们以后开发经常会用到的方式

首选我们来认识下 Tomcat。

### 3.1.3 Tomcat

Tomcat 服务器软件是一个免费的开源的 web 应用服务器。是 Apache 软件基金会的一个核心项目。由 Apache，Sun 和其他一些公司及个人共同开发而成。

由于 Tomcat 只支持 Servlet/JSP 少量 JavaEE 规范，所以是一个开源免费的轻量级 Web 服务器。

> JavaEE 规范： JavaEE => Java Enterprise Edition(Java 企业版)
>
> avaEE 规范就是指 Java 企业级开发的技术规范总和。包含 13 项技术规范：JDBC、JNDI、EJB、RMI、JSP、Servlet、XML、JMS、Java IDL、JTS、JTA、JavaMail、JAF

因为 Tomcat 支持 Servlet/JSP 规范，所以 Tomcat 也被称为 Web 容器、Servlet 容器。JavaWeb 程序需要依赖 Tomcat 才能运行。

Tomcat 的官网: https://tomcat.apache.org/

![image-20220824233903517](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824233903517.png)

### 3.2 基本使用

#### 3.2.1 下载

直接从官方网站下载：https://tomcat.apache.org/download-90.cgi

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824234407828.png)

> Tomcat 软件类型说明：
>
> - tar.gz 文件，是 linux 和 mac 操作系统下的压缩版本
> - zip 文件，是 window 操作系统下压缩版本（我们选择 zip 文件）

大家可以自行下载，也可以直接使用资料中已经下载好的资源，

Tomcat 的软件程序 ：/资料/SpringbootWeb/apache-tomcat-9.0.27-windows-x64.zip

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824234527743.png)

#### 3.2.2 安装与卸载

**安装:** Tomcat 是绿色版，直接解压即安装

> 在 E 盘的 develop 目录下，将`apache-tomcat-9.0.27-windows-x64.zip`进行解压缩，会得到一个`apache-tomcat-9.0.27`的目录，Tomcat 就已经安装成功。

![image-20221202184545321](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202184545321.png)

==注意，Tomcat 在解压缩的时候，解压所在的目录可以任意，但最好解压到一个不包含中文和空格的目录，因为后期在部署项目的时候，如果路径有中文或者空格可能会导致程序部署失败。

打开`apache-tomcat-9.0.27`目录就能看到如下目录结构，每个目录中包含的内容需要认识下

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220824234652173.png)

bin：目录下有两类文件，一种是以`.bat`结尾的，是 Windows 系统的可执行文件，一种是以`.sh`结尾的，是 Linux 系统的可执行文件。

webapps：就是以后项目部署的目录

**卸载：** 卸载比较简单，可以直接删除目录即可

#### 3.2.3 启动与关闭

**启动 Tomcat**

- 双击 tomcat 解压目录/bin/**startup.bat**文件即可启动 tomcat

![image-20221202183201663](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202183201663.png)

==注意: tomcat 服务器启动后,黑窗口不会关闭,只要黑窗口不关闭,就证明 tomcat 服务器正在运行==

![image-20221202183409304](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202183409304.png)

Tomcat 的默认端口为 8080，所以在浏览器的地址栏输入：`http://127.0.0.1:8080` 即可访问 tomcat 服务器

> 127.0.0.1 也可以使用 localhost 代替。如：`http://localhost:8080`

![image-20221202183550682](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202183550682.png)

- 能看到以上图片中 Apache Tomcat 的内容就说明 Tomcat 已经启动成功

==注意事项== ：Tomcat 启动的过程中，遇到控制台有中文乱码时，可以通常修改 conf/logging.prooperties 文件解决

![image-20220825083848086](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220825083848086.png)

**关闭:** 关闭有三种方式

1、强制关闭：直接 x 掉 Tomcat 窗口（不建议）

![image-20221202184753808](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202184753808.png)

2、正常关闭：bin\shutdown.bat

![image-20221202185103941](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202185103941.png)

3、正常关闭：在 Tomcat 启动窗口中按下 Ctrl+C

- 说明：如果按下 Ctrl+C 没有反映，可以多按几次

#### 3.2.4 常见问题

**问题 1：Tomcat 启动时，窗口一闪而过**

- 检查 JAVA_HOME 环境变量是否正确配置

![image-20221202190033167](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202190033167.png)

**问题 2：端口号冲突**

![image-20220825084104447](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220825084104447.png)

- 发生问题的原因：Tomcat 使用的端口被占用了。
- 解决方案：换 Tomcat 端口号

  - 要想修改 Tomcat 启动的端口号，需要修改 conf/server.xml 文件

<div>
<img src="https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220825084017185.png" alt="image-20220825084017185" style="zoom:80%;" />
</div>

> 注: HTTP 协议默认端口号为 80，如果将 Tomcat 端口号改为 80，则将来访问 Tomcat 时，将不用输入端口号。

### 3.3 入门程序解析

关于 web 开发的基础知识，我们可以告一段落了。下面呢，我们在基于今天的核心技术点 SpringBoot 快速入门案例进行分析。

#### 3.3.1 Spring 官方骨架

之前我们创建的 SpringBoot 入门案例，是基于 Spring 官方提供的骨架实现的。

Spring 官方骨架，可以理解为 Spring 官方为程序员提供一个搭建项目的模板。

![image-20221202195646621](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202195646621.png)

我们可以通过访问：https://start.spring.io/ ，进入到官方骨架页面

![image-20221202201623424](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202201623424.png)

![image-20221202200356398](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202200356398.png)

![image-20221202200547676](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202200547676.png)

![image-20221202200708988](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202200708988.png)

Spring 官方生成的 SpringBoot 项目，怎么使用呢？

- 解压缩后，就会得到一个 SpringBoot 项目工程

![image-20221202201042109](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202201042109.png)

![image-20221202201221136](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202201221136.png)

打开 pom.xml 文件，我们可以看到 springboot 项目中引入了 web 依赖和 test 依赖

![image-20221202201826364](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202201826364.png)

> **结论：不论使用 IDEA 创建 SpringBoot 项目，还是直接在官方网站利用骨架生成 SpringBoot 项目，项目的结构和 pom.xml 文件中内容是相似的。**

#### 3.3.2 起步依赖

在我们之前讲解的 SpringBoot 快速入门案例中，同样也引用了：web 依赖和 test 依赖

![image-20221202202305118](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202202305118.png)

spring-boot-starter-web 和 spring-boot-starter-test，在 SpringBoot 中又称为：起步依赖

而在 SpringBoot 的项目中，有很多的起步依赖，他们有一个共同的特征：就是以`spring-boot-starter-`作为开头。在以后大家遇到 spring-boot-starter-xxx 这类的依赖，都为起步依赖。

起步依赖有什么特殊之处呢，这里我们以入门案例中引入的起步依赖做为讲解：

- spring-boot-starter-web：包含了 web 应用开发所需要的常见依赖
- spring-boot-starter-test：包含了单元测试所需要的常见依赖

> **spring-boot-starter-web**内部把关于 Web 开发所有的依赖都已经导入并且指定了版本，只需引入 `spring-boot-starter-web` 依赖就可以实现 Web 开发的需要的功能
>
> ![image-20221202204013113](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202204013113.png)

Spring 的官方提供了很多现成的 starter(起步依赖)，我们在开发相关应用时，只需要引入对应的 starter 即可。

官方地址：https://docs.spring.io/spring-boot/docs/2.7.2/reference/htmlsingle/#using.build-systems.starters

![image-20221202204536647](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202204536647.png)

每一个起步依赖，都用于开发一个特定的功能。

> 举例：当我们开发中需要使用 redis 数据库时，只需要在 SpringBoot 项目中，引入：spring-boot-starter-redis ，即可导入 redis 开发所需要的依赖。

#### 3.3.2 SpringBoot 父工程

在我们之前开发的 SpringBoot 入门案例中，我们通过 maven 引入的依赖，是没有指定具体的依赖版本号的。

![image-20221202205103486](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202205103486.png)

为什么没有指定`<version>`版本号，可以正常使用呢？

- 因为每一个 SpringBoot 工程，都有一个父工程。依赖的版本号，在父工程中统一管理。

![image-20221202205318778](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20221202205318778.png)

#### 3.3.3 内嵌 Tomcat

问题：为什么我们之前书写的 SpringBoot 入门程序中，并没有把程序部署到 Tomcat 的 webapps 目录下，也可以运行呢？

原因呢，是因为在我们的 SpringBoot 中，引入了 web 运行环境(也就是引入 spring-boot-starter-web 起步依赖)，其内部已经集成了内置的 Tomcat 服务器。

我们可以通过 IDEA 开发工具右侧的 maven 面板中，就可以看到当前工程引入的依赖。其中已经将 Tomcat 的相关依赖传递下来了，也就是说在 SpringBoot 中可以直接使用 Tomcat 服务器。

![](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220825194553137.png)

当我们运行 SpringBoot 的引导类时(运行 main 方法)，就会看到命令行输出的日志，其中占用 8080 端口的就是 Tomcat。

![image-20220825195359993](https://cdn.jsdelivr.net/npm/zui-xin-ban-java-web-kai-fa-jiao-cheng@1.0.1/assets1/image-20220825195359993.png)
