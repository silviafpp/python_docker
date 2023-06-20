FROM python:3

ADD ./src/index.html index.html
ADD server.py server.py
EXPOSE 8000

ENTRYPOINT [ "python3", "server.py" ]