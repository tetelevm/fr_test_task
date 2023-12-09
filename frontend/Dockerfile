FROM node:20-alpine as fr-base-frontend

WORKDIR /frontend
COPY . .

RUN npm install --force

FROM fr-base-frontend as fr-frontend

EXPOSE 3000
ENTRYPOINT ["npm", "run", "serve"]
