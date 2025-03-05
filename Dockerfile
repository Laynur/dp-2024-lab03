FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["bash", "-c", "python -m unittest discover -s ./unit_test  -p 'test.py'"]