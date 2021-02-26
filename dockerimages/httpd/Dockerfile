FROM centos:latest
RUN yum install httpd net-tools -y
COPY index.html /var/www/html
CMD /usr/sbin/httpd -DFOREGROUND