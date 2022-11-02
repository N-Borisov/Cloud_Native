FROM python:3.8
LABEL maintainer="Nikolay Borisov"

ARG user
ENV MYSQL_DATABASE_USER $user
ARG pass
ENV MYSQL_DATABASE_PASSWORD $pass

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

# command to run on container start
CMD [ "python", "app.py" ]