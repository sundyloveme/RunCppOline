FROM registry.cn-shanghai.aliyuncs.com/sundy-allstar/run_cpp_app:env
COPY . /home
WORKDIR /home/judgerserver/
EXPOSE 8080
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]