FROM emanaev/alpine-base

# Install nginx
RUN  apk add --update nginx && \
    rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx

EXPOSE 80 443

# Install MongoDB
RUN apk --update add mongodb mongodb-tools &&\
    rm -rf /var/cache/apk/*

VOLUME /data/db
EXPOSE 27017

# Add the files
ADD root /
