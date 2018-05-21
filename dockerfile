FROM python:3.6-alpine
RUN apk add --no-cache bash
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gen.sh"]
CMD []
