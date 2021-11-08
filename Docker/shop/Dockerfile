FROM python:latest
COPY Shop/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/app

COPY ./Docker/shop/docker-entrypoint.sh ./Docker/shop/wait-for-command.sh ./Docker/shop/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

COPY Shop /usr/app

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["sh /runserver.sh"]