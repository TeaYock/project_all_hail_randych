FROM python:3.12-rc-slim-bullseye
WORKDIR /app/
COPY requirements.txt /app/
COPY ./db_dumps/randych_db.sql /docker-entrypoint-initdb.d/
RUN apt update && apt install libpq-dev postgresql gcc -y
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev
RUN pip install -r requirements.txt
RUN apt -y autoremove
COPY swagger/ db_variables api.py db_commands.py file_reader.py filesToRead/ /app/
ADD . app/
CMD python api.py