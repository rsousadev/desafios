# IDwall Test
# Version: 1.0
FROM python:3.10


# Project Files and Settings
RUN mkdir -p /opt/idwall
WORKDIR /opt/idwall
COPY requirements.txt /opt/idwall/
RUN pip3 install -r requirements.txt

COPY . /opt/idwall/


CMD ["python", "main_bot.py"]

