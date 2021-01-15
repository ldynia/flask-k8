FROM python:3.7.9-alpine

ARG PORT=80
ENV PORT=$PORT

ARG HOST=0.0.0.0
ENV HOST=$HOST

ARG FLASK_APP=/app/config/run.py
ENV FLASK_APP=$FLASK_APP

ARG FLASK_ENV=development
ENV FLASK_ENV=$FLASK_ENV

ENV HOME=/app
ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8

WORKDIR /app
COPY . /app

# Fixed permissions, create exec:exec and dev:dev
RUN sed -i '/999/d;' /etc/group
RUN addgroup -S -g 999 exec && adduser -u 999 -s /sbin/nologin -SDHG exec exec
RUN adduser -DH dev && adduser exec dev
RUN chown -R exec:dev \
    /app \
    /usr/local/bin/ \
    /usr/local/lib/python3.7/
RUN chmod -R a-w /etc

VOLUME /app
EXPOSE ${PORT}

USER exec:dev

ENTRYPOINT ["/app/scripts/startup.sh"]