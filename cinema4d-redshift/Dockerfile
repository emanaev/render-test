FROM nvidia/cuda:10.2-runtime-centos7

#FROM nvidia/cudagl:10.1-runtime-centos7

ENV CINEMA4D_DISTR=https://installer.maxon.net/Cinema4D-21.026_centos7_clr-RB290015.x86_64.rpm
RUN curl -L https://installer.maxon.net/Cinema4D-21.026_centos7_clr-RB290015.x86_64.rpm -o cinema4d.rpm
RUN yum install -y webkitgtk4-2.22.7-2.el7.x86_64 cinema4d.rpm

#ARG DISTRIB=http://172.25.4.169:8080
#ENV REDSHIFT_URL=$DISTRIB/redshift_v2.6.48_linux_demo.run
#RUN echo ===== Downloading RedShift from  ${REDSHIFT_URL} && \
#    curl ${REDSHIFT_URL} -o redshift.run && \
#    chmod +x redshift.run && \
#    echo accept | ./redshift.run && \
#    rm redshift.run
#RUN cp -r /usr/redshift/redshift4c4d/R20/Redshift $(ls -d /opt/maxon/*)
COPY c4d /
ENTRYPOINT ["/c4d"]
