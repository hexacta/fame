FROM node:6

WORKDIR /code

COPY package.json /code/package.json
RUN yarn install
RUN mv /code/node_modules /node_modules

COPY . /code

