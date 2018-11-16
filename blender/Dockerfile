FROM nvidia/cuda:8.0-runtime

RUN apt-get update && \
    apt-get install -y \
        curl \
        bzip2 \
        libfreetype6 \
        libgl1-mesa-dev \
        libglu1-mesa \
        libxi6 \
        libxrender1 && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

ENV BLENDER_MAJOR 2.79
ENV BLENDER_VERSION 2.79
ENV BLENDER_BZ2_URL https://mirror.clarkson.edu/blender/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-linux-glibc219-x86_64.tar.bz2

RUN mkdir /usr/local/blender && \
    curl -SL "$BLENDER_BZ2_URL" | \
    tar -jx -C /usr/local/blender --strip-components=1 && \
    ln -s /usr/local/blender/blender /usr/bin/blender

COPY render.sh /
COPY *.py /
ENV THREADS 0
CMD ["/render.sh"]
