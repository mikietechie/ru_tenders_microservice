FROM python:bullseye
WORKDIR /src
COPY requirements.txt /src
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY . /src
CMD ["python3", "main.py"]