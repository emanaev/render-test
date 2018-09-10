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

###
### INSTALL MAYA ###
###

#ENV MAYA_URL=https://edutrial.autodesk.com/NET18SWDLD/2018/MAYA/ESD/Autodesk_Maya_2018_EN_Linux_64bit.tgz
#ENV MAYA_URL=https://up.autodesk.com/2018/MAYA/4A3226EE-E90A-4E0A-9BE7-58D657D6F872/Autodesk_Maya_2018_3_Update_Linux_64bit.tgz
ENV MAYA_URL=http://${DISTRIB_IP}:8080/Autodesk_Maya_2018_3_Update_Linux_64bit.tgz

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

###
### INSTALL REDSHIFT FOR MAYA ###
###
ENV REDSHIFT_URL http://${DISTRIB_IP}:8080/redshift_v2.6.19_linux_demo.run

RUN echo ===== Downloading RedShift from  ${REDSHIFT_URL} && \
  wget -q ${REDSHIFT_URL} -O redshift.run && \
  chmod +x redshift.run && \
  echo accept | ./redshift.run && \
  rm redshift.run

RUN mkdir -p /root/maya/modules && \
    cp /usr/redshift/redshift4maya/redshift4maya.mod.template ~/maya/modules/redshift4maya.mod && \
    cp /usr/redshift/redshift4maya/common/rendererDesc/redshiftRenderer.xml /usr/autodesk/maya2018/bin/rendererDesc/

COPY entrypoint.sh /
CMD ["/entrypoint.sh"]

#RUN yum update -y && \
#    yum install -y unzip gcc openssl-devel bzip2-devel && \
#    yum clean all

#RUN cd /usr/src && curl -sL https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz | tar xz && \
#    cd Python-2.7.15 && ./configure --enable-optimizations && ./configure --enable-optimizations && make altinstall

#RUN curl -sL "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python2.7 get-pip.py && \
#    pip install pyte

#RUN curl https://bootstrap.pypa.io/2.6/get-pip.py -o get-pip.py && \
#    python get-pip.py && \
#    pip install --upgrade pip && \
    
#RUN mkdir setuptools && cd setuptools && \
#    curl -sLk https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz | tar zx --strip-components=1 && \
#    python setup.py install && \
#    cd .. && rm -rf setuptools


#RUN mkdir setuppyte && cd setuppyte && \
#    curl -sL https://github.com/selectel/pyte/tarball/0.4.0 | tar zx --strip-components=1 && \
#    python setup.py install && \
#    cd .. && \
#    rm -rf setuppyte

#COPY nanoterm.py /

#ENV VRAY_URL http://${DISTRIB_IP}:8080/vray_trial_36004_maya2018_linux_x64.tar.gz

#RUN echo ===== Downloading V-Ray from  ${VRAY_URL} && \
#    wget -q ${VRAY_URL} -O vray.tar.gz && \
#    tar xf vray.tar.gz

#RUN ./installer.bin -bin=vray_trial_36004_maya2018_linux_x64.ibin -auto
#    rm vray*


###
### INSTALL PHOENIXFD FOR MAYA ###
###
#ENV PHOENIX_URL http://${DISTRIB_IP}:8080/phoenixFD_trial_31100_maya2018_vray3_linux_x64.zip

#RUN echo ===== Downloading PhoenixFD from  ${PHOENIX_URL} && \
#    wget -q ${PHOENIX_URL} -O phoenixFD.zip && \
#    unzip phoenixFD.zip && \
#    chmod +x phoenixFD_trial_31100_maya2018_vray3_linux_x64 && \
#    ./phoenixFD_trial_31100_maya2018_vray3_linux_x64 -gui=0 -auto && \
#    rm phoenixFD*
