# 快速开始
## 安装
### Windows
首先在[Github Release](https://github.com/moyanj/hispid/releases "Github Release")下载Windows一键包，它的名字应该是 hispid-x.x.x-windows.exe
然后双击运行它，根据软件提示操作
### Linux

#### CentOS一键脚本
```bash
yum install -y wget && wget -O install.sh https://github.com/moyanj/hispid/ && sh ./install.sh
```
#### Ubuntu/Deepin一键脚本
```bash
wget -O install.sh https://github.com/moyanj/hispid/ && ./install.sh
```
### 从源码安装
#### 克隆源码
首先从Github上克隆源码至本地仓库
```bash
git clone https://github.com/moyanj/hispid.git
```
克隆完毕后，你的目录结构应为
```bash
├── LICENSE
├── Pipfile
├── config.json
├── core.py
├── data.py
├── docs
│   ├── CNAME
│   ├── README.md
│   ├── _navbar.md
│   └── index.html
├── hispid.py
├── moyansdk
│   └── hispid.py
├── plugin_manager.py
├── plugins
│   └── test
│       └── app.py
├── readme.md
├── requirements.txt
├── res
│   ├── copyright
│   ├── help
│   │   ├── de-DE.txt
│   │   ├── en-US.txt
│   │   ├── fr-FR.txt
│   │   └── zh-CN.txt
│   ├── png
│   │   ├── 128x128.png
│   │   ├── 16x16.png
│   │   ├── 32x32.png
│   │   ├── 512x512.png
│   │   ├── 64x64.png
│   │   └── 8x8.png
│   └── web
│       └── index.html
├── run.bat
├── run.sh
├── script
└── test.his
```
#### 安装Python
##### Windows
自行Google
##### Linux
```bash
yum install python3.11.3
```
或者
```bash
sudo apt-get install python=3.10.3
```
##### 安装所需要的python包
###### 虚拟环境
执行下列命令
```bash
pip install pipenv
```
```bash
pipenv install
```
###### 真实环境
```bash
pip -r install requirements.txt
```
