---
title: Authentication
tags:
  - Authentication
  - Bcrypt
categories: 学习
cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311222256191.jpg'
abbrlink: 33d0b125
date: 2023-11-22 22:55:29
---

# Authentication and Authorizations

身分验证（英语：Authentication）是指通过一定的手段，完成对使用者身分的确认。如果我们希望我们的应用程序被世界上的任何人使用，我们需要创建一个用户身分验证系统。这将是一个用户可以注册帐户和登录的系统。 Authentication 可以透过以下的几种方式来完成：

1. 要求使用者给予系统已经储存过的帐号密码。
2. 基于共享密钥的身分验证。当使用者需要进行身分验证时，使用者通过输入或通过保管有密码的装置提交由使用者和服务器共同拥有的密码。服务器在收到使用者提交的密码后，检查使用者所提交的密码是否与服务器端储存的密码一致，如果一致，就判断使用者为合法使用者。如果使用者提交的密码与服务器端所储存的密码不一致时，则判定身分验证失败。
3. 基于公开密钥加密演算法的身分验证。通信中的双方分别持有公开密钥和私有密钥，由其中的一方采用私有密钥对特定数据进行加密，而对方采用公开密钥对数据进行解密，如果解密成功，就认为使用者是合法使用者，否则就认为是身分验证失败。使用基于公开密钥加密演算法的身分验证的服务有：SSL、数位签章等等。
4. 基于生物学特征的身分验证，使用每个人身体上独一无二的特征，如指纹、虹膜等等。
5. 多重要素验证（英语：Multi-factor authentication，缩写为 MFA）。例如，使用银行卡时，需要另外输入个人识别码，确认之后才能使用其转帐功能。登入校园网路系统时，通过手机简讯或学校指定的手机软件进行验证。
6. 开放授权（OAuth）是一个开放标准，允许使用者让第三方应用存取该使用者在某一网站上储存的私密的资源（如相片，影片，联络人列表），而无需将使用者名称和密码提供给第三方应用。

既然我们知道正在使用系统的用户是谁，并且已经做了身份验证，服务器仍需要检查该用户是否有权执行他们尝试执行的操作。这称为授权(Authorizations)。例如，在 Udemy 上面，只有讲师可以看到每个学生的学习进度与后台资料，而学生无法看到其他学生的信息。若有学生尝试存取其他学生的后台数据，服务器应该加以阻挡。

# 密码学导论

在我们的数据库中以纯文字的形式存储密码是一个非常糟糕的主意。若骇客骇入系统内部，就可以马上看到所有用户的密码。另外，员工也可以访问数据库，看到所有用户的密码，可能会有信息安全疑虑。由于很多人在多个网站上都会重复使用相同的密码(并不是一个非常好的习惯)，若我们的数据库内的密码外泄，受影响的用户的 Google、 Facebook、银行等帐户可能都会同时遭到入侵。

因此，我们希望在将密码存储到数据库之前对其进行加密或转换。我们实际上不需要加密(encrypt)密码，我们只需要对它们进行哈希(hash)处理。加密通常意味着我们可以将我们加密的内容进行解密处理，以获取原始文字。哈希处理则代表没有可逆选项。 (前面章节有提过不可逆性与雪崩效应)

如果我们将密码的哈希值(hash values)存储在数据库中，当用户端给我们密码时，我们只需要将密码拿去做哈希处理，得到哈希值后，再去跟数据库中的哈希值去比较是否相同。

在哈希函数的选择上需要特别注意。我们可以使用 SHA 家族的演算法对密码进行哈希处理，但因为 SHA 家族演算法产生哈希值的速度非常快，并不适合当作使用者密码的哈希函数。这是因为， 如果我们使用一个非常快的演算法，骇客可以非常快速地对使用者的密码做出很多猜测。骇客可以不断的猜测不同可能的密码来尝试登入系统。通常来说，骇客会参考「一万种最常见的密码」列表来猜测使用者的密码。像这样的攻击，被称为字典攻击(dictionary attack)。

另一个信息安全问题是骇客可以创建彩虹表(rainbow table)。彩虹表是一个包含许多密码(可能超过 1 亿个)及其哈希值的列表。骇客如果进入我们的资料库，可以看到许多以哈希值的形式所储存的密码。此时骇客只需要拿出彩虹表对照，就可以反推原本的使用者密码。

如果帮单一密码算出哈希值所需要的时间越长，对骇客来说，创建彩虹表的时间成本就越高。因此，我们需要使用速度慢的哈希函数。在市面上，储存密码用的哈希函数最有名的就是 Bcrypt。跟 SHA 家族相比， Bcrypt 的速度很慢。此外，我们也可以做设定让 Bcrypt 完成的速度减慢。

# 密码加盐

即使我们在将密码保存到数据库之前对密码进行了哈希函数转换，仍然不安全。骇客仍然可以用彩虹表对照出哈希函数转换前的密码。因此，我们通常会在对密码「加盐」处理。

在我们对密码做哈希处理之前，我们在密码中添加一些盐(salt)，再拿去做哈希处理，这样相同的密码在数据库中看起来会有所不同，因为相同的密码会有不同的盐，所以哈希函数算出来的哈希值也会不同。例如：

| Password | Salt | Hash Value                                                      |
| -------- | ---- | --------------------------------------------------------------- |
| hello123 | ABC  | \$2a\$12\$5mt/1KTR.rY6zW0wnT1QveUgnt25iTLhyJsDB6emW4mv6zkZ.VGfO |
| hello123 | DEF  | \$2a\$12\$JsGO0u4TzBnPVzRDOdwA4e5mQF1SeF3n9.QL9/qlkmJE8qtw7ib7G |

在数据库中，我们会存储哈希值和盐两个部分。下次当使用者给服务器密码时，服务器可以将使用者给的密码配上数据库内储存的盐，两者拿去算出哈希值。若算出的值与数据库内的哈希值相符合，则验证使用者。

这就是为什么大多数网站不会在我们忘记密码时，告诉我们密码的原因。网站服务器真的没有办法恢复密码，因为网站服务器根本就没有储存过使用者的密码。服务器所能做的就是让我们创建一个新密码。

# Bcrypt

Bcrypt 是根据 Blowfish 加密演算法所设计的密码哈希函数。在使用 Bcrypt 时，我们可以客制化 salt round。 salt round 的数字越大， Bcrypt 做哈希运算所需要完成的时间就越久，且成 2^𝑠𝑎𝑙𝑡^ ^𝑟𝑜𝑢𝑛𝑑^倍成长。也就是说，salt round 写 10，会比写 1 需要花上的时间多 2^10^=1024 倍。

使用 Bcrypt 时，输入是密码、salt round、 一个盐巴，而输出是哈希值。哈希值的形式是：

$$
$2<a/b/x/y>$[cost]$[22 character salt][31 character hash]
$$

例如，如果密码是 abc123xyz, salt round 是 12, 还有随机的盐巴，那 bcrypt 输出的结果会是：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311191822820.png)

Where:

1. \$2a$: The hash algorithm identifier (bcrypt)
2. 12: Input cost (i.e. 4096 rounds)
3. R9h/cIPz0gi.URNNX3kh2O: input salt
4. PST9/PgBkqquzi.Ss7KIUgO2t0jWMUW: the first 23 bytes of the computed 24 byte hash

这里我们发现，数据库当中也会储存盐巴以及 salt round。所以下次有人登入时，我们把他的密码拿去跟数据库内的盐巴进行 bcrypt 加密，salt round 以及演算法版本，全部一起使用，即可确认密码的正确性了！

在 Node.js 当中使用 Bcrypt 计算密码的哈希值语法有两种：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311191823415.png)

第二种：

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311191824731.png)

```javascript
// student.js
const mongoose = require("mongoose");
const { Schema } = mongoose;

const studentSchema = new Schema({
  username: {
    type: String,
  },
  password: {
    type: String,
  },
});

const Student = mongoose.model("Student", studentSchema);
module.exports = Student;
```

```javascript
require("dotenv").config();
const express = require("express");
const app = express();
const session = require("express-session");
const mongoose = require("mongoose");
const Student = require("./models/student");
const bcrypt = require("bcrypt");
const saltRounds = 12; // 8, 10, 12, 14

mongoose
  .connect("mongodb://localhost:27017/exampleDB")
  .then(() => {
    console.log("成功連結mongoDB....");
  })
  .catch((e) => {
    console.log(e);
  });

app.use(
  session({
    secret: process.env.MYSESSIONSECRETKEY,
    resave: false,
    saveUninitialized: false,
    cookie: { secure: false }, // localhost
  })
);
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const verifyUser = (req, res, next) => {
  if (req.session.isVerified) {
    next();
  } else {
    return res.send("請先登入系統");
  }
};

app.get("/students", async (req, res) => {
  let foundStudent = await Student.find({}).exec();
  return res.send(foundStudent);
});

app.post("/students", async (req, res) => {
  try {
    let { username, password } = req.body;
    let hashValue = await bcrypt.hash(password, saltRounds);
    let newStudent = new Student({ username, password: hashValue });
    let savedStudent = await newStudent.save();
    return res.send({ message: "成功新增學生", savedStudent });
  } catch (e) {
    return res.status(400).send(e);
  }
});

app.post("/students/login", async (req, res) => {
  try {
    let { username, password } = req.body;
    let foundStudent = await Student.findOne({ username }).exec();
    if (!foundStudent) {
      return res.send("信箱錯誤。查無使用者。");
    } else {
      let result = await bcrypt.compare(password, foundStudent.password);
      if (result) {
        req.session.isVerified = true;
        return res.send("登入成功。。。");
      } else {
        return res.send("登入失敗。。。");
      }
    }
  } catch (e) {
    return res.status(400).send(e);
  }
});

app.post("/students/logout", (req, res) => {
  req.session.isVerified = false;
  return res.send("你已經登出系統了。。。");
});

app.get("/secret", verifyUser, (req, res) => {
  return res.send("我的秘密是，我喜歡白居易的詩。");
});

app.listen(3000, () => {
  console.log("Server running on port 3000....");
});
```
