FROM python:3

ADD . /user_service

RUN pip3 install -r /user_service/requirements.txt && pip3 install gunicorn


EXPOSE 8000
WORKDIR /user_service/user_service
CMD ["gunicorn", "-b", "0.0.0.0:8000", "user_service:app"]
