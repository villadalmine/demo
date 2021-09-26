FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
ADD demo.py /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "demo:app"]
