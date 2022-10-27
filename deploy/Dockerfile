FROM python:3.10-slim-bullseye AS build

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential
   
RUN python -m venv --upgrade-deps --copies /runtime

COPY requirements.txt .

RUN /runtime/bin/pip install -r requirements.txt

FROM python:3.10-slim-bullseye AS app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH /runtime/bin:$PATH

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx curl procps

COPY --from=build /runtime /runtime

COPY ./deploy/conf/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./ .

RUN chmod +x ./serve.sh

RUN groupadd fastapi && \
    useradd -g fastapi -d /app -s /bin/bash fastapi && \
    chown -R fastapi:fastapi . && \
    mkdir -p /var/log/nginx /var/lib/nginx && \
    chown -R fastapi:fastapi /var/log/nginx /var/lib/nginx

USER fastapi

CMD ["/app/serve.sh"]

EXPOSE 8080
