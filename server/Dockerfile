FROM node:6-slim

WORKDIR /code

COPY package.json /code/package.json
COPY yarn.lock /code/yarn.lock
RUN yarn install
RUN mv /code/node_modules /node_modules