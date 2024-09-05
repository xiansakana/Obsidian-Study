# Java

---

title: Java
tags:

- Java
- 后端
- OOP
  categories: 后端
  cover: 'https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202403050512455.jpg'
  abbrlink: df2849ec

---

# 基础知识

## 泛型 (Generics)

泛型是Java中的一个特性，它允许在编译时提供类型安全的检查，并消除类型强制转换。简单来说，泛型就是在定义类、接口或方法时使用类型参数（type parameters），这些类型参数在对象被创建或方法被调用时指定具体的类型。使用泛型可以使代码更加灵活，同时保持了类型的安全性。

### 泛型的好处：

1. **类型安全**：泛型提供编译时的类型检查，只允许存储指定类型的对象，减少运行时错误。
2. **消除类型强制转换**：使用泛型之前，集合中的对象是Object类型的，取出时需要强制类型转换。使用泛型后，对象的类型就是指定的类型，无需转换。
3. **提高代码的可读性和可维护性**：泛型代码明确了各种类型之间的关系，增加了代码的清晰度。

### 泛型的基本使用：

- **泛型类**：在类名后添加`<T>`，其中`T`是类型参数，表示该类是泛型类。例如，`ArrayList<E>`是一个可以存储任何类型对象的动态数组，`E`是在实例化ArrayList时指定的具体类型。

```java
public class Box<T> {
    private T t; // T stands for "Type"

    public void set(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }
}
```

- **泛型接口**：和泛型类类似，接口也可以是泛型的。例如，`Comparable<T>`接口允许当前对象与同一类型的另一个对象进行比较。

```java
public interface Comparable<T> {
    int compareTo(T o);
}
```

- **泛型方法**：在方法返回类型之前指定一个类型参数。这意味着每次调用方法时都可以指定一个具体的类型。

```java
public class Util {
    public static <T> void swap(T[] a, int i, int j) {
        T temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
```

### 泛型的类型参数命名约定：

- `E` - Element (在集合中使用，比如`ArrayList<E>`)
- `K` - Key (键，在Map中使用)
- `V` - Value (值，在Map中使用)
- `T` - Type (通用的类型)
- `S`, `U`, `V`等 - 第二个、第三个、第四个类型

### 泛型的限制：

- 不能实例化类型参数：`new T()`是不允许的，因为在编译时T的具体类型是未知的。
- 不能创建类型参数的数组：`new T[]`是不允许的，但可以创建`T[]`类型的引用。
- 不能使用某些静态方法：静态域或方法不能引用类的类型参数。
- 不能使用基本数据类型作为类型参数：只能使用类类型，如果需要使用基本数据类型，可以使用它们的包装类（如`Integer`、`Double`等）。

泛型在Java中是一个非常强大的特性，它为编程提供了更多的灵活性和类型安全。

## 多态 (Polymorphism)

Java 中的多态是面向对象编程中的一个核心概念，指的是一个方法调用可以有多种形式。它允许一个对象取多种形式，能够让 Java 程序具有更好的可扩展性和维护性。多态性可以分为编译时多态和运行时多态，主要通过继承和接口实现。

### 编译时多态（静态多态）

编译时多态是通过方法重载实现的。方法重载意味着在同一个类中可以有多个同名方法，只要它们的参数列表不同（参数的数量或类型不同）即可。编译器根据方法的不同参数列表在编译时决定使用哪个方法，因此称为编译时多态。

### 运行时多态（动态多态）

运行时多态是通过方法覆盖（方法重写）实现的，是多态的最常见形式。它允许子类有自己的实现，覆盖父类的方法。当通过父类引用调用该方法时，JVM 会根据对象的实际类型调用对应子类的覆盖方法，这种决定在运行时做出，因此称为运行时多态。

### 实现运行时多态的条件

1. **继承**：必须存在继承关系，子类继承父类。
2. **方法覆盖**：子类必须覆盖父类的方法。
3. **向上转型**：通过父类引用来调用子类对象。

### 示例

假设有一个父类`Animal`和两个子类`Dog`和`Cat`，每个类都有一个`makeSound`方法。

```java
class Animal {
    void makeSound() {
        System.out.println("Some sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Meow");
    }
}

public class TestPolymorphism {
    public static void main(String[] args) {
        Animal myAnimal = new Dog();
        myAnimal.makeSound();  // Outputs: Bark

        myAnimal = new Cat();
        myAnimal.makeSound();  // Outputs: Meow
    }
}

```

在这个例子中，通过父类引用`myAnimal`调用`makeSound`方法时，实际执行的是对象的实际类型（`Dog`或`Cat`）的`makeSound`方法。这就是运行时多态的体现。

# 面试

‍
