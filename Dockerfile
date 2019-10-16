FROM python:3

ADD . /token_service

RUN pip3 install -r /token_service/requirements.txt && pip3 install gunicorn


EXPOSE 8000
WORKDIR /token_service/token_service
CMD ["gunicorn", "-b", "0.0.0.0:8000", "token_service:app"]
