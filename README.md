# kakuyomu rss

~~~
docker-compose up -d --build
~~~
# access
feed  
`http://<your host>:8888`

# customize

docker-compose.yml

~~~
main:
  restart: always
  build: .
  environment:
    - MYDOMAIN=www.frandle.work:8888
    - KAKUYOMUDOMAIN=https://kakuyomu.jp
    - NOVELURL=https://kakuyomu.jp/works/1177354054882154317  # novels url
  ports:
    - 8888:5000                                               # listening port
~~~
