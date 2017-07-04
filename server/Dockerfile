FROM node:6-slim

WORKDIR /app

COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock
RUN yarn install

COPY ./src /app/src