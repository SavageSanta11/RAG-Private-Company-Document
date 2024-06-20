FROM python:3.11.8-alpine3.19

WORKDIR /cache_api

COPY . .

RUN pip install -r  requirements.txt

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8080"]

