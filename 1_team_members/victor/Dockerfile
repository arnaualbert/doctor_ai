FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000 

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

CMD ["python","app.py"]