FROM python:3.11.4-bookworm

WORKDIR /rag

COPY . .

RUN pip install -r  requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

