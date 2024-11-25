FROM python:3.13

ENV PYTHONUNBUFFERED 1

WORKDIR /tasktracker

COPY requirements.txt /tasktracker/
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

COPY . /tasktracker/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
