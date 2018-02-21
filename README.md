# kakuyomu rss

~~~
docker-compose up -d --build
~~~
# access
feed  
`http://<your host>:8888?novelid=<kakuyomu novel id>`

# customize

docker-compose.yml

~~~
main:
  restart: always
  build: .
  environment:
    - MYDOMAIN=www.frandle.work:8888
    - KAKUYOMUDOMAIN=https://kakuyomu.jp
    - NOVELURL=https://kakuyomu.jp/works/  # novels url base
  ports:
    - 8888:5000                                               # listening port
~~~
