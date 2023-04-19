
run:
	docker-compose up

stop:
	docker-compose stop

build:
	docker build -t converty_img .

entry:
	docker exec -it converty_bot bash
