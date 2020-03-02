FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash vim
RUN cd ..
COPY ./app.py app.py
RUN pip3 install Flask
EXPOSE 5000
ENTRYPOINT python3 app.py
