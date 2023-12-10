FROM nginx:1.25-alpine AS fr-base-nginx

FROM fr-base-nginx AS fr-nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
COPY uwsgi_params /etc/nginx/uwsgi_params
COPY proxy_params /etc/nginx

WORKDIR /app

EXPOSE 80
