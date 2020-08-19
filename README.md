# restfull_test
rename .env_example to .env

docker build -t restfull:latest .

docker-compose up -d

docker exec -it restfull_web_1 ./manage.py migrate

docker exec -it restfull_web_1 ./manage.py createsuperuser

docker exec -it restfull_web_1 ./manage.py loaddata fixture.json
