# Springboot

---

title: Springboot
tags:

- 后端
- Java
- SpringBoot
  categories: 后端
  cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401262242149.jpg
  abbrlink: cf14bd9c
  date: 2024-01-26 22:39:38

---

# 开发环境热部署

在实际的项目开发调试过程中会频繁地修改后台类文件，导致需要重新编译、重新启动，整个过程非常麻烦，影响开发效率。在实际的项目开发调试过程中会频繁地修改后台类文件，导致需要重新编译、重新启动，整个过程非常麻烦，影响开发效率。

`Spring Boot`提供了`spring-boot-devtools`组件，使得无须手动重启`SpringBoot`应用即可重新编译、启动项目，大大缩短编译启动的时间。Spring 启动提供了 Spring-boot-`devtools`组件，使得无须手动重启`SpringBoot`应用即可重新编译、启动项目，大大缩短编译启动的时间。

`devtools`会监听`classpath`下的文件变动，触发 Restart 类加载器重新加载该类从而实现类文件和属性文件的热部署。`devTools`会监听类路径下的文件变动，触发重启类加载器重新加载该类从而实现类文件和属性文件的热部署。

并不是所有的更改都需要重启应用(如静态资源、视图模板)，可以通过设置`spring.devtools.restart.exclude`属性来指定一些文件或目录的修改不用重启应用并不是所有的更改都需要重启应用(如静态资源、视图模板)，可以通过设置`spring.devtools.restart`排除属性来指定一些文件或目录的修改不用重启应用。

1. 在`pom.xml`配置文件中添加`dev-tools`依赖
2. 使用 optional=true 表示依赖不会传递，即该项目依赖`devtools`；其他项目如果引入此项目生成的 JAR 包，则不会包含`devtools`

   ```xml
   <dependency>
   	<groupId>org.springframework.boot</groupId>
   	<artifactId>spring-boot-devtools</artifactId>
   	<optional>true</optional>
   </dependency>
   ```
3. 在`application.properties`中配置`devtools`

```properties
   #热部署生效
   spring.devtools.restart.enabled=true
   #设置重启目录
   spring.devtools.restart.additional-paths=src/main/java
   #设置cLasspath月灵下的WEB-INF文件夹内容修改不重启
   spring.devtools.restart.exclude=static/**
```

如果使用了`Eclipse`，那么在修改完代码并保存之后，项目将自动编译并触发重启，而如果使用了`IntelliJIDEA`，还需要配置项目自动编译。

1. 打开 Settings 页面，在左边的菜单栏找到`Build, Execution, Deployment 一 Compiler`，勾选`Build project automatically`
2. 在 Settings 页面左边的菜单栏找到 Advanced Settings，勾选 A`llow auto-make to start even if developed application is currently running`

# Springboot Controller

## @RestController

默认情况下，`@RestController`注解会将返回的对象数据转换为 JOSN 格式

```java
@RestController
public class TestController {
    @RequestMapping("/user")
    public User getUser(){
        User user = new User();
        user.setUsername("zhangsan");
        user.setPassword("123");
        return user;
    }
}
```

## RequestMapping

- `@RequestMapping`注解主要负责 URL 的路由映射。它可以添加在 Controller 类或者具体的方法上。
- 如果添加在 Controller 类上，则这个 Controller 中的所有路由映射都将会加上此映射规则，如果添加在方法上，则只对当前方法生效。
- `@RequestMapping`注解包含很多属性参数来定义 HTTP 的请求映射规则。常用的属性参数如下:

  - value: 请求 URL 的路径，支持 URL 模板、正则表达式
  - method: HTTP 请求方法
  - consumes: 请求的媒体类型 (Content-Type) ，如 application/json
  - produces: 响应的媒体类型
  - params，headers: 请求的参数及请求头的值

  ```java
  @RestController
  public class HelloController {
  // http://localhost:8080/hello
      @RequestMapping(value = "/hello", method = RequestMethod.GET)
      public String hello(){
          return "hello";
      }
  }
  ```

## 参数传递

- `@RequestParam`将请求参数绑定到控制器的方法参数上，接收的参数来自 HTTP 请求体或请求 url 的 QueryString，当请求的参数名称与 Controller 的业务方法参数名称一致时`@RequestParam`可以省略。
- `@PathVaraible`: 用来处理动态的 URL，URL 的值可以作为控制器中处理方法的参数。
- `@RequestBody`接收的参数是来自 requestBody 中，即请求体。一般用于处理非 Content-Type: application/x-www-form-urlencoded 编码格式的数据，比如: application/json, application/xml 等类型的数据。

```java
@RestController
public class ParamsController {
    @RequestMapping(value = "/getTest1", method = RequestMethod.GET)
    public String getTest1(){
        return "GET请求";
    }

    @RequestMapping(value = "/getTest2", method = RequestMethod.GET)
    // http://localhost:8080/getTest2?nickname=xxx&phone=xxx
    public String getTest2(String nickname, String phone){
        System.out.println("nickname: " + nickname);
        System.out.println("phone: " + phone);
        return "GET请求";
    }

    @RequestMapping(value = "/getTest3", method = RequestMethod.GET)
    // http://localhost:8080/getTest2?nickname=xxx
    public String getTest3(@RequestParam(value = "nickname", required = false) String name){
        System.out.println("nickname: " + name);

        return "GET请求";
    }

    @RequestMapping(value = "/postTest1", method = RequestMethod.POST)
    public String postTest1(){
        return "POST请求";
    }

    @RequestMapping(value = "/postTest2", method = RequestMethod.POST)
    public String postTest2(String username, String password){
        System.out.println("username: " + username);
        System.out.println("password: " + password);
        return "POST请求";
    }

    @RequestMapping(value = "/postTest3", method = RequestMethod.POST)
    public String postTest3(User user){
        System.out.println(user);
        return "POST请求";
    }

    @RequestMapping(value = "/postTest4", method = RequestMethod.POST)
    public String postTest4(@RequestBody User user){
        System.out.println(user);
        return "POST请求";
    }

    @GetMapping(value = "/test1/**")
    public String test1(){
        return "多层通配符请求";
    }

    @GetMapping(value = "/test2/*")
    public String test2(){
        return "一层通配符请求";
    }
}
```

# 文件上传和拦截器

## 静态资源访问

- 使用 IDEA 创建 Spring Boot 项目会默认创建出`classpath:/static/`目录，静态资源一般放在这个目录下即可。
- 如果默认的静态资源过滤策略不能满足开发需求，也可以自定义静态资源过滤策略。
- 在`application.properties`中直接定义过滤规则和静态资源位置:

  ```properties
  spring.mvc.static-path-pattern=/static/**
  spring.web.resources,static-locations=classpath:/static/
  ```
- 过滤规则为`/static/**`，静态资源位置为`classpath:/static/`

## 文件上传原理

- 表单的`enctype`属性规定在发送到服务器之前应该如何对表单数据进行编码。
- 当表单的`enctype="application/x-www-form-urlencoded”`（默认） 时，form 表单中的数据格式为: `key=value&key=value`
- 当表单的`enctype="multipart/form-data"`时，其传输数据形式如下

  ![](https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202401191420448.png)
- SpringBoot 工程嵌入的 tomcat 限制了请求的文件大小，每个文件的配置最大为 1Mb，单次请求的文件的总数不能大于 10Mb。
- 要更改这个默认值需要在配置文件(如`application.properties`)中加入两个配置。

  ```properties
  spring.servlet.multipart.max-file-size=10MB
  spring.servlet.multipart.max-request-size=10MB
  ```
- 当表单的`enctype="multipart/form-data"`时,可以使用`MultipartFile`获取上传的文件数据，再通过`transferTo`方法将其写入到磁盘中。

  ```java
  @RestController
  public class FileUploadController {
      @PostMapping("/upload")
      @RequestMapping(value = "upload", method = RequestMethod.POST)
      public String up(String nickname, MultipartFile photo, HttpServletRequest request) throws IOException {
          System.out.println(nickname);
          // 获取图片的原始名称
          System.out.println(photo.getOriginalFilename());
          // 获取文件类型
          System.out.println(photo.getContentType());

          String path = request.getServletContext().getRealPath("/upload/");
          System.out.println(path);
          saveFile(photo, path);
          return "上传成功";
      }

      public void saveFile(MultipartFile photo, String path) throws IOException {
          File dir = new File(path);
          if(!dir.exists()){
              dir.mkdir();
          }

          File file = new File(path+photo.getOriginalFilename());
          photo.transferTo(file);
      }
  }
  ```
- 如想要用户能够访问上传的图片，应该在配置文件加入如下配置

  ```properties
  spring.web.resources.static-locations=/upload/
  ```

## 拦截器

拦截器在 Web 系统中非常常见，对于某些全局统一的操作，我们可以把它提取到拦截器中实现。总结起来，拦截器大致有以下几种使用场景:

- 权限检查：如登录检测，进入处理程序检测是否登录，如果没有，则直接返回登录页面。
- 性能监控：有时系统在某段时间莫名其妙很慢，可以通过拦截器在进入处理程序之前记录开始时间，在处理完后记录结束时间，从而得到该请求的处理时间。
- 通用行为：读取 cookie 得到用户信息并将用户对象放入请求，从而方便后续流程使用，还有提取 Locale、Theme 信息等，只要是多个处理程序都需要的，即可使用拦截器实现。

### 拦截器定义

- Spring Boot 定义了`Handlerlnterceptor`接口来实现自定义拦截器的功能。
- `Handlerlnterceptor`接口定义了`preHandle`, `postHandle`, `afterCompletion`三种方法，通过重写这三种方法实现请求前、请求后等操作。

```java
public class LoginInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler){
        System.out.println("LoginInterceptor");
        return true;
    }
}
```

### 拦截器注册

- `addPathPatterns`方法定义拦截的地址。
- `excludePathPatterns`定义排除某些地址不被拦截。
- 添加的一个拦截器没有`addPathPattern`任何一个`url`则默认拦截所有请求。
- 如果没有`excludePathPatterns`任何一个请求，则默认不放过任何一个请求。

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry){
        registry.addInterceptor(new LoginInterceptor()).addPathPatterns("/user/**");
    }
}
```

# RESTful

## 介绍

- RESTful 是目前流行的互联网软件服务架构设计风格。
- REST (Representational State Transfer，表述性状态转移)一词是由 RoyThomas Fielding 在 2000 年的博士论文中提出的，它定义了互联网软件服务的架构原则，如果一个架构符合 REST 原则，则称之为 RESTful 架构。
- REST 并不是一个标准，它更像一组客户端和服务端交互时的架构理念和设计原则，基于这种架构理念和设计原则的 Web API 更加简洁，更有层次。

## 特点

- 每一个 URI 代表一种资源
- 客户端使用 GET、POST、PUT、DELETE 四种表示操作方式的动词对服务端资源进行操作:GET 用于获取资源，POST 用于新建资源（也可以用于更新资源），PUT 用于更新资源，DELETE 用于删除资源。
- 通过操作资源的表现形式来实现服务端请求操作。
- 资源的表现形式是 JSON 或者 HTML。
- 客户端与服务端之间的交互在请求之间是无状态的，从客户端到服务端的每个请求都包含必需的信息。

## RESTful API

- 符合 RESTful 规范的 Web API 需要具备如下两个关键特性:
- 安全性:安全的方法被期望不会产生任何副作用，当我们使用 GET 操作获取资源时，不会引起资源本身的改变，也不会引起服务器状态的改变。
- 幂等性:幂等的方法保证了重复进行一个请求和一次请求的效果相同（并不是指响应总是相同的，而是指服务器上资源的状态从第一次请求后就不再改变了)，在数学上幂等性是指 N 次变换和一次变换相同。

## HTTP Method

- HTTP 提供了 POST、GET、PUT、DELETE 等操作类型对某个 Web 资源进行 Create、Read、Update 和 Delete 操作。
- 一个 HTTP 请求除了利用 URI 标志目标资源之外，还需要通过 HTTP Method 指定针对该资源的操作类型，一些常见的 HTTP 方法及其在 RESTful 风格下的使用:

|HTTP 方法|操作|返回值|特定返回值|
| ---------| ------| ------------------------------------------------------| -----------------------------------------------------------------------|
|POST|Create|201 (Created), 提交或保存资源|404 (Not Found), 409 (Conflict) 资源已存在|
|GET|Read|200 (OK), 获取资源或数据列表，支持分页、排序和条件查询|200 (OK) 返回资源, 404 (Not Found) 资源不存在|
|PUT|Update|200 (OK) or 204 (Not Content), 修改资源|404 (Not Found) 资源不存在, 405 (Method Not Allowed) 禁止使用该方法调用|
|PATCH|Update|200 (OK) or 204 (Not Content), 部分修改|404 (Not Found) 资源不存在|
|DELETE|Delete|200 (OK), 资源删除成功|404 (Not Found) 资源不存在, 405 (Method Not Allowed) 禁止使用该方法调用|

## HTTP 状态码

- HTTP 状态码就是服务向用户返回的状态码和提示信息，客户端的每一次请求，服务都必须给出回应，回应包括 HTTP 状态码和数据两部分。
- HTTP 定义了 40 个标准状态码，可用于传达客户端请求的结果。状态码分为以下
  5 个类别:
  - 1xx:信息，通信传输协议级信息
  - 2xx:成功，表示客户端的请求已成功接受
  - 3xx:重定向，表示客户端必须执行一些其他操作才能完成其请求
  - 4xx:客户端错误，此类错误状态码指向客户端
  - 5xx:服务器错误，服务器负责这写错误状态码

## Spring Boot 实现 RESTful API

- Spring Boot 提供的 spring-boot-starter-web 组件完全支持开发 RESTful APl,提供了与 REST 操作方式(GET、POST、PUT、DELETE）对应的注解。
- @GetMapping: 处理 GET 请求，获取资源。
- @PostMapping: 处理 POST 请求，新增资源。
- @PutMapping: 处理 PUT 请求，更新资源。
- @DeleteMapping: 处理 DELETE 请求，删除资源。
- @PatchMapping: 处理 PATCH 请求，用于部分更新资源。

```java
@RestController
public class UsersController {

    @GetMapping("/user/{id}")
    public String getUserById(@PathVariable int id){
        System.out.println(id);
        return "根据ID获取用户";
    }

    @PostMapping("/user")
    public String save(User user){
        return "添加用户";
    }

    @PutMapping("/user")
    public String update(User user){
        return "根据ID获取用户";
    }

    @DeleteMapping("/user/{id}")
    public String deleteById(@PathVariable int id){
        return "根据ID删除用户";
    }
}
```

# Swagger

- Swagger 是一个规范和完整的框架，用于生成、描述、调用和可视化`RESTful`风格的 Web 服务，是非常流行的 API 表达工具。
- Swagger 能够自动生成完善的`RESTfulAPI`文档同时并根据后台代码的修改同步更新，同时提供完整的测试页面来调试 API。

## 使用 Swagger 生成 Web API 文档

- 在 Spring Boot 项目中集成 Swagger 同样非常简单，只需在项目中引入`springfox-swagger2`和`springfox-swagger-ui`依赖即可。由于使用的 SpringBoot 是 3.2.0 版本，导致无法使用 swagger2 依赖无法使用。

  ```xml
  <dependency>
      <groupId>io.swagger.core.v3</groupId>
      <artifactId>swagger-annotations</artifactId>
       <version>2.2.15</version>
  </dependency>
  <dependency>
      <groupId>org.springdoc</groupId>
      <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
      <version>2.1.0</version>
  </dependency>
  ```
- 在`http://127.0.0.1:8080/swagger-ui/index.html`打开即可

# Mybatis Plus

- pom 配置

```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.5</version>
</dependency>

<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>

<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.21</version>
</dependency>
```

- application.properties 配置

```properties
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/mydb?useSSL=false
spring.datasource.username=root
spring.datasource.password=root
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

- 新建`com.xiansakana.mybatisplus.mapper`包用来储存数据库操作
- 在启动器`MyBatisPlusApplication`添加`@MapperScan("com.xiansakana.mybatisplus.mapper")`
