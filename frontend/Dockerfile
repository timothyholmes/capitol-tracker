FROM node
WORKDIR /usr/src/app
COPY package*.json ./
COPY . .
RUN npm install
RUN npm install react-script -g
RUN npm run build

EXPOSE 3000

CMD [ "npm", "start" ]