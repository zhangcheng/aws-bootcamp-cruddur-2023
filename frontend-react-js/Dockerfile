FROM node:16.18

ENV PORT=3000

RUN useradd --create-home --shell /bin/bash app
USER app
WORKDIR /home/app

COPY --chown=app:app . frontend-react-js
WORKDIR frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
