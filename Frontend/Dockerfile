FROM node:12.8.0-alpine
WORKDIR /usr/frontend
COPY . .
RUN npm install
RUN npm install react-scripts -g
RUN npm run build