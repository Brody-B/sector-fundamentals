FROM python:3.10-slim

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "streamlit", "run", "app.py" ]