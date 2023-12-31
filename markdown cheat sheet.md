# [Typora 的 Markdown 语法](https://support.typoraio.cn/zh/Markdown-Reference/)

# 标题

```markdown
# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题
```

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

# 分割线

```markdown
//分割线表示

---

---

---

<hr style="border:1px solid red;">
```

---

---

---

<hr style="border:1px solid red;">

# 字体

## 字体类型和颜色

```markdown
<font face="kaiti">这里是楷体</font>
<br/>
<font face="heiti">这里是黑体</font>
<br/>
<font face="simsun">这里是宋体</font>
<br/>
<font face="Arial">This is Arial</font>
<br/>
<font face="Arial Narrow">This is Arial Narrow</font>
<br/>
<font face="Times New Roman">This is Times New Roman</font>
<br/>
<font face="Calibri">This is Calibri</font>
<br/>
<font color="red"><b>红色加粗</b></font>
<br/>
<font style="background: linear-gradient( to right，#ff1616，#ff7716，#ffdc16,#36c945，#10a5ce，#Of0096，#a51eff，#ff1616); ">这是七色光彩背景颜色</font>
```

<font face="kaiti">这里是楷体</font>
<br/>
<font face="heiti">这里是黑体</font>
<br/>
<font face="simsun">这里是宋体</font>
<br/>
<font face="幼圆">这里是幼圆</font>
<br/>
<font face="华文彩云">这里是华文彩云</font>
<br/>
<font face="Arial">This is Arial</font>
<br/>
<font face="Arial Narrow">This is Arial Narrow</font>
<br/>
<font face="Times New Roman">This is Times New Roman</font>
<br/>
<font face="Calibri">This is Calibri</font>
<br/>
<font color="red"><b>红色加粗</b></font>
<br/>
<font style="background: linear-gradient( to right, #ff1616, #ff7716, #ffdc16, #36c945, #10a5ce, #Of0096, #a51eff, #ff1616); ">这是七色光彩背景颜色</font>

## 其他

```markdown
==高亮==
~~删除线~~
**粗\*\***体**
_斜体_
**_粗_\***\*_斜_**_**体**_
<u>下划线</u>
:smile:
$\theta=x^2$
```

==高亮==
~~删除线~~
**粗\*\***体**
_斜体_
**_粗_\***\*_斜_**_**体**_
<u>下划线</u>
😄
[emoji 链接](https://unicode.org/emoji/charts/full-emoji-list.html)
$\theta=x^2$

# 转义

```markdown
\\ 反斜杠
\` 反引号 \* 星号
\_ 下划线
\{\} 大括号
\[\] 中括号
\(\) 小括号
\# 井号
\+ 加号
\- 减号
\. 英文句号
\! 感叹号
```

\\ 反斜杠
\` 反引号 \* 星号
\_ 下划线
\{\} 大括号
\[\] 中括号
\(\) 小括号
\# 井号
\+ 加号
\- 减号
\. 英文句号
\! 感叹号

# 引用

```markdown
//一级引用用一个>来表示
//二级引用用两个>来表示
//三级引用用三个>来表示
```

> 一级引用

> > 二级引用

> > > 三级引用

# 脚注

```markdown
一键三连[^1]
```

一键三连[^1]

[^1]: 点赞、投币、收藏

# 列表

## 有序列表

```markdown
//有序列表

## 有序列表

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3
   1. 子序列 1
   2. 子序列 2
   3. 子序列 3
```

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3
   1. 子序列 1
   2. 子序列 2
   3. 子序列 3

## 无序列表

```markdown
//无序列表

## 无序列表

- 无序列表 1

* 无序列表 2
  - [ ] 子序列 1
  - [ ] 子序列 2
  - [x] 子序列 3

- 无序列表 3
  - 子序列 1
  * 子序列 2
  - 子序列 3
```

- 无序列表 1

* 无序列表 2
  - [ ] 子序列 1
  - [ ] 子序列 2
  - [x] 子序列 3

- 无序列表 3

  - 子序列 1

  * 子序列 2

  - 子序列 3

# 数学公式

```markdown
$$
\frac{partial f}{\partial x} = \sqrt[3]{a_1}x
$$

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt \tag{2}
$$

$$
\lim_{a\to\infty}a=\infty\lim_{b\rightarrow-\infty}=-\infty \tag{3}
$$

$$
x(t)=\sum_{k=-\infty}^{\infty}a_ke^{jkw_0t} \tag{4}
$$
```

$$
\frac{\partial f}{\partial x} = \sqrt[3]{a_1}x \tag{1}
$$

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt \tag{2}
$$

$$
\lim_{a\to\infty}a=\infty\lim_{b\rightarrow-\infty}=-\infty \tag{3}
$$

$$
x(t)=\sum_{k=-\infty}^{\infty}a_ke^{jkw_0t} \tag{4}
$$

```markdown
$$
\vec{F}=ma\\
\leq\\
\geq
$$
```

$$
\vec{F}=ma\\
a\leq b\\
b\geq c
$$

## 希腊字母

```markdown
$$
\alpha, \beta, \gamma, \delta, \epsilon\\
\varepsilon, \eta, \theta, \vartheta, \kappa\\
\pi, \rho,\lambda, \mu, \phi\\
\varphi, \omega, \tau, \psi, \Psi\\
\xi,\iota, \zeta, \nu, \upsilon\\
\sigma, \chi, \O, \Xi, \Upsilon
$$
```

$$
\alpha, \beta, \gamma, \delta, \epsilon\\
\varepsilon, \eta, \theta, \vartheta, \kappa\\
\pi, \rho,\lambda, \mu, \phi\\
\varphi, \omega, \tau, \psi, \Psi\\
\xi,\iota, \zeta, \nu, \upsilon\\
\sigma, \chi, \O, \Xi, \Upsilon
$$

## 矩阵

```markdown
$$
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix} \tag{1}
$$
```

$$
\begin{Bmatrix}
  a & b \\
  c & d
\end{Bmatrix} \tag{1}
$$

```markdown
$$
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix} \tag{2}
$$
```

$$
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix} \tag{2}
$$

```markdown
$$
\begin{vmatrix}
a & b\\
c & d
\end{vmatrix} \tag{3}
$$
```

$$
\begin{vmatrix}
a & b\\
c & d
\end{vmatrix} \tag{3}
$$

```markdown
$$
\left\{
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
\right\} \tag{4}
$$
```

$$
\left\{
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
\right\} \tag{4}
$$

```markdown
$$
\left[
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
\right] \tag{5}
$$
```

$$
\left[
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
\right] \tag{5}
$$

```markdown
$$
\left(
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
\right) \tag{6}
$$
```

$$
\left(
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
\right) \tag{6}
$$

```markdown
$$
\begin{Bmatrix}
1 & 2 & \cdots & 5\\
6 & 7 & \cdots & 10\\
\vdots & \vdots & \ddots & \vdots\\
\alpha & \alpha+1 & \cdots & \alpha+4
\end{Bmatrix}\tag{7}
$$
```

$$
\begin{Bmatrix}
1 & 2 & \cdots & 5\\
6 & 7 & \cdots & 10\\
\vdots & \vdots & \ddots & \vdots\\
\alpha & \alpha+1 & \cdots & \alpha+4
\end{Bmatrix}\tag{7}
$$

## 多行等式对齐

```markdown
$$
\begin{aligned}
a &= b + c \\
  &= d + e + f
\end{aligned}
$$
```

$$
\begin{aligned}
a &= b + c \\
  &= d + e + f
\end{aligned}
$$

## 方程组、条件表达式

```markdown
$$
\begin{cases}
3x + 5y +  z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
$$
```

$$
\begin{cases}
3x + 5y +  z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
$$

```markdown
$$
f(n) =
\begin{cases}
n/2,  & \text{if }n\text{ is even} \\
3n+1, & \text{if }n\text{ is odd}
\end{cases}
$$
```

$$
f(n) =
\begin{cases}
n/2,  & \text{if }n\text{ is even} \\
3n+1, & \text{if }n\text{ is odd}
\end{cases}
$$

## 间隔

```markdown
//紧贴 + 无空格 + 小空格 + 中空格 + 大空格 + 真空格 + 双真空格

$$
a\!b + ab + a\,b + a\;b + a\ b + a\quad b + a\qquad b
$$
```

$$
a\!b + ab + a\,b + a\;b + a\ b + a\quad b + a\qquad b
$$

## 表格

### 简易表格

```markdown
$$
\begin{array}{|c|l|r|}
  \hline 1&20&3000\\
  \hline 40&500&60000\\
  \hline 7000&80000&9000000\\
  \hline
\end{array}
$$
```

$$
\begin{array}{|c|l|r|}
  \hline 1&20&3000\\
  \hline 40&500&60000\\
  \hline 7000&80000&9000000\\
  \hline
\end{array}
$$

```markdown
|参数|解释|  
|:-:|:-:|//居中
//|-:|-:|右对齐
//|:-|:-|左对齐
|enable|是否启用 nav 左侧项目按钮，仅控制左侧项目按钮|
|travelling|是否启用 nav 开往按钮|
```

|    参数    |                     解释                      |
| :--------: | :-------------------------------------------: |
|   enable   | 是否启用 nav 左侧项目按钮，仅控制左侧项目按钮 |
| travelling |             是否启用 nav 开往按钮             |

### 真值表

```markdown
$$
\begin{array}{cc|c}
         A&B&F\\
  \hline 0&0&0\\
         0&1&1\\
         1&0&1\\
         1&1&1\\
\end{array}
$$
```

$$
\begin{array}{cc|c}
         A&B&F\\
  \hline 0&0&0\\
         0&1&1\\
         1&0&1\\
         1&1&1\\
\end{array}
$$

# 甘特图

````markdown
```mermaid
    gantt
        dateFormat  YYYY-MM-DD
        title 软件开发甘特图
        section 设计
        需求                      :done,    des1, 2014-01-06,2014-01-08
        原型                      :active,  des2, 2014-01-09, 3d
        UI设计                    :         des3, after des2, 5d
        未来任务                   :         des4, after des3, 5d
        section 开发
        学习准备理解需求                      :crit, done, 2014-01-06,24h
        设计框架                             :crit, done, after des2, 2d
        开发                                 :crit, active, 3d
        未来任务                              :crit, 5d
        耍                                   :2d
        section 测试
        功能测试                              :active, a1, after des3, 3d
        压力测试                               :after a1  , 20h
        测试报告                               : 48h
```
        gantt
        dateFormat  YYYY-MM-DD
        title Work Plan

        FYP Topic Select                      :done,    des1, 2022-06-06,2022-09-15
        Preliminary Report                      :done,  des2, 2022-10-05,2022-10-30
        Final Report Framework: done, 2022-11-18, 2022-12-01
        Literature Reading                    :active,          2022-09-20,2023-03-18
        Interim Report :done, 2022-12-25, 2023-01-13
        Experiment Performing :active, 2022-11-23, 2023-03-01
        Data Analysis: 2023-02-22, 2023-04-10

        Final Report: 2023-03-01, 2023-04-28

        Oral Presentation: 2023-05-15, 2023-05-19
````

# 超链接

```markdown
[B 站](https://www.bilibili.com)

[原神](./QQ截图20220110160242.png)

[【静止画 MAD】FRIEND(https://i0.hdslb.com/bfs/archive/3fb28cc5eef41d048083c48e7539bdf9a7864440.jpg@560w_350h_100Q_1c.webp)

[【静止画 MAD】FRIEND](https://www.bilibili.com/video/BV1uL411W7HT)

<iframe src="https://player.bilibili.com/player.html?aid=461536590&bvid=BV1uL411W7HT&cid=368370249&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" &danmaku="1" width="90%" height="360"> </iframe>
```

[B 站](https://www.bilibili.com)

[【静止画 MAD】FRIEND](https://i0.hdslb.com/bfs/archive/3fb28cc5eef41d048083c48e7539bdf9a7864440.jpg@560w_350h_100Q_1c.webp)

[【静止画 MAD】FRIEND](https://www.bilibili.com/video/BV1uL411W7HT)

  <!--<iframe src="https://player.bilibili.com/player.html?aid=461536590&bvid=BV1uL411W7HT&cid=368370249&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" &danmaku="1" width="90%" height="360" autoplay="false"> </iframe>-->

# 图片

```markdown
//在线图片
![【静止画MAD】FRIEND](https://i0.hdslb.com/bfs/archive/3fb28cc5eef41d048083c48e7539bdf9a7864440.jpg@560w_350h_100Q_1c.webp)

//本地图片
![原神](./QQ截图20220110160242.png)
```

![【静止画MAD】FRIEND](https://i0.hdslb.com/bfs/archive/3fb28cc5eef41d048083c48e7539bdf9a7864440.jpg@560w_350h_100Q_1c.webp)

# 代码块

```markdown
`printf()`
printf()
#include<stdio.h>
int main(){
printf("hello world!");
return 0;
}
```

# UML 图表

````markdown
//下面是一个序列图

```mermaid
sequenceDiagram
张三 ->> 李四: 你好！李四, 最近怎么样?
李四-->>王五: 你最近怎么样，王五？
李四--x 张三: 我很好，谢谢!
李四-x 王五: 我很好，谢谢!
Note right of 王五: 李四想了很长时间, 文字太长了<br/>不适合放在一行.

李四-->>张三: 打量着王五...
张三->>王五: 很好... 王五, 你怎么样?
```
sequenceDiagram
张三 ->> 李四: 你好！李四, 最近怎么样?
李四-->>王五: 你最近怎么样，王五？
李四--x 张三: 我很好，谢谢!
李四-x 王五: 我很好，谢谢!
Note right of 王五: 李四想了很长时间, 文字太长了<br/>不适合放在一行.

李四-->>张三: 打量着王五...
张三->>王五: 很好... 王五, 你怎么样?
//下面是一个流程图

```mermaid
graph LR
A[长方形] -- 链接 --> B((圆))
A --> C(圆角长方形)
B --> D{菱形}
C --> D
```
graph LR
A[长方形] -- 链接 --> B((圆))
A --> C(圆角长方形)
B --> D{菱形}
C --> D
````

- 关于 **Mermaid** 语法，参考 [这儿](https://mermaidjs.github.io/),

# Flowchart 流程图

```markdown
//标准流程图源码格式
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st->op->cond
cond(yes)->io->e
cond(no)->sub1(right)->op
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st->op->cond
cond(yes)->io->e
cond(no)->sub1(right)->op
//标准流程图源码格式（横向）
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st(right)->op(right)->cond
cond(yes)->io(bottom)->e
cond(no)->sub1(right)->op
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st(right)->op(right)->cond
cond(yes)->io(bottom)->e
cond(no)->sub1(right)->op
```
