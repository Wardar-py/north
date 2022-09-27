The citybike Wien Importer

Команда для запуска: `docker-compose -f docker-compose.yml up -d`

После запуска зайти в контейнер командой: `docker exec -it {name of container} bash`

Применить миграции бд внутри контейнера: `aerich upgrade`

Swagger API:  `http://localhost:6001/docs`
