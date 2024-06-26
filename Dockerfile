# 基础镜像，Python 环境
FROM python:3.9

# 设置 /app 作为工作目录
WORKDIR /app

# 将当前目录内容复制到工作目录内
COPY . /app

# 安装 requirements.txt 中的 Python 依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt


## 设置环境变量，例如 FLASK_ENV=development, FLASK_APP=app.py 等
## 根据你的需求设置正确的环境变量
ENV FLASK_ENV=production \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

# 使得端口号可供外界访问
EXPOSE 5000

# 定义容器启动时执行的命令，这里使用flask run启动应用
CMD ["flask", "run"]
# 启动 Flask 应用
#CMD ["python3", "app.py"]
