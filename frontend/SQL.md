---
title: SQL
date: 2024-04-25T19:25:47Z
lastmod: 2024-04-25T19:25:47Z
---

# 数据库管理系统 DBMS

我们为什么需要数据库？ 我们不能只将所有数据存储在 Excel 表格中吗？尽管我们可以对电子表格中的数据进行排序和过滤，但数据库具有广泛的查询功能，可以检索与选择条件匹配的所有记录，并且在多个表格中做交叉引用记录以及跨多个表格执行复杂的聚合计算。
此外，就查询资料而言，数据库比 Excel 快上许多，在资料庞大时差别会更明显。 Excel 可以处理最多大约 100 万行数据，但对于现代数据来说明显容量不足了。

数据库管理系统（英语：database management system，缩写：DBMS） 是一种为管理数据库而设计的管理系统。具有代表性的数据管理系统有：Microsoft SQL Server、 MongoDB 、MySQL 及 PostgreSQL 等。(简单来说，DBMS 就是管理数据库的软件)
数据库在概念上来说，可以被分成两种：

1. Relational Database (or SQL Database)
2. Non-Relational Database (or NoSQL Database)

Relational Database 是一种存储并提供对彼此相关的数据点的访问的数据库。例如，一家娱乐公司有一个数据库来存储他们所有的艺术家和歌曲数据。 所有歌曲都有一位或多于一位作家，所有作家都有一首或多于一首歌曲。 因此，该数据库的每个表格之间是有关连的。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311111807687.png)

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311111807969.png)

几十年来，SQLite、PostgreSQL、MySQL 和 SQL Server 等关系数据库已成为数据存储的热门选择。近几年来，包括 MongoDB 和 Redis 在内的 NoSQL 数据库受到青睐。

![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202311111808138.png)

# 增删查改 CRUD

增删查改(英语：CRUD)，全称增加(Create，意为“建立”)、删除(Delete)、查询(Read，意为“读取”)、改正(Update，意为“更新”)，是在 DBMS 当中，一连串常见的操作行为。

- 增删查改除了常用于 SQL 资料库之外，也在与网站的 API 埠口时常使用。在 Restful API 的制作时，会再次使用。但网站的 API 埠口使用 HTTP 协定传送通讯，所以原本的“增删查改”所对应的英文词汇会因此而改名，而不再对应 CRUD。 比如“查”不再是 Read，而改为 GET；“增”不再是 Create，而改为 POST；“改”不再是 Update，而改为 PUT 等等。
- 英语中因为 CRUD 比中文所对应的 CDRU 易读易记而将“删除”（Delete）放置于最后。但是英文小写的 crud，是指渣滓、水垢、腐蚀污泥，或是恶心的东西。

# Keys

关系键(keys)是关联式数据库的重要组成部分。关系键是一个表中的一个或几个属性，用来标识该表的每一行或与另一个表产生联络。在 DBMS 当中，主要的 keys 有：

1. 主键 (英语：primary key) – 是数据库表中对储存数据对象予以唯一和完整标识的数据列或属性的键。一笔数据只能有一个主键(但可以由两个以上的行组成 primary key)，且主键的取值不能缺失，即不能为空值（Null）。
2. 外键 (Foreign Key) – 是指向其他表格的主键的栏位，用于确定两张表格的关联性。
3. 自然键 (natural key) –若使用在真实生活中唯一确定一个事物的标识，来当作数据库的 primary key，则此 primary key 可被称作是 natural key。例如，身份证号可以当作数据库的 natural key。
4. 代理键(surrogate key) – 相对于 natural key，在当数据表格中的所有现有栏位都不适合当主键时，例如数据太长，或是意义层面太多，就会制作一个无意义的栏位来代为作主键。
5. 复合主键(composite key) – 当数据表的主键(Primary Key)如果是由多个栏位组成，则称为 composite key。

# SQL

SQL (Structured Query Language，结构化查询语言) 是一种特定目的程式语言，用于对关联式数据库管理系统 (Relational DBMS, or RDBMS)下达指令。 SQL 在 1987 年成为国际标准化组织（ISO）标准。

虽然有这一标准的存在，但大部分的 SQL 代码在不同的数据库系统中并不具有完全的跨平台性。也就是说，虽然 SQL 这门程式语言可以用来操作 DBMS，但每个 DBMS 所接受的 SQL 语法有些微差异。例如，用来操作 MySQL 这个 DBMS 的 SQL 程式码不能全部拿去用来操作 Microsoft SQL Server 这个 DBMS。

# SQL Data Types

|Data Types|Bytes|Description|
| -------------| -----------------| -------------------------------------------------------------------------------------------------------------------------|
|INT|4 bytes|数据范围是-2<sup>31</sup>~~2~~​ ~~&lt;sup&gt;~~​~~31~~​ ~~&lt;/sup&gt;~~​ ~~-1 (-2147483648~~2147483467)|
|DECIMAL(p, s)|视精确度而定|p 代表 total digits，s 代表小数点后的 digits。例如 153.23，p 是 5，s 是 2。数据范围是-10<sup>38</sup>+1~10<sup>38</sup>-1|
|VARCHAR(n)|变动长度，max=2GB|数据范围是 1~2<sup>21</sup>-1|
|DATETIME|8 bytes|数据范围是 1753/1/1~9999/12/31 ex: 2008-11-27 08:08:08.888|

# SQL 基本语法

在 SQL 中，创造新表格的语法为：

```sql
CREATE TABLE table_name (column1 datatype,    column2 datatype,    column3 datatype,   ....);
```

若要得到 SQL 的表格信息，可以用：

```sql
DESCRIBE table_name
```

若要在表格当中新增数据，则语法为：

1. 指定 column name 和要插入的值：

   ```sql
   INSERT INTO table_name (column1, column2, column3, ...)
   VALUES (value1, value2, value3, ...);
   ```
2. 如果要为表格的所有 column 添加值，则无需指定 column name。但是，需要确保值的顺序与表中 column 的顺序相同：

   ```sql
   INSERT INTO table_name
   VALUES (value1, value2, value3, ...);
   ```

若要修改表格中的现有记录，语法为：

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

> 更新表中的记录时要小心！注意 UPDATE 语句中的 WHERE。 WHERE 可以指定应该更新哪些记录。如果省略 WHERE，表中的所有记录都将被更新！

若要删除表格中的现有记录，语法为：

```sql
DELETE FROM table_name WHERE condition;
```

删除表中的记录时也要小心！如果省略 WHERE ，表中的所有记录都将被删除！ DELETE 语法只能够删除表格中的资料，但表格本身依然存在。若要删除表格，则必须使用语法：

```sql
DROP TABLE table_name;
```

查询表格中的数据时，常用语法为：

```sql
SELECT column1, column2, ... FROM table_name;
```

如果要选择表中所有的 column，可使用：

```sql
SELECT * FROM table_name;
```

ORDER BY 关键字用于对查询结果按升序或降序进行排序(默认按升序对记录进行排序)：

```sql
SELECT column1, column2, ... FROM table_nameORDER BY column1 (ASC|DESC), column2 (ASC|DESC), …;
```

查询表格中的数据时，WHERE 可用于过滤记录：

```sql
SELECT column1, column2, ...FROM table_nameWHERE condition;
```

WHERE 中可以使用以下运算符：=, <, <=, >, >=, <>, IN, BETWEEN, != 等等。

JOIN 用于根据两个或多个表之间的相关 column 的组合。 JOIN 的语法为：

```sql
SELECT column1, column2, ...
FROM table1
JOIN table2 ON table1.columnName = table2.columnName;
```

> 在 JOIN 两个数据表时，若不指定任何结合条件(也就是不写 JOIN ON，而是只写 JOIN)，则合并的结果为两个数据表间的笛卡儿乘积(Cartesian Product)，也就是两个数据表中所有的可能组合。

# SQL 与 NoSQL 比较

关系型数据库主要有以下优点：

1. 由于关系型数据库改变表格架构较为困难，通常会保持数据的一致性。
2. 数据库内的数据表连结性高，可以进行 Join 等复杂查询。
3. 产品成熟度高、稳定性也高，经过多年发展，较少 bug 需要处理，且提供报表生成等商业功能。

缺点是：

1. 扩展困难。关系型数据库通常会垂直扩展，单台服务器要持有整个数据库来确保可靠性与数据的持续可用性。这样做的代价就是非常昂贵、扩展受到限制。
2. 成本高：企业级数据库的 License 价格很惊人，并且随着系统的规模，而不断上升。
3. 读写慢：这种情况主要发生在数据量达到一定规模时，由于关系型数据库的系统逻辑非常复杂(MySQL uses both B-Tree, B+Tree, and HASH indexes )，且有可能死锁( Deadlock)的并发问题，所以其读写速度下滑非常严重。

NoSQL 的优点有：

1. 可扩展性：NoSQL 数据库一般的设计都能透过硬体的分散式丛集来向外扩展，而不必藉由增加昂贵和重量级的服务器来进行垂直扩展。云端服务器供应商通常将这些操作处理成全受管服务。
2. 快速的读写：主要例子有 Redis，只在 RAM 操作，使得其性能非常出色，每秒可以处理超过 10 万次读写操作。 Redis 数据库的操作，在所有数据都在 RAM 的前提之下，增删查改都是 O(1)的时间复杂度，不受数据数量影响。
3. 低廉的成本：这是 NoSQL 数据库共有的特点，因为主要都是开源软件，没有昂贵的 License 成本。

NoSQL 的缺点是：

1. 不提供对 SQL 的支持：因为不支持 SQL 这样的传统数据库，将会对用户产生一定的学习和应用迁移成本。
2. 支持的特性不够丰富：现有产品所提供的功能都比较有限，也不像 MS SQL Server 和 Oracle 那样能提供各种附加功能，比如自通生成报表等。
3. 现有产品的不够成熟：大多数产品都还处于初创期，和关系型数据库几十年的完善不可同日而语。
