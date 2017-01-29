FROM centos:7

RUN yum install -y epel-release
RUN yum install -y supervisor
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install flask feedgenerator lxml

COPY bin /opt/kakuyomu_rss_gen/bin
COPY supervisord.conf /etc/supervisord.conf

CMD python /usr/bin/supervisord -c /etc/supervisord.conf
