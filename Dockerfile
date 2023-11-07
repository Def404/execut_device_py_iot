FROM python:3.10
WORKDIR /app
COPY req_mqtt.txt .
RUN pip install --upgrade pip
RUN pip install -r /req_mqtt.txt
COPY main.py .
CMD ["python", "./main.py"]