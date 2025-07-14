# Etapa 1: Build
FROM node:22-alpine AS build

WORKDIR /app

COPY ./vigilo-dashboard/package*.json ./
RUN npm install

COPY ./vigilo-dashboard/ .
RUN npm run build


EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
