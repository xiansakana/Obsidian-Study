---
title: REST
date: 2024-04-25T19:27:18Z
lastmod: 2024-04-25T19:27:18Z
---

# REST

表现层状态转换（英语：Representational State Transfer，缩写：REST）是 Roy Thomas Fielding 博士于 2000 年在他的 UC Irvine 博士论文中提出来的一种全球资讯网软体架构风格，目的是便于不同软体/程式在网路（例如 WWW）中互相传递资讯。

REST 是根基于超文字传输协定(HTTP)之上而确定的一组约束和属性，也就是说 REST 本身并不是一套标准，而是一套设计风格。现代 API 在制作时，通常采用的设计风格就是 REST。因此，这类型的 API 被称为是 RESTful APIs。

符合或相容于这种架构风格（简称为 REST 或 RESTful）的网路服务，允许使用者端发出以统一资源标识符（简称为 URI）存取和操作网路资源的请求，而与预先定义好的无状态操作集一致化。相对于其它种类的网路服务，例如 SOAP 服务，则是以本身所定义的操作集，来存取网路上的资源。

# RESTful API

如果我们要将服务器架构成一种服务(或是 API)，让任何使用者都可以存取数据，则可以将制作一个 RESTful API：

|HTTP Verb|Path|用途|
| ---------| -------------| ------------------------------------------------------------------|
|GET|/students|获得所有学生的数据。|
|GET|/students/:id|获得特定学生的数据。|
|POST|/students|创建一个新的学生。|
|PUT|/students/:id|修改特定学生的数据。使用者提供的资料会被变成数据库内的完整新数据。|
|PATCH|/students/:id|修改特定学生的数据。使用者只需要提供要被修改的数据即可。|
|DELETE|/students/:id|删除特定的学生|

```javascript
const express = require("express");
const app = express();
const mongoose = require("mongoose");
const Student = require("./models/student");

mongoose
  .connect("mongodb://127.0.0.1:27017/exampleDB")
  .then(() => {
    console.log("成功连接mongoDB...");
  })
  .catch((e) => {
    console.log(e);
  });

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 获得所有学生的数据。
app.get("/students", async (req, res) => {
  try {
    let studentData = await Student.find({}).exec();
    return res.send(studentData);
  } catch (e) {
    return res.status(500).send("数据搜索错误");
  }
});

// 获得特定学生的数据。
app.get("/students/:_id", async (req, res) => {
  let { _id } = req.params;
  try {
    let foundStudent = await Student.findOne({ _id }).exec();
    return res.send(foundStudent);
  } catch (e) {
    return res.status(500).send("数据搜索错误");
  }
});

// 创建一个新的学生。
app.post("/students", async (req, res) => {
  try {
    let { name, age, major, merit, other } = req.body;
    //   console.log(name, age, major, merit, other);
    let newStudent = new Student({
      name,
      age,
      major,
      scholarship: {
        merit,
        other,
      },
    });
    let savedStudent = await newStudent.save();
    return res.send({
      msd: "数据储存成功",
      savedObject: savedStudent,
    });
  } catch (e) {
    return res.status(400).send(e.message);
  }
});

// 修改特定学生的数据。使用者提供的资料会被变成数据库内的完整新数据。
app.put("/students/:_id", async (req, res) => {
  try {
    let { _id } = req.params;
    let { name, age, major, merit, other } = req.body;
    let newData = await Student.findOneAndUpdate(
      { _id },
      { name, age, major, scholarship: { merit, other } },
      {
        new: true,
        runValidators: true,
        overwrite: true,
        // 因为HTTP put request要求客户端提供所有数据，所以需要根据客户端提供的数据来更新数据库内的数据
      }
    );
    return res.send({ msg: "成功更新学生数据！", updatedData: newData });
  } catch (e) {
    res.status(400).send(e.message);
  }
});

// 修改特定学生的数据。使用者只需要提供要被修改的数据即可。
class NewData {
  constructor() {}
  setProperty(key, value) {
    if (key != "merit" && key != "other") {
      this[key] = value;
    } else {
      this[`scholarship.${key}`] = value;
    }
  }
}
app.patch("/students/:_id", async (req, res) => {
  try {
    let { _id } = req.params;
    let newObject = new NewData();
    for (let property in req.body) {
      newObject.setProperty(property, req.body[property]);
    }
    let newData = await Student.findByIdAndUpdate({ _id }, newObject, {
      new: true,
      runValidators: true,
      // 不能写overwrite: true
    });
    res.send({ msg: "成功更新学生数据！", updatedData: newData });
  } catch (e) {
    return res.status(400).send(e.message);
  }
});

// 以上修改特定学生的数据方法也可以换成如下
app.patch("/students/:_id", async (req, res) => {
  try {
    let { _id } = req.params;
    let { name, age, merit, other } = req.body;

    let newData = await Student.findByIdAndUpdate(
      { _id },
      {
        name,
        age,
        "scholarship.merit": merit,
        "scholarship.other": other,
      },
      {
        new: true,
        runValidators: true,
        // 不能寫overwrite: true
      }
    );
    res.send({ msg: "成功更新學生資料!", updatedData: newData });
  } catch (e) {
    return res.status(400).send(e.message);
  }
});

// 删除特定的学生
app.delete("/students/:_id", async (req, res) => {
  try {
    let { _id } = req.params;
    let deleteResult = await Student.deleteOne({ _id });
    return res.send(deleteResult);
    console.log(deleteResult);
  } catch (e) {
    console.log(e);
    res.status(400).send("无法删除学生数据");
  }
});

app.listen(3000, () => {
  console.log("服务器正在监听port 3000");
});
```

# RESTful Routing

如果我们的服务器不提供服务，而是网页功能，还是可以将网页服务器内部的 routing 做成 REST 风格，称为 RESTful Routing。通常来说，RESTful Routing 遵守以下的表格。当然，每个网站也可以设定自己的 Restful Routing。以下的表格与 Ruby on Rails 框架相同：

|HTTP Verb|Path|用途|
| ---------| ------------------| ------------------------------------------|
|GET|/students|获得所有学生的数据|
|GET|/students/new|回传一个包含可以用来新增学生表格的网页|
|POST|/students|创建一个新的学生|
|GET|/students/:id|获得特定学生的数据|
|GET|/students/:id/edit|回传一个包含可以用来修改学生数据表格的网页|
|PUT/PATCH|/students/:id|修改特定学生的数据|
|DELETE|/students/:id|删除特定的学生|

```javascript
const methodOverride = require("method-override");
app.use(methodOverride("_method"));

// 获得所有学生的数据。
app.get("/students", async (req, res) => {
  try {
    let studentData = await Student.find({}).exec();
    return res.render("students", { studentData });
  } catch (e) {
    return res.status(500).send("数据搜索错误");
  }
});

// 回传一个包含可以用来新增学生表格的网页
app.get("/students/new", (req, res) => {
  return res.render("new-student-form");
});

// 回传一个包含可以用来修改学生数据表格的网页
app.get("/students/:_id/edit", async (req, res) => {
  let { _id } = req.params;
  try {
    let foundStudent = await Student.findOne({ _id }).exec();
    // return res.send(foundStudent);
    if (foundStudent != null) {
      return res.status(400).render("edit-student", { foundStudent });
    } else {
      return res.status(400).render("student-not-found");
    }
  } catch (e) {
    // return res.status(500).send("数据搜索错误");
    return res.status(400).render("student-not-found");
  }
});

// 创建一个新的学生。
app.post("/students", async (req, res) => {
  try {
    let { name, age, merit, other } = req.body;
    let newStudent = new Student({
      name,
      age,
      scholarship: {
        merit,
        other,
      },
    });
    let savedStudent = await newStudent.save();
    return res.render("student-save-success", { savedStudent });
  } catch (e) {
    return res.status(400).render("student-save-fail");
  }
});

// 修改特定学生的数据。使用者提供的资料会被变成数据库内的完整新数据。
app.put("/students/:_id", async (req, res) => {
  try {
    let { _id } = req.params;
    let { name, age, major, merit, other } = req.body;
    let newData = await Student.findOneAndUpdate(
      { _id },
      { name, age, major, scholarship: { merit, other } },
      {
        new: true,
        runValidators: true,
        overwrite: true,
      }
    );
    return res.render("student-update-success", { newData });
  } catch (e) {
    res.status(400).send(e.message);
  }
});
```
