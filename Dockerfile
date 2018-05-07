FROM ubuntu:xenial

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y python-pip \
    apt-get install build-essential checkinstall -y \
    apt-get install libreadline-gplv2-dev libncursesw5-dev -y \
    aot-get install libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y

EXPOSE 5000

RUN pip install requests
RUN pip install python-oauth2
RUN pip install flask

COPY twttr1.py .
COPY classinput.py .
EXPOSE 5000

COPY app.py .

ENTRYPOINT ["python -m flask run --host=0.0.0.0" ]
