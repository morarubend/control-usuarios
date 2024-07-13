FROM node:latest AS build
COPY ./vue /vue
WORKDIR /vue
RUN npm install && npm run build