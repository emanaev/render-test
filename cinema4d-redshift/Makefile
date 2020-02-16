IMAGE=cinema4d-redshift

build:
	docker run -d --rm --name=distrib -p 8080:80 -v /Users/emanaev/Downloads/:/usr/share/nginx/html:ro nginx
	docker build -t $(IMAGE) .
	docker stop distrib

run:
	docker run -it $(IMAGE) -render /render/balltest.c4d -oimage /render/balltest -oformat JPG

