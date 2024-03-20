---
title: SpringBoot常用注解
tags:
  - SpringBoot
  - 后端
categories: 后端
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202312180825037.jpg
abbrlink: e750a506
date: 2023-12-18 08:13:42
---

# @SpringBootApplication

`@SpringbootApplication`标注一个主程序类，相当于`@Configuration`, `@EnableAutoConfiguration`和`@ComponentScan`并具有他们的默认属性值。

```java
package com.xiansakana.springbootannotation;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringbootAnnotationApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringbootAnnotationApplication.class, args);
    }

}
```

# @Controller

`@Controller`是`@Component`注解的一个延伸，会自动扫描并配置被该注解标注的类，返回页面。此注解用于标注 Spring MVC 的控制器。

# @RequestMapping

`@RequestMapping`是用于映射 url 到控制器类的一个特定处理程序方法。可用于方法或者类上面，也就是可以通过 url 找到该方法或该类。

```java
package com.xiansakana.springbootannotation.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;


@Controller
public class ViewController {
    // 不带数据直接返回页面，用String返回
    @RequestMapping("/view")
        public String view(){
            return "test";
    }

    // 带数据返回页面，用ModelAndView对象返回
    @RequestMapping("/data")
    public ModelAndView data(){
        ModelAndView m = new ModelAndView("test");
        m.addObject("str1", "Hello");
        m.addObject("str2", "World");
        return m;
    }
}
```

```html
<!--resources/static/test.html-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>test</title>
  </head>
  <body>
    <div>Test</div>
    <hr />
    <div>${str1}</div>
    <hr />
    <div>${str2}</div>
  </body>
</html>
```

如果要将`return "test.html"`修改成`return "test"`则需要在`application.properties`中加上如下内容

```properties
spring.mvc.view.prefix=/
spring.mvc.view.suffix=.html
```

除此之外，如果要解析视图，需要在`pom.xml`中引入 freemarker dependency

```xml
<!--freemarker模版引擎-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-freemarker</artifactId>
</dependency>
```

然后在`application.properties`里配置

```properties
#freemarker
spring.freemarker.suffix=.html
spring.freemarker.template-loader-path=classpath:/static/
```

# @RequestParam

`@RequestParam`注解用于将方法的参数与 Web 请求的传递的参数进行绑定。使用`@RequestParam`可以轻松的访问 HTTP 请求参数的值。

```java
package com.xiansakana.springbootannotation.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ParamController {
    @RequestMapping("/param")

    public ModelAndView param(@RequestParam(value = "id", defaultValue = "0") int id, @RequestParam(value = "name", required = false, defaultValue = "") String name){
        System.out.println("id=" + id);
        System.out.println("name=" + name);
        ModelAndView m = new ModelAndView("test2");
        m.addObject("id", id);
        m.addObject("name", name);
        return m;
    }
}
```

```html
<!--resources/static/test2.html-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Param</title>
  </head>
  <body>
    <div>id: ${id}</div>
    <div>name: ${name}</div>
  </body>
</html>
```

# @PathVariable

`@PathVariable`注解是将方法中的参数绑定到请求 URI 中的模板变量上。

```java
package com.xiansakana.springbootannotation.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ParamController {
    @RequestMapping("/path/{id}/{name}")

    public ModelAndView path(@PathVariable(required = false) int id, @PathVariable(required = false) String name){
        System.out.println("id=" + id);
        System.out.println("name=" + name);
        ModelAndView m = new ModelAndView("test2");
        m.addObject("id", id);
        m.addObject("name", name);
        return m;
    }
}
```

```html
<!--resources/static/test2.html-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Param</title>
  </head>
  <body>
    <div>id: ${id}</div>
    <div>name: ${name}</div>
  </body>
</html>
```

# @RestController (@Controller + @ResponseBody)

`@RestController`是在 Spring 4.0 开始引入的，这是一个特定的控制器注解。此注解相当于`@Controller`和`@ResponseBody`的快捷方式。返回的是输出结果，如 json，一般用来与`@RequestMapping`, `@GetMapping`, `@PostMapping`结合。

# @GetMapping

`@GetMapping`注解用于查询所有用户方法，用于处理 HTTP GET 请求，并将请求映射到具体的处理方法中。具体来说，`@GetMapping`是一个组合注解，它相当于是`@RequestMapping(method=RequestMethod.GET)`的快捷方式。

```java
package com.xiansakana.springbootannotation.controller;

import com.xiansakana.springbootannotation.entity.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {

    @GetMapping("/get") // http://localhost:8080/user/get
    public User get(){
        User user = new User(1, "saltedfish", "男", 23);
        System.out.println("user: " + user);
        return user;
    }

    @GetMapping("/{id}") // http://localhost:8080/user/{id}
    public User getById(@PathVariable("id") int id){
        User user = new User(2, "xiansakana", "女", 18);
        System.out.println("user: " + user);
        return user;
    }
}
```

# @PostMapping

`@PostMapping`注解用于处理 HTTP POST 请求，并将请求映射到具体的处理方法中。`@PostMapping`与`@GetMapping`一样，也是一个组合注解，它相当于是`@RequestMapping(method=HttpMethod.POST)`的快捷方式。

# @RequestBody

`@RequestBody`在处理请求方法的参数列表中使用，它可以将请求主体中的参数绑定到一个对象中，请求主体参数是通过`HttpMessageConverter`传递的，根据请求主体中的参数名与对象的属性名进行匹配并绑定值。此外，还可以通过`@Valid`注解对请求主体中的参数进行校验。

```java
@PostMapping // http://localhost:8080/user
public User addUser(@RequestBody User user){
    System.out.println(user);
    return user;
}
```

# @CrossOrigin

`@CrossOrigin`注解将为请求处理类或请求处理方法提供跨域调用支持。如果我们将此注解标注类，那么类中的所有方法都将获得支持跨域的能力。使用此注解的好处是可以微调跨域行为。

| 注解                    | 备注                 |
| ----------------------- | -------------------- |
| @Service                | bean 注册            |
| @Component              | bean 注册            |
| @Autowired              | 获取 bean            |
| @Resource               | 获取 bean            |
| @Autowired + @Qualifier | 获取 bean            |
| @Configuration + @Bean  | bean 注册（人为）    |
| @Value                  | 从配置文件中获取参数 |

# @Service

`@Service`注解是`@Component`的一个延伸（特例），它用于标注业务逻辑类。与`@Component`注解一样，被此注解标注的类，会自动被 Spring 所管理。

# @Component

`@component`定义 spring 管理 bean，声明一个 IOC 容器，把所有标记了`@Bean`注解的类注入到 IOC 容器中去。

# @Autowired

`@Autowired`注解用于标记 Spring 将要解析和注入的依赖项。此注解可以作用在构造函数、字段和 setter 方法上，会找到接口的实现类并自动装配。

```java
// UserService
package com.xiansakana.springbootannotation.service;

import com.xiansakana.springbootannotation.entity.User;

public interface UserService {
    public User get();
    public User getById(int id);
    public User addUser(User user);
}
```

```java
// UserServiceImpl
package com.xiansakana.springbootannotation.service.impl;

import com.xiansakana.springbootannotation.entity.User;
import com.xiansakana.springbootannotation.service.UserService;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

@Service
public class UserServiceImpl implements UserService {

    public User get(){
        User user = new User(1, "saltedfish", "男", 23);
        System.out.println("user: " + user);
        return user;
    }

    public User getById(@PathVariable("id") int id) {
        User user = new User(2, "xiansakana", "女", 18);
        System.out.println("user: " + user);
        return user;
    }

    public User addUser(@RequestBody User user){
        System.out.println(user);
        return user;
    }
}
```

```java
// UserActionController
package com.xiansakana.springbootannotation.controller;

import com.xiansakana.springbootannotation.entity.User;
import com.xiansakana.springbootannotation.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/action")
public class UserActionController {
    @Autowired
    private UserService userService;

    @GetMapping("/get") // http://localhost:8080/action/get
    public User get(){
      return userService.get();
    }

    @GetMapping("/{id}") // http://localhost:8080/action/{id}
    public User getById(@PathVariable("id") int id){
       return userService.getById(id);
    }

    @PostMapping // http://localhost:8080/action
    public User addUser(@RequestBody User user){
        return userService.addUser(user);
    }
}
```

# @Primary

如果同类型的bean存在多个，可以用`@Primary`指定优先级

```java
@Primary
@Service
public class UserServiceImpl implements UserService{}
```

# @Resource (@Autowired + @Qualifier)

如果两个实现类共用一个接口可以用`@Resource`代替`@Autowired`并指定`name`。`@Resource`是JDK提供的注解，`@Autowired`是Spring框架提供；`@Resource`默认按照名称注入，而`@Autowired`默认按照类型注入。

```java
@RestController
public class UserController{
	@Resource(name = "userServiceImpl")
	private UserService userService;
	
	@Resource(name = "adminServiceImpl")
	private UserService adminService;
}
```

# @Qualifier

```java
@RestController
public class UserController{
	@Autowired
	@Qualifier("userServiceImpl")
	private UserService userService;
}
```

# @Configuration

配置类，对应配置文件，本质上是一个`@Component`，只是更有意义，见名知意。

# @Bean

`@Bean`注解主要的作用是告知 Spring，被此注解所标注的类将需要纳入到 Bean 管理工厂中。注解后，spring 容器就会调用接口对应的方法，并将方法的返回结果存入容器。

```java
// MyBeans
package com.xiansakana.springbootannotation.configuration;

import com.xiansakana.springbootannotation.service.UserService;
import com.xiansakana.springbootannotation.service.impl.AdminServiceImpl;
import com.xiansakana.springbootannotation.service.impl.UserServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MyBeans {
    @Bean
    public UserService AdminServiceImpl(){
        return new AdminServiceImpl();
    }

    @Bean
    public UserService UserServiceImpl(){
        return new UserServiceImpl();
    }
}
```

# @Value

```java
@Value("${local.username}")
private String username;

@Value("${local.password}")
private String password;

@GetMapping("value") // http://localhost:8080/action/value
public String getValue(){
    System.out.println("username: " + username);
    System.out.println("password: " + password);
    return "value{username: " + username + ", password: " + password + "}";
}
```

```properties
local.username=saltedfish
local.password=123456
```

# @ConfigurationProperties

@Value注解只能一个个注入外部属性，但是@ConfigurationProperties可以批量的将外部属性注入到bean对象属性中。

```java
// AliOSSProperties.java
@Data
@Component
@ConfigurationProperties(perfix = "aliyun.oss")
public class AliOSSProperties{
	private String endpoint;
	private String accessKeyId;
	private String accessKeySecret;
	private String bucketName;
}
```

```yml
aliyun:
  oss:
    endpoint:
    accessKeyId:
    accessKeySecret:
    bucketName:
```
