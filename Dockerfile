FROM python:3.10
COPY req_mqtt.txt /app/req_mqtt.txt
RUN pip install --upgrade pip
RUN pip install -r /app/req_mqtt.txt
COPY main.py /app
WORKDIR /app
CMD ["python", "main.py"]