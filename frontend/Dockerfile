FROM node:16-alpine

ENV BACKEND_URL=http://backend-host:8000/receive

WORKDIR /app

ADD . /app

RUN npm install

ENTRYPOINT ["npm"]

CMD ["start"]