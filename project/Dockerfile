FROM python:3

ADD server.py server.py
ADD /build/html /var/www/html
WORKDIR /var/www/html

EXPOSE 8888

ENTRYPOINT ["python3", "/opt/app.py"]

