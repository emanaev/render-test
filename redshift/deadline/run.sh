docker run --runtime=nvidia --rm -it -v /mount:/data/files \
  -v /etc/timezone:/etc/timezone:ro -v /etc/localtime:/etc/localtime:ro \
  --add-host files:10.147.147.1 \
  emanaev/redshift3d:deadline
