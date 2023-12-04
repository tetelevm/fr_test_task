FROM nginx:1.21-alpine as base-nginx

FROM base-nginx as dev-nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d
COPY ./uwsgi_params /etc/nginx/uwsgi_params

EXPOSE 80

WORKDIR /app
