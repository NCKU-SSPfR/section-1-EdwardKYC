FROM python:3.11

RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]
#hi