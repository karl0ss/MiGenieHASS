FROM python:3.8-slim
RUN mkdir /app 
COPY /app /app
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root
CMD [ "python", "main.py"]


