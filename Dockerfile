FROM python:3.10.13-slim-bullseye


WORKDIR /django_app_dir

COPY requirements.txt requirements.txt

COPY .  .



ENV PYTHONUNBUFFERED 1  

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip  


RUN pip3 install -r requirements.txt


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]