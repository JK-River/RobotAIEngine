FROM hub.c.163.com/netease_comb/centos:7
MAINTAINER xiaoyi

# 更新yum源
RUN yum makecache fast && yum -y update glibc    

# 安装常用软件
RUN yum install -y openssh-server vim tar wget curl rsync bzip2 iptables tcpdump less telnet net-tools lsof
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN yum -y install git
RUN yum -y install gcc
#RUN yum -y install gcc-c++
RUN yum -y install python-devel
RUN yum -y install make automake
RUN yum -y install redis
RUN yum clean all

RUN mkdir -p /data/www/query_analysis
RUN mkdir -p /data/logs
ADD . /data/www/query_analysis

RUN pip install --upgrade pip
RUN pip install supervisor
RUN pip install tornado
RUN pip install redis
RUN pip install PyYAML
RUN pip install regex

WORKDIR /data/www/query_analysis
ENTRYPOINT ["supervisord", "-n", "-c", "supervisord_docker.conf"]



