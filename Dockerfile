FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y procps htop nano

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "other_codebase_client.py"]
