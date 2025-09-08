FROM python:3.12
WORKDIR /app

RUN pip install flask flask_pymongo

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]