docker-compose down
docker-compose up --build -d

ssh -i ~/.ssh/id_rsa root@localhost -p 4343
cat var/lib/tor/hidden_service/hostname