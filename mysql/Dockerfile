FROM mysql

ENV MYSQL_DATABASE employees_db
ENV MYSQL_ROOT_PASSWORD root
COPY ./mysql_script.sql /docker-entrypoint-initdb.d/  

