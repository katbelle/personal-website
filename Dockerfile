FROM python:3.7.3
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install

CMD pipenv run python server.py