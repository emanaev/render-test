FROM emanaev/redshift3d

RUN apt-get update && \
  apt-get install -y libglib2.0-0 libgl1-mesa-glx

WORKDIR /root

ENV DEADLINECLIENT DeadlineClient-10.0.7.4-linux-x64-installer.run

RUN wget http://${DISTRIB_IP}:8080/${DEADLINECLIENT} && \
  chmod +x ${DEADLINECLIENT} && \
  ./DeadlineClient-10.0.7.4-linux-x64-installer.run --mode unattended --connectiontype Remote  \
    --noguimode true --licensemode LicenseFree --proxyrootdir nashtorg.ru:8081

CMD ["/opt/Thinkbox/Deadline10/bin/deadlineslave", "-nogui"]
