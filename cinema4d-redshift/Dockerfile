FROM nvidia/cuda:10.2-runtime-centos7

RUN curl -L https://installer.maxon.net/installer/21.115_RB297076/Cinema4D-21.115_centos7_clr-RB297076.x86_64.rpm -o cinema4d.rpm && \
    yum install -y webkitgtk4-2.22.7-2.el7.x86_64 cinema4d.rpm && \
    rm cinema4d.rpm && \
    yum clean all && \
    rm -rf /var/cache/yum

RUN curl http://192.168.1.3:8080/redshift_v2.6.51_linux.run -o redshift.run && \
    chmod +x redshift.run && \
    echo accept | ./redshift.run && \
    rm redshift.run
RUN cp -r /usr/redshift/redshift4c4d/R21/Redshift $(ls -d /opt/maxon/*/bin/plugins)
COPY c4d /
COPY login /
RUN mkdir /render
COPY balltest.c4d /render
ENTRYPOINT ["/c4d"]
