DISTRIB_IP=172.16.1.18
docker build --build-arg DISTRIB_IP=$DISTRIB_IP -t emanaev/redshift3d main
docker build -t emanaev/redshift3d:benchmark benchmark
