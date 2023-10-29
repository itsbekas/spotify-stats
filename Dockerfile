FROM python:3.11-alpine

# Flask needs SIGINT to exit gracefully (Docker sends SIGTERM by default)
STOPSIGNAL SIGINT

WORKDIR /app

COPY . /app

COPY ./.env /app/.env

RUN pip install -r requirements.txt

RUN pip install .

EXPOSE 5000

CMD ["spotifystats", "run-api"]
