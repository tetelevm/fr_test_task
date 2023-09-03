FROM node:20-alpine3.18 as base-frontend

WORKDIR /frontend
COPY . .

RUN npm install --force


FROM base-frontend as dev-frontend

EXPOSE 3000

CMD ["npm", "run", "serve"]
