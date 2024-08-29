
FROM python:3.9.16-slim

WORKDIR /usr/src/model

COPY ./req.txt ./req.txt
RUN pip install -r ./req.txt

COPY ./app ./app/

EXPOSE $API_PORT

ENTRYPOINT ["python", "./app/main.py"]