FROM node:20-alpine AS fr-base-frontend

WORKDIR /frontend
COPY . .

RUN npm install --force

FROM fr-base-frontend AS fr-frontend

EXPOSE 3000
ENTRYPOINT ["npm", "run", "serve"]
