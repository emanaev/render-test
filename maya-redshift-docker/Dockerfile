FROM nvidia/cuda:7.5-runtime-centos6

RUN yum update -y && yum install -y \
    nano \
    csh \
    libXp \
    libXmu \
    libXpm \
    libXi \
    libtiff \
    libXinerama \
    elfutils \
    gcc \
    gstreamer-plugins-base.x86_64 \
    gamin \
    git \
    mesa-utils \
    mesa-libGL-devel \
    tcsh \
    xorg-x11-server-Xorg \
    xorg-x11-server-Xvfb \
    wget && \
    yum groupinstall -y "X Window System" && \
    yum clean all

ARG DISTRIB_IP=none
ENV DISTRIB_IP ${DISTRIB_IP}
#ENV DISTRIB_IP=172.16.1.18

#ENV MAYA_URL=https://edutrial.autodesk.com/NET18SWDLD/2018/MAYA/ESD/Autodesk_Maya_2018_EN_Linux_64bit.tgz
ENV MAYA_URL=http://${DISTRIB_IP}:8080/Autodesk_Maya_2018_EN_Linux_64bit.tgz

RUN echo ==== Downloading Maya from  ${MAYA_URL} && \
    wget -q ${MAYA_URL} -O maya.tgz && \
    mkdir /maya && tar -xvf maya.tgz -C /maya && \
    rm maya.tgz && \
    rpm -Uvh /maya/Maya*.rpm && \
    rm -r /maya

# Make mayapy the default Python
RUN echo alias hpython="\"/usr/autodesk/maya/bin/mayapy\"" >> ~/.bashrc && \
    echo alias hpip="\"mayapy -m pip\"" >> ~/.bashrc

# Setup environment
ENV MAYA_LOCATION=/usr/autodesk/maya/
ENV PATH=$MAYA_LOCATION/bin:$PATH

# Workaround for "Segmentation fault (core dumped)"
# See https://forums.autodesk.com/t5/maya-general/render-crash-on-linux/m-p/5608552/highlight/true
ENV MAYA_DISABLE_CIP=1

ENV REDSHIFT_URL http://${DISTRIB_IP}:8080/redshift_v2.6.19_linux_demo.run

RUN echo ===== Downloading RedShift from  ${REDSHIFT_URL} && \
  wget -q ${REDSHIFT_URL} -O redshift.run && \
  chmod +x redshift.run && \
  echo accept | ./redshift.run && \
  rm redshift.run

RUN mkdir -p /root/maya/modules && \
    cp /usr/redshift/redshift4maya/redshift4maya.mod.template ~/maya/modules/redshift4maya.mod && \
    cp /usr/redshift/redshift4maya/common/rendererDesc/redshiftRenderer.xml /usr/autodesk/maya2018/bin/rendererDesc/
