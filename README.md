# restfull_test
rename .env_example to .env

docker-compose up -d --build

docker exec -it restfull_backend_1 ./manage.py migrate

docker exec -it restfull_backend_1 ./manage.py createsuperuser

docker exec -it restfull_backend_1 ./manage.py loaddata fixture.json

localhost:9999/
