FROM python:3.7-buster

RUN apt-get update && apt-get install -y libev-dev
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt && rm /requirements.txt

WORKDIR /app
COPY copenapi /app/openapi
COPY src /app/src
COPY api.py /app/

EXPOSE 8080

CMD ["python3", "api.py"]
