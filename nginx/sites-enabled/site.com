server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://restfull_frontend_1:3000;
    }
    location /api {
        proxy_set_header Host $http_host;
        proxy_pass http://restfull_backend_1:8500;
    }

}
