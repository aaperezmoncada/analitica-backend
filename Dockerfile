FROM python:3.9

EXPOSE 5005

WORKDIR /analitica

COPY . /analitica/

RUN pip install pipenv && pipenv install

ENV PYTHONPATH /analitica

ENTRYPOINT ["pipenv", "run", "python", "./src/main.py"]