FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myDir
WORKDIR /myDir
ADD . /myDir/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000
