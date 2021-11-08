FROM python:latest
COPY Warehouse/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/app

COPY ./Docker/warehouse/docker-entrypoint.sh ./Docker/warehouse/wait-for-command.sh ./Docker/warehouse/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

COPY Warehouse /usr/app

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["sh /runserver.sh"]