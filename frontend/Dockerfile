FROM node:24-alpine AS build

WORKDIR /app

# Nuxt build peut consommer beaucoup de heap; on augmente la limite pour éviter OOM en Docker Desktop.
ENV NODE_OPTIONS="--max-old-space-size=4096"

COPY package*.json .

RUN npm install

COPY . .

RUN npm run build

FROM node:24-alpine AS prod

WORKDIR /app

COPY --from=build /app/.output /app/.output

ENV NODE_ENV=production

EXPOSE 3000

CMD [ "node", ".output/server/index.mjs" ]
