FROM node:16.14-alpine

WORKDIR /app-frontend

EXPOSE 3000

COPY ./ .

RUN npm install

RUN npm run build

CMD [ "npm", "run", "preview" ]