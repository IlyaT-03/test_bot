FROM python:3.8
COPY requirements.txt .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]