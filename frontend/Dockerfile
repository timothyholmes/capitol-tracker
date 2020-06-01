FROM node

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install react-scripts -g

# add app
COPY . ./

# start app
CMD ["npm", "start"]