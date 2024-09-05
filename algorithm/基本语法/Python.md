# Python

# Int

### 取整

* 向上取整

```python
>>> math.ceil(8.1)
9
>>> math.ceil(-8.9)
-8
```

* 向下取整

```python
>>> math.floor(8.9)
8
>>> math.floor(-8.1)
-9
```

* 四舍五入

```python
>>> round(8.1)
8
>>> round(-8.9)
-9
```

* 去尾

```python
>>> int(8.9)
8
>>> int(-8.1)
-8

#如果指定了base参数，那么第一个参数必须是字符类型
#面的例子就是指定字符为2进制数据，将其转换为十进制
>>> int('11', base=2)
3

#如果不指定，则认为字符是十进制数据
>>> int('101')
101
```

* 分别取整数和小数

```python
>>> math.modf(3.25)
(0.25, 3.0)
>>> math.modf(3.75)
(-0.75, -3.0)
```

# String

## isalnum()

String中至少有一个字符且如果String中的所有字符都是字母数字，那么返回结果就是True；否则，就返回False。

## strip()

删除头尾指定字符

```python
my_string = "   Hello, world!   "
stripped_string = my_string.strip() 
print(stripped_string)
# Hello, world!

string = " the King has the largest army in the entire world the"
print(string.strip(" eht"))
# King has the largest army in the entire world
```

‍

## replace()

```python
string = "geeks for geeks geeks geeks geeks"
print(string.replace("e", "a"))
# gaaks for gaaks gaaks gaaks gaaks

print(string.replace("ek", "a", 3))
# geas for geas geas geeks geeks
```

## split()

```python
text = 'geeks for geeks'
print(text.split())
# ['geeks', 'for', 'geeks']
 
word = 'geeks, for, geeks'
print(word.split(','))
# ['geeks', ' for', ' geeks']
 
word = 'geeks:for:geeks'
print(word.split(':'))
# ['geeks', 'for', 'geeks']
 
word = 'CatBatSatFatOr'
print(word.split('t'))
# ['Ca', 'Ba', 'Sa', 'Fa', 'Or']

word = 'geeks, for, geeks, pawan'
print(word.split(', ', 0))
# ['geeks, for, geeks, pawan']

print(word.split(', ', 4))
# ['geeks', 'for', 'geeks', 'pawan']

print(word.split(', ', 1))
# ['geeks', 'for, geeks, pawan']
```

# Array

## sort(), sorted()

* sorted()不会改变原来列表的顺序

```python
L = [1, 5, 4, 2, 3]
print(sorted(L))
# [1, 2, 3, 4, 5]
print(L)
# [1, 5, 4, 2, 3]
```

* sort()会改变原来列表的顺序

```python
L = [1, 5, 4, 2, 3]
print(L.sort())
# [1, 2, 3, 4, 5]
print(L)
# [1, 2, 3, 4, 5]
```

* 二维数组

```python
students = [[3,'Jack',12],[2,'Rose',13],[1,'Tom',10],[5,'Sam',12],[4,'Joy',8]]
# 按学号顺序排序：
print(sorted(students,key=(lambda x:x[0])))
# [[1, 'Tom', 10], [2, 'Rose', 13], [3, 'Jack', 12], [4, 'Joy', 8], [5, 'Sam', 12]]

# 按年龄为主要关键字，名字为次要关键字倒序排序：
print(sorted(students,key=(lambda x:[x[2],x[1]]),reverse=True))
# [[2, 'Rose', 13], [5, 'Sam', 12], [3, 'Jack', 12], [1, 'Tom', 10], [4, 'Joy', 8]]
```

# Dictionary

## Counter()

```python
from collections import Counter
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
x = Counter(a)
print(x)
# Counter({12: 2, 3: 2, 4: 1, 5: 1, 11: 1, 6: 1, 7: 1})
x_keys = list(x.keys())
x_values = list(x.values())
print(x_keys)
# [12, 3, 4, 5, 11, 6, 7]
print(x_values)
# [2, 2, 1, 1, 1, 1, 1]
```

## defaultdict()

defaultdict(list),会构建一个默认value为list的字典

```python
from collections import defaultdict
result = defaultdict(list)
data = [("p", 1), ("p", 2), ("p", 3), ("h", 1), ("h", 2), ("h", 3)]
for (key, value) in data:
    result[key].append(value)
print(result)
#defaultdict(<class 'list'>, {'p': [1, 2, 3], 'h': [1, 2, 3]})
```

## get()

```python
word_map = {}
words = ["bar","foo","the"]
# 如果 word 存在于word_map中，它将返回 word 当前的计数；如果 word 不在word_map中，它将返回默认值 0
for word in words:
	word_map.get(word, 0) + 1
```

## clear()

```python
# 删除字典内所有元素
word_map.clear()
```

# Set

## add()

```python
rows = [set() for _ in range(9)]
for i in range(9):
	rows[i].add(num)
```

# 其他

## zip()

```python
names = ("John", "Jane", "Jade")
ages = (2, 4, 6)
zipped = zip(names, ages)
print(tuple(zipped))
# (('John', 2), ('Jane', 4), ('Jade', 6))

print(list(zipped))
# [('John', 2), ('Jane', 4), ('Jade', 6)]

print(set(mapped))
# {('John', 2), ('Jane', 4), ('Jade', 6)}

for(x,y) in zipped:
	print(x,y)
# John 2
# Jane 4
# Jade 6

new_dict = {name: age for names, ages in zip(names, ages)}
print(new_dict)
# {'John': 2, 'Jane': 4, 'Jade': 6}

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
# 0 John 2
# 1 Jane 4
# 2 Jade 6

namez, agez = zip(*zipped)
print("The name list is: ", end="")
print(namz)
print("The age list is: ", end="")
print(agez)
# The name list is: ("John", "Jane", "Jade")
# The age list is: (2, 4, 6)
```

## divmod()

​`divmod()`​是一个内置函数，它接受两个数字作为参数，并返回一个包含商和除法运算的余数的元组。

* If x and y are integers, the return value is (x // y, x % y)

```python
print('(15, 13) = ', divmod(15, 13))
# (15, 13) =  (1, 2)
```

* If x or y is a float, the result is (q, x % y), where q is the whole part of the quotient.

```python
print('(8.0, 3) = ', divmod(8.0, 3))
# (8.0, 3) =  (2.0, 2.0)
print('(3, 8.0) = ', divmod(3, 8.0))
# (3, 8.0) =  (0.0, 3.0)
print('(7.5, 2.5) = ', divmod(7.5, 2.5))
# (7.5, 2.5) =  (3.0, 0.0)
```

‍
