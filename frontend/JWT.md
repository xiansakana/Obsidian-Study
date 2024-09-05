# JWT

---

title: JWT
tags:

- JWT
  categories: 前端
  cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311242029724.jpg
  abbrlink: 1bb08f7a
  date: 2023-11-24 20:48:25

---

# HTTP is a stateless protocol

HTTP 是一种无状态协议(stateless protocol)。无状态协议是指，此协议不要求服务器在多个 request 期间保留有关每个用户的信息或状态。例如，如果我们服务器中的 session 储存了某个送到客户端的 session id 何时会过期，则这就是 stateful。 (但这在世界上的服务器是很常见的。之前介绍过的 express-session 这个 package 也是 stateful。)

在 HTTP 协议被设计时，之所以将 HTTP 定义成无状态协议是因为，如果服务器不需要跟踪多个请求的状态(state)，就能够简化客户端和服务器之间所需要沟通的次数与需要传输的数据量。如果要求服务器维护客户端访问的状态，则发出和回应 HTTP request 的结构将更加复杂。

# Stateful and Stateless Authentication

在验证使用者的方面，基本上可以分为两种：

1. Stateful Authentication – 成功验证客户端的身份后，应用程序生成一个 session id 发送回客户端，然后在内部数据库中创建一个 session，储存跟客户端有关的信息，例如 session id 何时过期、这个客户端可访问的资源有哪些等等的信息。
2. Stateless Authentication – 成功验证客户端的身份后，应用程序将包含跟客户端有关的信息拿去用进行签名，生成一个令牌(token)，然后将其发送回客户端。令牌生成的标准是 JWT (Json Web Token)， OpenID Connect (OIDC) 规范中描述了 JWT 的生成过程。

Stateful Authentication 的优点在于：

1. 因为服务器端可以随时将 session 内部的数据删除，所以方便做 session 管理。例如，如果在服务器直接删除 session 数据，那么客户端持有的 session Id 就完全没有意义了。
2. 如果我们后端的服务器主机只有一个，则可以很容易的管理 stateful authentication。

Stateful Authentication 的缺点在于：

1. 增加服务器开销：随着正在登录用户数的增加，这些储存的 session 也会占用越多服务器的资源。
2. 服务器的扩展差：如果 session 分布在不同的服务器上，我们需要写一个演算法来追踪特定每个用户的 session id 所指向的 session 储存在哪个服务器主机上面。例如，如果小明的 session 储存在服务器 A 主机上面，则小明往后所有的 HTTP request 都需要由服务器 A 主机来处理，因为只有服务器 A 上面才得到小明的 sesssion id 指向的资料。另外，通常服务器主机的部署会将数据复制以当作其中一个服务器故障的备案(也就是指，通常会有两个服务器主机储存一模一样的数据，被免其中某个服务器主机故障时丢失所有资料)，我们就需要写另一个算法来确保两个服务器主机上 sessions 数据的一致性。

Stateless Authentication 的优点在于：

1. 降低服务器开销：大量 session 数据不需要存储在服务器端。因此，我们可以在客户端上存储更多的用户属性，以减少访问数据库的次数，而不用担心服务器的开销问题。
2. 易于扩展：由于客户端的状态数据存储在客户端，因此 request 会被导向到哪个后端服务器的主机并不重要，只要所有后端服务器都持有相同的密钥，那么所有服务器主机都具有相同的能力来验证令牌的有效性。因此，我们可以轻易扩展大量的后端主机数量。

Stateless Authentication 的缺点在于：

1. 不能随时撤销 session：由于 session 数据存储在客户端，服务器无法删除 session 。
2. 制作难度较高：相比于 Stateful Authentication，使用 Stateless Authentication 需要更多的技术。

# JWT (Json Web Token)

JWT 验证的逻辑步骤：

在https://openid.net/specs/draft-jones-json-web-token-07.html#ExamplePlaintextJWT 可以看到，当我们要将使用者相关的资讯做成 JWT 时，会先取得两个部分。第一，制作 JWT 所使用的方法。例如，`{"typ":"JWT","alg":"HS256"}` 设定了使用的演算法是 HMAC SHA 256。第二，要被制作成 JWT 的信息。例如，

```
{"iss":"joe",
 "exp":1300819380,
 "http://example.com/is_root":true}
```

以上的信息要放入 JWT 内部。有了这两个部分之后，我们分别将上面这两个部分换成 Base64url encoding。这是一种可以跟 UTF-8 互换的编码方式。转换后，我们得到：

eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9

以及

eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly
9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ

这个个值，可以分别叫做 Part1 以及 Part2。

将 Part1 以及 Part2 串接后，放入 HMAC 算法，生成

```
dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

将 Part1, Part2 以及 Part3 串接在一起，成为 JWT：

```
eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

然后将 JWT 寄给用户。当用户将 JWT 寄回给服务器时，服务器可以先取得 JWT 中的 Part1 以及 Part2。将 Part1 从 Base64url encoding 换成 UTF-8 后，可以知道，当初服务器是使用何种算法生成 Part 3。如果 Part1 被更改过，服务器无法转换回正确的对象，或是无法匹配使用的算法时，会马上发现 Part1 有问题，于是判定 JWT 无效。

若 Part1 没有被篡改过，服务器将 Part1, Part2 都换成 Base64url encoding 后，串接起来，使用之前知道的算法，生成 HMAC 值。再去跟获得的 JWT 中的 Part3 比较，即可知道 JWT 是否被篡改过。
