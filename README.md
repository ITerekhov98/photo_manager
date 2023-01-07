### Photo manager, based on drf and postgresql.

## Функционал
### [Ссылка на сайт](https://iterekhov.ru/api/v1/photos/)
### [Ссылка на postman-коллекцию](https://www.postman.com/navigation-astronaut-23060129/workspace/iterekhov/collection/24836864-e622ed07-0ea4-4a98-a50a-cb4b03ec9149?action=share&creator=24836864)
#### Как быстро потестить API:
- Зарегистрируйтесь в [Postman](https://identity.getpostman.com/login);
- Перейдите по ссылке на postman-коллекцию выше, создайте форк (Ctrl+Alt+F);
- Таким же образом скопируйте к себе [Тестовый environment с access token](https://www.postman.com/navigation-astronaut-23060129/workspace/iterekhov/environment/24836864-19357dff-7cec-405b-b18c-4b4523517525);
- Перейдите во вкладку коллекции и в правом верхнем углу выберите тестовый environment;
- Можете пользоваться :)


## Установка и запуск:

### Dev версия

Скачайте репозиторий с кодом, перейдите в каталог. Создайте `.env` файл и наполните его следующими настройками, в формате `Ключ=значение`:

- `DEBUG` — дебаг-режим
- `DJANGO_SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `POSTGRES_DB` - Имя базы данных
- `POSTGRES_USER` - Имя пользователя базы данных
- `POSTGRES_PASSWORD` - Пароль пользователя базы данных

Собираем и запускаем контейнер:
```
docker-compose -f docker-compose.dev.yaml up --build
```
Подождите несколько секунд чтобы запустились все сервисы и собралась статика. Сайт будет доступен на [127.0.0.1:80](https://127.0.0.1:80)

## Prod-версия c поддержкой HTTPS
Создайте `.env` файл с данными, по инструкции в секции *Dev-версия*. Добавьте к нему почту для certbot, которая будет использоваться при регистрации ssl сертификата:
```
CERTBOT_EMAIL=example@email.com
```
Далее в файле *nginx_ssl/nginx_ssl.conf* замените {your hostname} на домен вашего сайта

Собираем и запускаем контейнер:
```
docker-compose -f docker-compose.prod_ssl.yaml up --build
```
логи сервисов можно посмотреть выполнив в консоли команду:
```
docker-compose -f docker-compose.prod_ssl.yaml logs -f
```
