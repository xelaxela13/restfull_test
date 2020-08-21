# restfull_test
rename .env_example to .env

docker-compose up -d --build

docker exec -it restfull_backend_1 ./manage.py migrate

docker exec -it restfull_backend_1 ./manage.py createsuperuser

docker exec -it restfull_backend_1 ./manage.py loaddata fixture.json

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "xelaxela13@gmail.com", "password": "054489473"}' \
  http://localhost:8500/api/token/
  
curl \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk3OTkyODExLCJqdGkiOiIwNzY2NTgyZWY2Y2Q0NDk1OWFjMGFhMGQ3MzNjMDVhYyIsInVzZXJfaWQiOjN9.SSbKHfV-MuvelBwdCUu_5KDiLxX-onGTdLOPKzVwb_M" \
  http://localhost:8500/products/
