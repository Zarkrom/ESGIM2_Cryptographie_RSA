FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /srv/app
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup -g ${GROUP_ID} pythoniste && \
    adduser -u ${USER_ID} -G pythoniste -s /bin/sh -D pythoniste
RUN chown pythoniste:pythoniste /srv/app
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN apk del build-deps
COPY . /srv/app
USER pythoniste