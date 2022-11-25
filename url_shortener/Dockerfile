#
FROM python:3.10

#
WORKDIR /url_shortener

#
COPY ./requirements.txt /url_shortener/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /url_shortener/requirements.txt

#
COPY ./app /url_shortener/app

#
WORKDIR /url_shortener/app

EXPOSE 8000
# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"]