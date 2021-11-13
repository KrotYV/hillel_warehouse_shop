FROM python:latest

COPY warehouse/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/app

COPY docker/warehouse/docker-entrypoint.sh docker/warehouse/wait-for-command.sh docker/warehouse/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

COPY warehouse /usr/app

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["sh /runserver.sh"]
