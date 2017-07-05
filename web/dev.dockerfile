FROM node:6

WORKDIR /app

COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock
RUN yarn install
RUN mv /app/node_modules /node_modules

COPY . /app

