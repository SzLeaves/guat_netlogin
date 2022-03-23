# GUAT campus network auto login
桂航校园网认证服务登录脚本，使用python构建

## Introduce 介绍
本项目用于航院校园网认证系统的登录认证  
只需要配置好`config`文件后运行脚本，就可以登录校园网服务，**不需要打开浏览器操作**  

如果有其他需求，欢迎提交pr和issues :)


## Requirements 依赖要求 
只需要安装python解释器，版本`3.x`及以上即可  
可以去这里下载安装包：[python.org/downloads](https://www.python.org/downloads/)  
**安装时记得添加环境变量**

## Usage 使用
### 1. 下载
使用`git`执行：`git clone https://github.com/SzLeaves/guat_netlogin.git`克隆仓库到本地  
或者点这里下载压缩包：[main.zip](https://github.com/SzLeaves/guat_netlogin/archive/refs/heads/main.zip)  
然后将脚本存放或解压到一个指定位置后即可  
如果考虑方便命令执行，可以将`netlogin.py`所在的根目录路径加入环境变量中  

### 2. 生成配置文件
进入启动脚本`netlogin.py`所在的根目录  

**首次运行启动脚本**需要配置登录用户文件：
* Linux / MacOS 在终端运行：`./netlogin.py gen`  
* Windows 在命令行运行：`python netlogin.py gen`

并按提示输入校园网登入验证地址（只需要域名或ip），学号，密码和网络运营商即可  
脚本会自动在当前目录下创建一个新的**默认**登录配置文件`config.json`  
```bash
➜  ./netlogin.py gen
Generate new file.
enter network login address: xxx.xxx.xxx                     # 认证入口IP：10.1.2.3
enter your campus id: 123456                                 # 学号 
enter your password:                                         # 上网密码
enter your isp name (campus/telecom/unicom/mobile): campus   # 网络运营商

Configure file generated successful.
Use: netlogin.py up to login network.
Use: netlogin.py down to logout network.
or, Use: '--config=' option to specify a configure file.
```

其中**网络运营商**目前校内有四家：配置时需要输入指定的运营商名称：
|名称     |含义        |
|---------|------------|
|campus   |默认校内网络|
|telecom  |中国电信    |
|unicom   |中国联通    |
|mobile   |中国移动    |

如果有需要生成多个用户的配置文件，可以使用`gen [FILE_NAME]`参数指定配置文件名称：
```bash
➜  ./netlogin.py gen example        # 生成一个名称为example的配置文件
Generate new file example.json
enter network login address: xxx.xxx.xxx
enter your campus id: 987654
enter your password: 
enter your isp name (campus/telecom/unicom/mobile): campus

Configure file generated successful.
Use: ./netlogin.py up to login network.
Use: ./netlogin.py down to logout network.
or, Use: '--config=' option to specify a configure file.
```

成功生成的配置文件默认会放置在**启动脚本所在的根目录下**  

> 如果在登录的时候没有指定配置文件，启动脚本将默认选择`config.json`

### 3. 登录
配置完成后，即可登录校园认证网络：  
* Linux / MacOS 在终端运行：`./netlogin.py up`  
* Windows 在命令行运行：`python netlogin.py up`

程序将自动读取默认的配置文件内容进行登录认证操作  

如果你需要指定其他的配置文件，可以添加`--config=`参数：  
```bash
netlogin.py up --config=[your_config_file]
```

如果你需要临时指定登录的网络运营商，可以使用`--isp=`参数：
```bash
netlogin.py up --isp=[your_bind_isp]
```
> **上述两个选项可以同时指定**

### 4. 注销
如果需要注销：  
* Linux / MacOS 在终端运行：`./netlogin.py down`  
* Windows 在命令行运行：`python netlogin.py down`  

即可注销当前登录用户  

如果你需要指定其他的配置文件，可以添加`--config=`参数：  
```bash
netlogin.py down --config=[your_config_file]
```

## Auto Login 自动登录
如果有启动系统时就自动联网的需求，可以为`netlogin.py`配置自启动服务
