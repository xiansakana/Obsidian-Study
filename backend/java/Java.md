---
abbrlink: '0'
---
# 基础知识

## 多态 (Polymorphism)

Java中的多态是面向对象编程中的一个核心概念，指的是一个方法调用可以有多种形式。它允许一个对象取多种形式，能够让Java程序具有更好的可扩展性和维护性。多态性可以分为编译时多态和运行时多态，主要通过继承和接口实现。

### 编译时多态（静态多态）

编译时多态是通过方法重载实现的。方法重载意味着在同一个类中可以有多个同名方法，只要它们的参数列表不同（参数的数量或类型不同）即可。编译器根据方法的不同参数列表在编译时决定使用哪个方法，因此称为编译时多态。

### 运行时多态（动态多态）

运行时多态是通过方法覆盖（方法重写）实现的，是多态的最常见形式。它允许子类有自己的实现，覆盖父类的方法。当通过父类引用调用该方法时，JVM会根据对象的实际类型调用对应子类的覆盖方法，这种决定在运行时做出，因此称为运行时多态。

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

