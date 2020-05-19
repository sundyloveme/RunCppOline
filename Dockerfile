FROM registry.cn-shanghai.aliyuncs.com/sundy-allstar/run_cpp_app:1.0
COPY . /home
WORKDIR /home/judgerserver/
EXPOSE 8080
CMD ["gunicorn", "judgerserver.wsgi", "-b", "0.0.0.0:8080"]