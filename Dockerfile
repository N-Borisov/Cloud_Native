FROM python:3.8
LABEL maintainer="Nikolay Borisov"

ARG USER
ENV MYSQL_DATABASE_USER =$USER
ARG PASS
ENV MYSQL_DATABASE_PASSWORD =$PASS

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

# command to run on container start
CMD [ "python", "app.py" ]