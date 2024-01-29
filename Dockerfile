FROM python:3.8.2-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]