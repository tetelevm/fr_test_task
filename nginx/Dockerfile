FROM nginx:1.25-alpine as fr-base-nginx

FROM fr-base-nginx as fr-nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
COPY uwsgi_params /etc/nginx/uwsgi_params

WORKDIR /app

EXPOSE 80
