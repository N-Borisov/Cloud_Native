FROM python:3.8
LABEL maintainer="Nikolay Borisov"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

# command to run on container start
CMD [ "python", "app.py" ]