from django.shortcuts import render, HttpResponse
from django.views import View
from django import forms
import os
import _judger
import pdb
import json


class SubmitCode(forms.Form):
    """
    提交代码的表单
    """
    user_code = forms.CharField(label="代码", max_length=1024, widget=forms.Textarea, required=True)
    user_input = forms.CharField(label="输入数据", max_length=1024, required=True)


# Create your views here.
class ProcessCodeView(View):
    """
    返回运行代码结果的视图类
    """
    # 用户代码和测试用例提交路径
    code_path = os.path.dirname(__file__) + "/user_codes"

    def get(self, request):
        """
        渲染出请求用户代码的表单页面
        """
        form = SubmitCode()
        return render(request, template_name="index.html", context={'form': form})

    def post(self, request):
        """
        返回用户代码的运行结果
        """
        # 清除本地文件
        self.clear_usercode()
        form_data = SubmitCode(request.POST)
        if form_data.is_valid():
            # 将用户提交的代码写入main.c文件中
            # 将用户提交的输入数据保存到1.in中
            try:
                code_file = open(self.code_path + "/main.cpp", "w+")
                code_file.write(form_data.cleaned_data['user_code'])
                code_file.close()

                input_file = open(self.code_path + "/1.in", "w+")
                input_file.write(form_data.cleaned_data['user_input'])
                input_file.close()
            except KeyError:
                return HttpResponse("请提供代码和输入数据")

            # 运行代码
            error_mess = self.run_usercode()

            # 返回内容
            content = {}

            # 读取运行结果1.out文件
            # 如果文件不存在，说明运行出错，返回错误信息
            try:
                file1 = open(self.code_path + "/1.out", "r")
                content['status'] = "success"
                content['output'] = file1.read()
                file1.close()
                return HttpResponse(json.dumps(content))
            except FileNotFoundError:
                content['status'] = "error"
                content['output'] = ""
                return HttpResponse(json.dumps(content))
        return HttpResponse("请提交有效数据")

    def clear_usercode(self):
        """
        清除user_codes文件夹下所有文件
        """
        os.system("rm " + self.code_path + "/*")

    def run_usercode(self):
        """
        运行用户代码
        """
        if os.system("g++ " + self.code_path + "/main.cpp" + " -o" + self.code_path + "/main"):
            return "编译或者运行错误，请检查你的代码"
        ret = _judger.run(max_cpu_time=1000,
                          max_real_time=2000,
                          max_memory=128 * 1024 * 1024,
                          max_process_number=200,
                          max_output_size=10000,
                          max_stack=32 * 1024 * 1024,
                          # five args above can be _judger.UNLIMITED
                          exe_path=self.code_path + "/main",
                          input_path=self.code_path + "/1.in",
                          output_path=self.code_path + "/1.out",
                          error_path=self.code_path + "/1.out",
                          args=[],
                          # can be empty list
                          env=[],
                          log_path="judger.log",
                          # can be None
                          seccomp_rule_name="c_cpp",
                          uid=0,
                          gid=0)
        return ret
