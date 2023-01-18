# Deploy FastAPI to AWS EC2

### Steps to deploy on EC2
1. sudo apt-get update
2. sudo apt install -y python3-pip nginx
3. sudo vim /etc/nginx/sites-enabled/fastapi_nginx
4. server {
    listen 80;
    server_name <public IPv4>;
    location / {
      proxy_pass http://127.0.0.1:8000;
     }
   }
5. esc button
6. :wq 
7. sudo service nginx restart
8. git clone https://github.com/dhanashreeronghe24/test-fastapi.git
9. cd test-fastapi
10. ls 
11. cat requirements.txt 
12. pip3 install -r requirements.txt 
13. python3 -m uvicorn main:testApp
14. http://<public IPv4>

