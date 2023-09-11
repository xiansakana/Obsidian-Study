## 创建Github新仓库
 
![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309092235458.png)

一定要勾选public，不然别人看不到图，然后建议加一个README文件。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100117996.png)

看到如下界面就说明图床已经创建好了，接下来就是上传图片了。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100119836.png)

## 上传图片

#### 下载PicGo

推荐使用一个开源图床工具 [PicGo](https://molunerfinn.com/PicGo/) 来作为我们的图片上传工具，打开链接的官网后点击免费下载后会跳转到Github的界面。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309111107422.png)

一般前几个是beta版本，也就是测试版本，所以我们选择后面的正式版。

![[Pasted image 20230911111011.png]]

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309111111418.png)

在所需下载版本的最后的assets中选择对应的系统版本，windows系统32位就选ia32，64位就选x64，或者直接直接选下面那个setup exe的，ios系统选dmg。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309111113731.png)

安装之后软件的界面大概是这样。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100122429.png)


#### 创建Github token

在Github里打开Settings

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100125562.png)

然后翻到最下面左侧选择Developer settings

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100127190.png)

进入Developer settings后选择左边Personal access tokens里的的tokens (classic)，最后点击Generate new token (classic)。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100153740.png)

填写用途，我选择的是永不过期，并勾选repo，然后点Generate token即可

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100133829.png)

这个token只会显示一次，所以最好把它复制下来存好，方便下次使用，否则下次有需要重新新建。我的话直接在Github上新建一个private库来存这个token，这样想用也能随时找到。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100154448.png)

#### 配置PicGo

打开PicGo，选择图床设置中的GitHub然后设置如下，其中仓库名是刚刚创建的仓库，分支名一般是main，Token就是刚刚生成的那个，最后点击确定。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100139688.png)

我一般直接选择qq或者snipaste截图然后直接剪切板图片快捷上传，或者直接拖动图片上传。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100122429.png)

也可以通过快捷键上传，默认为ctrl + shift +P。

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100146871.png)

如果在国内的话Github图片访问可能会很慢，所以这时候我们就可以用 [jsDelivr](https://www.jsdelivr.com/") 进行免费加速，而设置的方法也很简单，只需要在我们 PicGo 图床配置中添加如下自定义域名即可

>https://cdn.jsdelivr.net/gh/用户名/仓库名

![](https://raw.githubusercontent.com/xiansakana/IMG-BED/main/202309100200201.png)
