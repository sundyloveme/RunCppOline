# JudgeServer

#### 介绍
一个在线运行C++代码的web程序。

#### 软件架构
- Python3.7
- Django2.0
- [Judger](http://github.com/QingdaoU/Judger)

#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

通过post请求向服务器发送代码和输入数据，post请求格式如下：
```
{
    "csrfmiddlewaretoken":"PkGuYgbcPoin2cm4KejexiSV9FNBQfAKYJdzzCEkijfmBbnrRzOGycvYXm63YId2",
    "user_code": "your_code",
    "user_input": "your_input_data"
}
```
举例，在本地个文本文件`main`内容如下：
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

发送post请求举例:
```py
file = open(os.path.dirname(__file__) + '/main', "r")
user_code = file.read()
file.close()
response = client.post('/', {"user_code": user_code, "user_input": "World"})
```

返回两个字段，一个`status`表示代码运行的结果，'error'表示代码运行错误；一个‘output’表示代码运行输出结果。
```
{
    "status": "",
    "output": "",
}
```

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

如有问题请发`Issues`谢谢。