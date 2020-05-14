from django.test import TestCase
import pdb
import os
import json


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
        file.close()
        response = self.client.post('/', {"user_code": user_code, "user_input": "yyy"})
        self.assertEqual(response.content, b"{\"status\": \"success\", \"output\": \"Hello yyy\\n\"}")

    def test_run_code2(self):
        """
        测试复杂的cpp代码
        代码中包含dfs递归算法，输入中包含换行
        """
        file = open(os.path.dirname(__file__) + '/main2', "r")
        user_code = file.read()
        file.close()

        file = open(os.path.dirname(__file__) + '/input', "r")
        user_input = file.read()
        file.close()

        response = self.client.post('/', {"user_code": user_code, "user_input": user_input})
        self.assertEqual(json.loads(response.content)['output'], "23\n")

    def test_code_error(self):
        """
        测试用户提交的代码有错的情况
        """
        file = open(os.path.dirname(__file__) + '/main3', "r")
        user_code = file.read()
        file.close()
        # TODO
        response = self.client.post('/', {"user_code": user_code, "user_input": "sudny"})
        self.assertEqual(json.loads(response.content)['status'], "error")
