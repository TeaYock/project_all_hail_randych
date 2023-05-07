FROM python:3.12-rc-slim-bullseye
COPY ["swagger/", ".env", "api.py", "db_commands.py", "file_reader.py", "filesToRead/"]
COPY requirements.txt /app/
ADD . app/
WORKDIR /app
RUN apt update && apt install libpq-dev postgresql gcc -y
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev
RUN pip install -r requirements.txt
RUN apt -y autoremove
CMD python api.py & python swagger/swagger.py