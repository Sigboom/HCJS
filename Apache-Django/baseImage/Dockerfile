FROM httpd:latest
RUN apt-get -y upgrade && apt-get update
RUN apt-get install -y wget gcc make build-essential libncursesw5-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev libreadline-dev libapache2-mod-wsgi-py3
RUN wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
RUN tar xvf Python-3.6.8.tar.xz
RUN cd Python-3.6.8 && ./configure && make && make install
RUN rm -rf /usr/local/apache2/Python-3.6.8*
RUN ln -s /usr/local/bin/python3 /usr/local/bin/python
RUN ln -s /usr/local/bin/pip3 /usr/local/bin/pip
RUN pip install --upgrade pip
RUN pip install django pymysql django-redis cryptography
COPY mod_wsgi.so /usr/local/apache2/modules/
