# GUAT campus network auto login

## Introduce 介绍
这个script是为航院校园网认证系统设计的自动化登录脚本  
只需要配置好`config`文件和自启动服务，就可以在开机时自动登录校园网
**不需要打开浏览器**，只需要有python环境执行脚本就能连接校园网  

如果有其他需求，欢迎提交pr和issues :)

## Usage 使用

### 1. 配置python环境
运行环境：只需要安装python解释器，版本`3.x`及以上即可  
可以去这里下载安装包：[python.org](https://www.python.org/)  
**安装时记得添加环境变量**

### 2. 下载
使用`git`执行：`git clone https://github.com/SzLeaves/guat_netlogin.git`克隆仓库到本地  
或者点这里下载压缩包：[main.zip](https://github.com/SzLeaves/guat_netlogin/archive/refs/heads/main.zip)  
然后将脚本存放或解压到一个指定位置后即可  
如果考虑方便命令执行，可以将`netlogin.py`所在的根目录路径加入环境变量中  

### 3. 运行
进入`netlogin.py`所在的根目录  
**首次运行脚本**需要配置登录用户文件，运行：`./netlogin.py gen`  
并按提示输入校园网登入验证地址（只需要域名或ip），学号，密码和网络运营商即可  
脚本会自动在当前目录下创建一个新的登录配置文件`config.json`  
```
➜  ./netlogin.py gen
Generate new file.
enter network login address: xxx.xxx.xxx
enter your campus id: 123456
enter your password: 
enter your isp name (campus/telecom/unicom/mobile): campus
Configure file generated successful.
Use: ./netlogin.py up to login network.
Use: ./netlogin.py down to logout network.
```

其中**网络运营商**目前校内有四家：配置时需要输入指定的运营商名称：
|名称     |含义        |
|---------|------------|
|campus   |默认校内网络|
|telecom  |中国电信    |
|unicom   |中国联通    |
|mobile   |中国移动    |

配置完成后，即可执行：`./netlogin.py up` 登录校园网  
如果需要注销，执行：`./netlogin.py down` 即可注销当前登录用户  

