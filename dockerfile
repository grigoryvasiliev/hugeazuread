FROM python:3.6-alpine
COPY . /app
WORKDIR /app
CMD ["python","gen2.py"]
