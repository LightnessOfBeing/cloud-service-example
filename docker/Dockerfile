FROM python:3

WORKDIR /my_app

COPY . .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD [python3 hello.py]