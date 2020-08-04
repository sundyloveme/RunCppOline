from django.test import TestCase
import pdb
import os
import json


def to_str_to_json(response):
    json_response_content = str(response.content, "utf-8")
    json_response_content = json.loads(json_response_content)
    return json_response_content


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
        file = open(os.path.dirname(__file__) + '/main', "r")
        user_code = file.read()
        file.close()
        response = self.client.post('/', {"user_code": user_code,
                                          "user_input": "yyy"})
        json_response_content = str(response.content, "utf-8")
        json_response_content = json.loads(json_response_content)
        self.assertEqual(json_response_content['status'], 'success')
        self.assertEqual(json_response_content['output'], 'Hello yyy\n')

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

        response = self.client.post('/', {"user_code": user_code,
                                          "user_input": user_input})
        # self.assertEqual(json.loads(response.content)['output'], "23\n")
        content = to_str_to_json(response)
        self.assertEqual(content['output'], "23\n")

    def test_code_error(self):
        """
        测试用户提交的代码有错的情况
        """
        file = open(os.path.dirname(__file__) + '/main3', "r")
        user_code = file.read()
        file.close()

        response = self.client.post('/', {"user_code": user_code,
                                          "user_input": "sudny"})
        content = to_str_to_json(response)
        self.assertEqual(content['status'], "error")

    def test_code_empty(self):
        """
        测试用户提供的数据为空 或者不存在 user_code和user_input字段
        """
        file = open(os.path.dirname(__file__) + '/main', "r")
        user_code = file.read()
        file.close()

        response = self.client.post('/', {"user_code": "",
                                          "user_input": ""})
        content = response.content.decode("utf-8")
        self.assertEqual(content, "请提交有效数据")

    def test_code_contain_zh(self):
        """
        测试用户代码中包含中文
        """
        file = open(os.path.dirname(__file__) + '/main4', "r", encoding="utf-8")
        user_code = file.read()
        file.close()
        response = self.client.post('/', {"user_code": user_code,
                                          "user_input": "yyy"})
        json_response_content = str(response.content, "utf-8")
        json_response_content = json.loads(json_response_content)
        self.assertEqual(json_response_content['status'], 'success')
        self.assertEqual(json_response_content['output'], 'Hello yyy\n')
