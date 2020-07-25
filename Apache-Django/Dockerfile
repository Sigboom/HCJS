FROM django:BASE
MAINTAINER "daniel <sigbooom@163.com>"
COPY conf/mod_wsgi.so /usr/local/apache2/modules/
COPY conf/httpd.conf /usr/local/apache2/conf/
COPY conf/autosort.conf /usr/local/apache2/conf/extra/
COPY mysql-change/*.py /usr/local/lib/python3.7/dist-packages/django/db/backends/mysql/
