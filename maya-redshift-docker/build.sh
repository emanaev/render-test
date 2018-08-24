#!/bin/bash
ADDR=$(ip addr | grep 'state UP' -A2 | head -n3 | tail -n1 | awk '{print $2}' | cut -f1 -d'/')
DISTRIB=$(readlink -f $PWD/../../distrib)
echo Starting distrib at http://${ADDR}:8080
echo Make sure distributions of Maya and Redshift are in $DISTRIB
docker run --name some-nginx --rm -v $DISTRIB:/usr/share/nginx/html:ro -d -p 8080:80 nginx
docker build -t emanaev/maya-redshift --build-arg DISTRIB_IP=$ADDR .
docker stop some-nginx
