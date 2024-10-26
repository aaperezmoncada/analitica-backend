FROM ubuntu:latest
LABEL authors="alvaro"
ENTRYPOINT ["top", "-b"]
FROM python:3.9
EXPOSE 5001
WORKDIR /analitica
COPY . /analitica/
RUN pip install pipenv && pipenv install
ENV PYTHONPATH /manejoClientes
ENTRYPOINT ["pipenv", "run", "python", "./src/main.py"]