# RunCppOline

#### 介绍
一个在线运行C++代码的web程序[预览](http://120.92.173.80:8080/)

#### 软件架构
- Python3.5
- Django2.2
- [Judger](http://github.com/QingdaoU/Judger) 运行环境沙盒


#### 快速部署教程
1.使用本仓库的 `Dockerfile` 构建一个新镜像

2.运行 `docker run -it -p 本地端口:8080 镜像名称` 或者 `docker run -it -P 镜像名称`

3.访问 `0.0.0.0:8080`或者`0.0.0.0:-P指定的端口`

4.返回如下界面表示成功
![11](judgerserver/startics/shili1.png)

5.运行单元测试 `python3 manage.py test` 返回类似如下，表示功能正常
```shell script
Ran 6 tests in 1.132s

OK
Destroying test database for alias 'default'...
```

#### 开发环境搭建

1.安装`docker`

2.拉取镜像。该镜像为该项目的开发环境。`sudo docker pull registry.cn-shanghai.aliyuncs.com/sundy-allstar/run_cpp_app:env`

3.运行镜像并且将代码文件挂载入容器中。 挂载文件 注意使用绝对路径
```shell script
docker run -it -p 8080:8080 \
  -v /Users/mac/Desktop/new_run_cpp/RunCppOline/judgerserver:/home/judgerserver \
  registry.cn-shanghai.aliyuncs.com/sundy-allstar/run_cpp_app:env
```
在容器中运行代码，在本地中修改代码即可。

#### Ubuntu下部署教程

1.安装依赖
```
sudo apt-get install libseccomp-dev
mkdir build && cd build && cmake .. && make && sudo make install
```

2.运行
```
sudo python manage.py runserver 0:8080
```

#### 使用说明

 **1.请求和返回** 

通过post请求向服务器发送代码和输入数据，post请求格式如下：
```
{
    "user_code": "your_code",
    "user_input": "your_input_data"
}
```

返回两个字段，`status`表示代码运行的结果，`error`表示代码运行错误，`success`表示代码运行成功；`output`表示代码运行输出结果。
```
{
    "status": "",
    "output": "",
}
```

 **2.举例** 

在本地有个文本文件`main`内容如下：
```cpp
#include<cstdio>
#include<iostream>
using namespace std;
int main(){
    string input;
    cin>>input;
    cout<<"Hello "<<input<<endl;
}
```

发送post请求:

```py
file = open(os.path.dirname(__file__) + '/main', "r")
user_code = file.read()
file.close()
client.post('/', {"user_code": user_code, "user_input": "World"})
```

返回：
```
{
    "status": "success",
    "output": "Hello World",
}

```


如有问题请发`Issues`谢谢。
