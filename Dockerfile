FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash vim
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 
COPY ./app.py app.py
COPY ./dbsetup.py dbsetup.py
ADD ./templates/ templates/
ADD ./static static/
RUN pip install --upgrade pip
RUN pip3 install Flask httpagentparser pusher
RUN python dbsetup.py
EXPOSE 5000
ENTRYPOINT flask run --host=0.0.0.0
