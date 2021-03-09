FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install dicttoxml cryptography
CMD ["encrypt.py", "sample.json", "-genrate", "-encrypt"]
ENTRYPOINT ["python"]
