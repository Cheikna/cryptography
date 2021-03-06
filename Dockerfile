FROM python:3.8-slim

COPY . .

RUN pip install flask numpy

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]
