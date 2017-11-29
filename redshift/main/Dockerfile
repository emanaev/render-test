FROM nvidia/cuda

ARG DISTRIB_IP=none
ENV DISTRIB_IP ${DISTRIB_IP}
RUN echo $DISTRIB_IP

RUN apt-get update && \
  apt-get install -y wget libfreetype6 && \
  wget -q ${DISTRIB_IP}:8080/redshift_v2.5.32_linux_demo.run && \
  chmod +x redshift_v2.5.32_linux_demo.run && \
  echo accept | ./redshift_v2.5.32_linux_demo.run && \
  rm redshift_v2.5.32_linux_demo.run

WORKDIR /usr/redshift/bin
