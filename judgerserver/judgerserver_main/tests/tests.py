from django.test import TestCase
import pdb
import os


# Create your tests here.
# 测试C语言代码
# 测试C++语言代码
# 测试输入数据中有换行
# 测试输入的代码有错误 能不能返回错误 编译或者运行错误，请检查你的代码

class ViewTest(TestCase):
    def test_home(self):
        """
        检测访问首页是否成功
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200, "访问首页出错")

    def test_run_code(self):
        """
        测试cpp代码能否通过运行
        """
        # pdb.set_trace()
        file = open(os.path.dirname(__file__) + '/main', "r")
        user_code = file.read()
        response = self.client.post('/', {"user_code": user_code, "user_input": "yyy"})
        self.assertEqual(response.content, b"Hello yyy\n")
