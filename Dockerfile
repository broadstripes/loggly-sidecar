FROM debian:stretch-slim
MAINTAINER Javier Maldonado  <3goliad@gmail.com>

RUN apt-get update && apt-get install --yes \
    syslog-ng \
    curl

RUN mkdir -pv /opt/syslog-ng/keys/ca.d \
    && cd /opt/syslog-ng/keys/ca.d/ \
    && curl -O https://logdog.loggly.com/media/logs-01.loggly.com_sha12.crt

COPY syslog-ng.conf.tmpl /etc/syslog-ng/

VOLUME /dev/log

COPY run.py /root/

CMD ["/usr/bin/python2.7", "/root/run.py"]
