FROM python:3.12.2-slim-bookworm

WORKDIR /var/www

COPY /sql_app/requirements.txt .

RUN pip install -r requirements.txt

COPY sql_app .

CMD ["python3", "main.py"]
