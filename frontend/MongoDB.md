---
title: MongoDB
tags:
  - MongoDB
  - 数据库
  - 后端
categories: 学习
cover: "https://cdn.cbd.int/xiansakana-blog-img/202311140937414.jpg"
abbrlink: 8ead567e
date: 2023-11-14 09:36:39
---

## JSON and BSON

JavaScript Object Notation，通常称为 JSON，在 2000 年代初期由 JavaScript 创建者 Douglas Crockford 定义为 JavaScript 语言的一部分。 JavaScript 对象是简单的容器，其中一个 String key 可以映射到一个 value （这个 value 可以是数字、String，甚至是另一个对象）。这种简单的语言特性允许 JavaScript 对象在文件中非常简单地表示：

JSON 的普遍性使其成为 MongoDB 在开发时的数据结构第一选择。但是，有几个问题使 JSON 不太适合在数据库内部使用：

1. JSON 是基于纯文字的格式，而纯文字在解析上很缓慢。
2. JSON 的高可读性并无法节省储存空间，另一个用 JSON 制作数据库会引发的问题。
3. JSON 仅支持有限数量的基本 data types。

为了使 MongoDB 提高性能，人们发明了 BSON 来解决以上的问题。 BSON 基于 JSON，但仍然具有高性能和通用性。 BSON 代表 Binary JSON，BSON 的二进制结构对 data types 和长度信息进行编码，从而可以更快地对其进行解析，针对速度、空间和灵活性进行了优化。

例如，将 JSON 的{“hello”: “world”} 换成 BSON 会得到
\x16\x00\x00\x00\x02 hello\x00\x06\x00\x00\x00world\x00\x00

|                   | JSON                           | BSON                                                                                   |
| ----------------- | ------------------------------ | -------------------------------------------------------------------------------------- |
| Encoding          | UTF-8 String                   | Binary                                                                                 |
| Data Type Support | String, Boolean, Number, Array | String, Boolean, Number (Integer, Float, Long, Decimal128...), Array, Date, Raw Binary |
| Readability       | Human and Machine              | Machine Only                                                                           |

## MongoDB Shell (mongosh)

MongoDB Shell (mongosh)是一个功能齐全的 JavaScript 和 Node.js 16.x REPL(Read, Evaluate, Print, Loop) 环境，用于与 MongoDB 部署进行交互运作。我们可以使用 MongoDB Shell 直接用数据库测试查询和操作。

在 MongoDB 当中，我们可以一次拥有数个 databases。每个 database 内部可以有数个 collections。 Collections 等同于是 MySQL 当中的一个表格。

![](https://cdn.cbd.int/xiansakana-blog-img/202311131431197.png)

在 MongoDB Shell 当中，常用的指令有：

- show dbs - 展示所有的数据库。
- db -展示目前所在的数据库。
- use <db> - 将当前所在的数据库切换到 <db>。若 <db>不存在，则制作出并且切换到 <db>。
- show collections - 打印当前所在的数据库的所有 collections。

在 MongoDB 中，document 指的是数据的基本单元或基本构建块。在 MongoDB Shell 当中，跟 CRUD 有关的常见语法有：

- db.collection.insertOne(<document>) – 参数为一个物件，功能为在 collection 当中新增一个 document。

  ```sql
  db.students.insertOne({name:"Grace",age:27,major:"Computer Science",scholarship:{merit:3000,other:1500}})
  ```

- db.collection.insertMany( [ <document 1> , <document 2>, ...) – 参数为一个由物件组成的 array，功能为在 collection 当中新增一个或一个以上的 document。

  ```sql
  db.students.insertMany([{name:"Mike Huang",age:28,magjor:"Chemistry",scholarship:{merit:0,other:1500}},{name:"Spence Kwan",age:35,major:"Computer Science",scholarship:{merit:3000,other:2000}}])
  ```

- db.collection.insert( <document or array of documents>) – 参数为一个物件或是一个由物件组成的 array，功能为在 collection 当中新增一个或一个以上的 document。

- db.collection.find(<query>) – 找寻 collection 中的资料。 Query 的 data type 是 object，用来过滤找寻的资料。若想要获得 collection 中的所有资料，query 可以是 empty object，或者执行 find()时不给定任何 argument 即可。

  ```sql
  db.students.find({major:"Computer Science"})
  db.students.find({"scholarship.merit":{$lt:1000}})
  ```

- db.collection.updateOne( <filter>, <update>) – 更新 collection 中第一笔找到的资料。 Filter 的 data type 是 object，是指更新的选择标准，与 find()中 query 功能一模一样。 Update 的 data type 也是 object，我们可以将被修改资料的新数据放在 update 这个位置。

  ```sql
  db.students.updateOne({name:"Spence Kwan"},{$set:{name:"Spencer Kwan",age:36}})
  db.students.updateOne({name:"Spencer Kwan"},{$set:{age:37},$currentDate:{lastModified:true}})
  ```

- db.collection.updateMany(<filter>,<update>) – 功能也是更新 collection 中的资料，但可以一次性的更新 collection 中所有符合 filter 的多笔资料。

  ```sql
  db.students.updateMany({major:"Computer Science"},{$set:{major:"CS"}})
  ```

- db.collection.deleteOne(<filter>) – 可以删除 collection 内的第一笔符合 filter 的资料。

  ```sql
  db.students.deleteOne({name:"Mike Huang"})
  ```

- db.collection.deleteMany(<filter>) – 删除 collection 内所有符合 filter 的资料。
