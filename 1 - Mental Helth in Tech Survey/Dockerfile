# app/Dockerfile

FROM python:3.9-slim

COPY ./requirements.txt /requirements.txt

EXPOSE 8501

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]