FROM python:3.8.8-slim

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 8000
COPY . /app
WORKDIR /app

CMD ["python", "application.py"]

