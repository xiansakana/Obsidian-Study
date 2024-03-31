---
title: Mongoose
tags:
  - Mongoose
  - 数据库
  - 后端
categories: 后端
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311140944975.jpg
abbrlink: aaac2584
date: 2023-11-14 09:43:11
---

# Mongoose

若要在程式语言中使用或存取 MongoDB，我们需要工具让数据库可以跟 JavaScript 程式码连结。这类工具的特点就是，能够将 JavaScript 中的 Object 转换成 MongoDB 当中的 document，因此，这类的工具叫做 object-document mapping (ODM)。在市面上，众多 MongoDB 的 ODM 当中，最热门的叫做 mongoose。

使用 ODM 的好处在于：

1. 数据库的结构能被追踪。通常数据库的结构经过改变之后，很难退回到未改变的结构。使用 ODM 可以将数据库的结构写在程式码内部，方便追踪与更改。
2. 通常 ORM/ODM 会内建保护机制或是保护型语法，所以使用 SQL 数据库时，就不用担心 SQL Injection 之类的攻击。
   让 Project 更符合 MVC 模型。 Mongoose 是 model，用来与 MongoDB 互动获得或改变数据、View 是 EJS，Controller 则是 app.js 来担任。

> SQL 数据库使用的工具叫做 ORM ，而 NoSQL 数据库使用的工具叫做 ODM。两者功能相同但名称不同。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311132010171.png)

# Model and Schema

在 Mongoose 中，两个 keyword 需要记得：

1. Schema – 每个 Schema 映射到一个 MongoDB 中的 Collection，并且定义该 Collection 中 document 的架构，包含默认值、最大长度、最大值、最小值等等。
2. Model – 包装 Schema 的容器。在数据库中，Schema 所对应到的 Collection 提供了一个接口，可以用 Model 来对 Collection 进行新增、查询、更新、删除记录等功能。

Model 就像是 SQL 当中的 table，而 Schema 是 create table 的步骤。

Schema 的语法为：

```java
import mongoose from "mongoose";
const { Schema } = mongoose;
const blogSchema = new Schema({
  title: String, // String is shorthand for {type: String},
  date: { type: Date, default: Date.now },
  meta: { votes: Number, favs: Number },
});
```

在 blogSchema 的 constructor 当中，参数为一个对象，而对象的每个 key 都定义了 blog collection 当中的 document 的属性。并且在对象的每个 key 赋予的 value 为一个属性，为 SchemaType 的对象。常见的 SchemaType 有：String, Number, Date, Boolean, ObjectId, Array, Decimal128, Map 等等。

Model 的语法为：

```javascript
const Blog = mongoose.model("Blog", blogSchema);
```

特别注意，mongoose.model()的第一个参数是 String，为我们的 collection 名称。这里使用的 String 必须为大写英文字母开头，且为单数形式。例如，如果我们希望制作名为 students 的 collection，就必须使用’Student’，而如果想要制作名为 people 的 collection，就必须使用’Person’。 (Mongoose 会自动转换，我们需要确保提供正确的拼字即可)

```javascript
const express = require("express");
const app = express();
const mongoose = require("mongoose");
const { Schema } = mongoose;

app.set("view engine", "ejs");

mongoose
  .connect("mongodb://127.0.0.1:27017/exampleDB")
  .then(() => {
    console.log("成功连接mongoDB");
  })
  .catch((e) => {
    console.log(e);
  });

const studentSchema = new Schema({
  name: String,
  age: Number,
  major: String,
  scholarship: {
    merit: Number,
    other: Number,
  },
});

const Student = mongoose.model("Student", studentSchema);
const newObject = new Student({
  name: "Esther",
  age: 27,
  major: "Mathematics",
  scholarship: {
    merit: 6000,
    other: 7000,
  },
});

newObject
  .save()
  .then((saveObject) => {
    console.log("数据已经储存完毕，储存的数据是：");
    console.log(saveObject);
  })
  .catch((e) => {
    console.log(e);
  });

app.listen(3000, () => {
  console.log("服务器正在监听port3000...");
});
```

# CRUD in Mongoose

常见在 Mongoose 中，跟 CRUD 有关的操作是：

- document.save() – 在 MongoDB 中储存 document。 returns a promise。

  ```javascript
   doc.save().then(savedDoc => { savedDoc === doc; // true });
  ```

在 Mongoose 当中，许多 methods 的 return type 都是「Query」。 Query 是一种 Mongoose 特有的 Class（根据 documentation，Query 是一种 thenable object，但不是 Promise），提供用于 find、update 和 delete documents 等操作提供 method chaining。如果要让这些 methods 的 return type 变成 promise，可以让 Query 执行.exec()即可。

- Model.find(filter) – 找到所有符合 filter 条件的对象。参数一个对象，用来提供过滤寻找的条件。

  ```javascript
  app.get("/", async (req, res) => {
    try {
      let data = await Student.find().exec();
      console.log(data);
      res.send(data);
    } catch (e) {
      console.log(e);
    }
  });
  ```

  ```javascript
  Student.find({ "scholarship.merit": { $gte: 5000 } })
    .then((data) => {
      console.log(data);
    })
    .catch((e) => {
      console.log(e);
    });
  ```

- Model.findOne(filter) –找到第一个符合 filter 条件的对象。参数一个对象，用来提供过滤寻找的条件。

  ```javascript
  app.get("/", async (req, res) => {
    try {
      let data = await Student.findOne({ name: "Grace" }).exec();
      console.log(data);
      res.send(data);
    } catch (e) {
      console.log(e);
    }
  });
  ```

- Model.updateOne(filter, update, options) –找到第一个符合 filter 条件的对象，并且将数据更新 update 的值。 filter, update 这两个 parameter 的数据类型都是 object。 .then()内部的 callback 被执行时，带入的 parameter 是更新操作讯息，例如，acknowledged, modifiedCount, upsertedId 等等。 Options 对象可设定 runValidators，若 update 对象的值不符合 Schema 的设定，则出现 error。

  ```javascript
  Student.updateOne({ name: "Esther" }, { name: "Esther Lam" })
    .exec()
    .then((msg) => {
      console.log(msg);
    })
    .catch((e) => {
      console.log(e);
    });

  // Student.find({})
  //   .exec()
  //   .then((data) => {
  //     console.log(data);
  //   })
  //   .catch((e) => {
  //     console.log(e);
  //   });
  ```

  ```javascript
  const studentSchema = new Schema({
    name: String,
    age: Number, //{ type: Number, min: [0, "年龄不能小于0"] },
    major: String,
    scholarship: {
      merit: Number,
      other: Number,
    },
  });

  Student.updateOne(
    { name: "Esther Lam" },
    { age: -100 },
    { runValidators: true }
  )
    .exec()
    .then((msg) => {
      console.log(msg);
    })
    .catch((e) => {
      console.log(e);
    });
  // 会出现error
  // age: ValidatorError: 年龄不能小于0
  ```

- Model.updateMany(filter, update, options) – 找到所有符合 filter 条件的对象，并且将符合 filter 的每一笔数据，更新 update 的值。 filter, update 这两个 parameter 的数据类型都是 object。 .then()内部的 callback 被执行时，带入的 parameter 也是更新操作讯息。 Options 可设定 runValidators。

- Model.findOneAndUpdate(condition, update, options) –找到第一个符合 condition 条件的对象，并且更新 update 的值。 condition, update, options 这三个 parameter 的数据类型都是 object。 .then()内部的 callback 被执行时，若在 options 内部有表明 new 属性为 true，则.then()内部的 callback 被执行时，带入的 parameter 会是更新完成了 document。反之， 没有表明 new 是 true，或设定 new 是 false (这是预设值)，则 callback 的 parameter 会是更新前的 document。 Options 中也可设定 runValidators。

  ```javascript
  Student.findOneAndUpdate(
    { name: "Grace" },
    { name: "Grace Xie" },
    { runValidators: true, new: true }
  )
    .exec()
    .then((newData) => {
      console.log(newData);
    })
    .catch((e) => {
      console.log(e);
    });

  // {
  //     scholarship: { merit: 3000, other: 1500 },
  //     _id: new ObjectId('65528e22afaf4b1c4d102ba6'),
  //     name: 'Grace Xie',
  //     age: 27,
  //     major: 'CS'
  // }
  ```

  > updateOne()与 findOneAndUpdate()的使用时机为何？ updateOne()是在当我们不需要更新后的 document 时，并且希望节省一点数据库操作时间和通讯流量的话，可以用的选择。但其他情况下， findOneAndUpdate()提供更新完成的 document 是非常实用的功能。

- Model.deleteOne(conditions) – 从 Collections 中删除与 conditions 匹配的第一个 document。此 method 会 return 一个具有 deletedCount 属性的 object。

  ```javascript
  Student.deleteOne({ name: "Wilson" })
    .exec()
    .then((msg) => {
      console.log(msg);
    })
    .catch((e) => {
      console.log(e);
    });
  ```

- Model.deleteMany(conditions) – 从 Collections 中删除与 conditions 匹配的所有 documents。此 method 会 return 一个具有 deletedCount 属性的 object。

其他的所有操作，请参考 Mongoose CRUD 页面： https://mongoosejs.com/docs/queries.html

# Schema Validators

如果我们希望 Collections 中的数据，在被存放到 Collections 之前，可以经过验证(例如，员工数据库的薪资栏位不能小于 0)，则可以在 Schema 中设定每个属性的验证器(validators)来达到此功能。

通常来说，Schema 属性的设定语法是：name: String，但也可以写成是：name: {type: String}。因为 validator 本身是 Schema 属性设定时，对象的一个属性，所以加入 validator 的语法会变成：

```javascript
name:{  type: String,  required: true}
```

因为每种 data type 所通用的验证器不同，所以我们需要将每种验证器归类到各自的 data type 上。对于所有的 data type 都适用的验证器有：

1. required – 可放入一个 boolean 值，或是一个 array(包含一个值以及一个客制化的错误讯息)，或是一个 function。

   ```javascript
   const studentSchema = new Schema({
     name: { type: String, require: true },
     age: { type: Number, min: [0, "年龄不能小于0"] },
     major: { type: String, required: [true, "每个学生都需要至少一门主修"] },
     scholarship: {
       merit: Number,
       other: Number,
     },
   });
   ```

   ```javascript
   const studentSchema = new Schema({
     name: { type: String, require: true },
     age: { type: Number, min: [0, "年龄不能小于0"] },
     major: {
       type: String,
       required: function () {
         return this.scholarship.merit >= 3000;
       },
     },
     scholarship: {
       merit: Number,
       other: Number,
     },
   });
   ```

2. default – 可设定属性的预设值。

   ```javascript
   const studentSchema = new Schema({
     name: { type: String, require: true },
     age: { type: Number, min: [0, "年龄不能小于0"] },
     major: {
       type: String,
       required: function () {
         return this.scholarship.merit >= 3000;
       },
     },
     scholarship: {
       merit: { type: Number, default: 0 },
       other: { type: Number, default: 0 },
     },
   });
   ```

跟 String 有关的验证器有：

1. uppercase (boolean)

2. lowercase (boolean)

3. enum (array of strings)

   ```javascript
   const studentSchema = new Schema({
     name: { type: String, require: true },
     age: { type: Number, min: [0, "年龄不能小于0"] },
     major: {
       type: String,
       required: function () {
         return this.scholarship.merit >= 3000;
       },
       enum: [
         "Chemistry",
         "Computer Science",
         "Mathematics",
         "Civil Engineering",
         "Undecided",
       ],
     },
     scholarship: {
       merit: { type: Number, default: 0 },
       other: { type: Number, default: 0 },
     },
   });
   ```

4. minlength (number)

5. maxlength (number)

   ```javascript
   name: { type: String, require: true, maxlength: 25 }
   ```

跟 number 有关的验证器有：min, max, enum。

# Instance Method

在 Mongoose Model 当中的每笔数据都叫做 document，而 document 又叫做 instance。若我们希望某个 model 中的所有 documents 都可以使用某个 method，则可以将此 method 定义在 Schema 上。像这样定义在 Schema 上的 method 被称为 instance method。 Instance method 的语法有两种。第一种是在 Schema 内设定 methods 属性并且给予一个对象，对象内部有 methods：

```javascript
const studentSchema = new Schema(
  {
    name: { type: String, require: true, maxlength: 25 },
    age: { type: Number, min: [0, "年龄不能小于0"] },
    major: {
      type: String,
    },
    scholarship: {
      merit: { type: Number, default: 0 },
      other: { type: Number, default: 0 },
    },
  },
  {
    methods: {
      printTotalScholarship() {
        return this.scholarship.merit + this.scholarship.other;
      },
    },
  }
);

const Student = mongoose.model("Student", studentSchema); // students

Student.find({})
  .exec()
  .then((arr) => {
    arr.forEach((student) => {
      console.log(
        student.name + "总奖学金金额是" + student.printTotalScholarship()
      );
    });
  });
```

或是，第二种方式是，我们可以直接设定 Schema 的 methods 属性：

```javascript
const studentSchema = new Schema({
  name: { type: String, require: true, maxlength: 25 },
  age: { type: Number, min: [0, "年龄不能小于0"] },
  major: {
    type: String,
  },
  scholarship: {
    merit: { type: Number, default: 0 },
    other: { type: Number, default: 0 },
  },
});

studentSchema.methods.printTotalScholarship = function () {
  return this.scholarship.merit + this.scholarship.other;
};

const Student = mongoose.model("Student", studentSchema); // students

Student.find({})
  .exec()
  .then((arr) => {
    arr.forEach((student) => {
      console.log(
        student.name + "总奖学金金额是" + student.printTotalScholarship()
      );
    });
  });
```

# Static Methods

如果我们想要定义某个专属于 Schema 使用的 method，则可以使用 static method。 Static method 属于 Schema 本身，而不属于 Mongoose Model 内部的 documents。此概念来自于面向对象程式设计。 Static methods 的设置方式有以下三种：

```javascript
const studentSchema = new Schema(
  {
    name: { type: String, require: true, maxlength: 25 },
    age: { type: Number, min: [0, "年龄不能小于0"] },
    major: {
      type: String,
      required: function () {
        return this.scholarship.merit >= 3000;
      },
    },
    scholarship: {
      merit: { type: Number, default: 0 },
      other: { type: Number, default: 0 },
    },
  },
  {
    statics: {
      findAllMajorStudents(major) {
        return this.find({ major: major }).exec();
      },
    },
  }
);

const Student = mongoose.model("Student", studentSchema); // students

Student.findAllMajorStudents("Mathematics")
  .then((data) => {
    console.log(data);
  })
  .catch((e) => {
    console.log(e);
  });
```

或是直接将 methods 设定在 Schema 的 statics 属性上：

```javascript
const studentSchema = new Schema(
  {
    name: { type: String, require: true, maxlength: 25 },
    age: { type: Number, min: [0, "年龄不能小于0"] },
    major: {
      type: String,
      required: function () {
        return this.scholarship.merit >= 3000;
      },
    },
    scholarship: {
      merit: { type: Number, default: 0 },
      other: { type: Number, default: 0 },
    },
  },
  {
    statics: {},
  }
);

studentSchema.statics.findAllMajorStudents = function (major) {
  return this.find({ major: major }).exec();
};

const Student = mongoose.model("Student", studentSchema); // students

Student.findAllMajorStudents("Mathematics")
  .then((data) => {
    console.log(data);
  })
  .catch((e) => {
    console.log(e);
  });
```

或是：

```javascript
const studentSchema = new Schema(
  {
    name: { type: String, require: true, maxlength: 25 },
    age: { type: Number, min: [0, "年龄不能小于0"] },
    major: {
      type: String,
      required: function () {
        return this.scholarship.merit >= 3000;
      },
    },
    scholarship: {
      merit: { type: Number, default: 0 },
      other: { type: Number, default: 0 },
    },
  },
  {
    statics: {},
  }
);

studentSchema.static("findAllMajorStudents", function (major) {
  return this.find({ major: major }).exec();
});

const Student = mongoose.model("Student", studentSchema); // students

Student.findAllMajorStudents("Mathematics")
  .then((data) => {
    console.log(data);
  })
  .catch((e) => {
    console.log(e);
  });
```

# Mongoose Middleware

Mongoose Middleware (也称为 pre, post hooks) 是在异步函数执行期间传递控制权的函数。 Middleware 是定义在 Schema 上的。

例如，我们可以定义 schema.pre(‘save’, callbackFn)这个 Middleware。当任何与此 Schema 有关的对象要被储存之前，此 pre hook 内的 callbackFn 就会先被执行。同理，若定义 schema.post(‘save’, callbackFn)这个 Middleware，则任何与此 Schema 有关的对象被成功储存之后，此 post hook 内的 callbackFn 就会被执行。

```javascript
const fs = require("fs");
studentSchema.pre("save", () => {
  fs.writeFile("record.txt", "A new data will be saved...", (e) => {
    if (e) throw e;
  });
});
```
