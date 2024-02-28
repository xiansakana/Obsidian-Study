---
title: OAuth
tags:
  - OAuth
  - Passport.js
categories: 学习
cover: "https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311222257191.jpg"
abbrlink: 6529f8fe
date: 2023-11-22 22:58:04
---

## OAuth

我们可以依靠另一方（如 Facebook）来验证某人的真实性，而不是使用密码。大多数网站让用户在本地身份验证（local authentication）或使用其他服务之间进行选择。我们可以使用 OAuth 以帮助新旧用户简化注册/登录过程。假设用户已经在浏览器中登入 Facebook，则用户只需单击一个按钮即可登入我们的网站，而不需要填写个人数据表格或是注册新的密码。

大多数网站都会使用 OAuth 来提高转化率，即访问网站者中的注册百分比。若用户觉得注册帐户非常容易，更多的用户会倾向注册帐户。每个帐户都有电子邮件地址，网站也就可以开始通过电子邮件向用户进行营销。

OAuth 2.0 是一种安全协议，协议规范能让第三方应用程式以有限的权限，透过构建资源拥有者与网路服务器间的许可交互机制，让第三方应用程式代表资源拥有者访问服务器。 OAuth 常见名词：

- Resource Owner – 资源拥有者，即网页的使用者。资源是指网页使用者的个人数据与授权。
- Client – 客户端，指的是第三方应用程序网站本身。
- Authorization Server – 授权服务器，指的是 Google, Facebook 等大型系统，也就是给予授权的服务器。
- Resource Server – 资源服务器，指的是 Google, Facebook 等大型系统中，存放资源拥有者的被保护信息的位置。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311201924672.png)

## OAuth 2.0 详细流程

1. Site A 到 Site B 注册自己，并且从 Site B 拿到 Secret 以及一个 ID。
2. 当使用者 X 告诉 Site A 去存取 X 在 Site B 上的数据，使用者 X 会被透过 Site A 的 ID 送到 Site B，并且告诉 Site B 说自己同意 Site A 来获取自己存在这里的信息。
3. Site B 接下来会把使用者 X 导回到 Site A，并且附加上一个 Authorization Code 。
4. Site A 接下来把 Authorization Code 以及在 Site B 注册时得到的 secret 送到 Site B。
5. Site B 确认了 Site A 给的 secret，确认没有其他网站冒充 Site A，并且透过 Authorization Code 确认使用者 X 确实给了 Site A 授权来存使用者 X 的信息，于是 Site B 将 security token 寄给 Site A。
6. Site A 接下来拿者 security token 到 Site B 去取得所需数据。

## OAuth 详细流程

1. 架设 Client 叫做 Spencer Cool Website，网址是www.spencercool.com。 Client 需要先到 Google 注册自己，表明自己会使用 Google OAuth，而 Google 会给 Spencer Cool Website 两组英数字码：client_id 以及 secret。也需要设定 redirect URL，是 Google 验证使用者完成后，需要将使用者导向到 Spencer Cool Website 的地方。
2. Spencer Cool Website 需要制作一个 anchor tag， 连结到 /auth/google。网页使用者点击链接，就会被送到 Google 登入页面。
3. 网页使用者登入 Google 后，Google 会在 Authorization Server 内部制作一组 code，这组 code 专属于 Spencer Cool Website 以及目前的使用者。如果目前的使用者叫做 saltedfish，我们可以先用”Spencer-saltedfish code”来代表这种 Authorization Server 制作的 code。
4. Spencer Cool Website 先把 secret 连同”Spencer-saltedfish code”带到 Authorization Server 取得 token。
5. 取得 token 后， Spencer Cool Website 用 token 向 Google Resource Server 取得使用者信息。
6. 由于认证成功，Google Server 会用 HTTP status code 302 把网页使用者重新导向到https://www.spencer.com/auth/google/redirect?code= 。其中的 code 会是 Spencer-saltedfish code。 /auth/google/redirect 这个 route 是由 Spencer Cool Website 后端来处理的。
7. Spencer Cool Website 可以在/auth/google/redirect 这个 route 中，先确认了使用者已经被验证了(可以用 passport.authenticate('google'))，再将使用者导向 profile 页面，此页面显示使用者存在 Google 的基本信息，但页面是由 Spencer cool website 所提供的。对网页使用者来说，步骤 2 到 6 都是不可见的。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img//202311201938540.png)

## Passport 套件

Passport.js 是适用于 Node.js 中，用来做身份验证的 middleware。使用 Passport.js，我们可以将 OAuth 身份验证的功能轻松集成到任何基于 Node 和 Express 的应用程序中。

Passport 库提供了 500 多种身份验证机制，包括本地身份验证、Google、Facebook、Twitter、 GitHub 、LinkedIn、 Instagram 登入等等功能。

## Passport 套件语法

因为 Passport 把所有跟 OAuth 有关的步骤都自动完成了，所以我们的程序码是从获得 token 与 resource owner 的数据后，以及 redirect 的部分开始撰写。 (内部的步骤有点繁琐且复杂，需要一些耐心。)

1. 先设定 Google Strategy 的登入方式。 Google Strategy 需要两个 parameter，第一个 parameter 是一个对象，内部含有 client id, client secret 以及一个 callback URL。第二个 parameter 是一个 function。
2. 用户端在 Google 登入页面按下登入后，Passport 会自动完成 Oauth 的步骤，取得用户的数据。取得用户的数据后，Passport 会自动调用 Google Strategy 第二个 parameter 内部的 function。此 function 的参数为 accessToken, refreshToken, profile, done。其中，profile 代表 Passport 从 Google 取得的用户数据。
3. 我们可以在此 function 内部判断，若此用户为第一次登入系统，则将从 Google 取得的用户数据存入我们系统的数据库内。
4. 在此 function 的第四个参数 done 是一个 function。我们可以将使用者信息放入 done 的第二个参数内，并且执行 done()。

在程序开发当中，Serialization 是指，将数据(或是对象)传输或储存之前，将其转换为 bytes 的过程。 Deserialization 则是指将 bytes 转换回到对象。

Passport 将这部分的实作留给开发者自己决定怎么实践 Serialization 与 Deserialization 的功能。传统上来说， Serialization 的做法，是简单的将用户端的 id 存入 session。而 Deserialization 的做法是将 session 内部的 id 拿去数据库查看数据，将 id 所指向的数据取回。

在 Passport 当中，serialization 与 deserialization 的功能名称叫做 serializeUser 与 deserializeUser。我们实作这两个功能之前，需要先使用 express-session 这个套件的功能，帮 session 做签名等功能。

以上的功能都设定好后，在 Google Strategy 内部的第二个参数的 function 所使用的第四个参数 done 被我们执行时，Passport 会透过 express-session 套件去自动执行 passport.serializeUser()。 serializeUser()参数为 user 与 done。 user 会被自动带入 Google Strategy 的 done 的第二个参数。 passport.serializeUser()也会自动带入以下的两个功能(当内部的 done()被执行时)：

1. 内部的 done()执行时，将参数的值放入 session 内部，并且在用户端设置 cookie。
2. 设定 req.isAuthenticated()为 true。

serializeUser 完成后，Passport 会执行 callback URL 的 route。进入此 route 之后，Passport 会执行 deserializeUser()。

Passport 在 deserializeUser()额外附加的一个功能，就是当 deserializeUser()内部的 done()被执行时，第二个参数会被设定在 req.user 内部。为何 Passport 会如此设计？这是因为，从使用者登入后，我们目前只有执行过 serializeUser，也就是将使用者的登入信息存入 session 内部。但使用者或许曾经登入过系统，是个旧用户，以前曾在系统内有存过其他数据。我们让使用者开始使用网站之前，最好可以把这些数据放在一个方便存取的地方。这就是为 Passport 会提供「deserializeUser()内部自动设定 req.user 的值是 done()的第二个参数的值」这个功能了。

最后，callback URL 内部会将使用者导向到网页的其他地方。在这些 route 内部，我们就可以使用 req.user 这个属性来客制化网页的内容了。以下几个为 Passport 内建的 methods：

- req.logout() – 登出使用者。 Passport 会自动删除 session。
- req.isAuthenticated() – 给定 boolean 的值，代表使用者是否被认证过。

## 整体流程

1. 使用者按下通过 Google 登陆后，会进入 Google Strategy 的 callback function。
2. 在 callback function 内部，我们可以决定是否储存使用者信息。执行 done()后，连接到第三步骤。
3. serializeUser()被执行。
4. 被导向到在 Google 设定的 callback URL，也就是 /auth/google/redirect。
5. deserializeUser()被执行。 req.user 被设定成数据库内的使用者信息。
6. /auth/google/redirect 内部导向使用者到/profile 页面。在/profile 中，req.user 是 deserializeUser()被执行的结果。
