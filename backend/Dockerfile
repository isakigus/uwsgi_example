FROM alpine:3.7
EXPOSE 3031 4444
VOLUME /usr/src/app/public
WORKDIR /usr/src/app
RUN apk add --no-cache \
    uwsgi-python3 \
    python3
RUN apk add --update --no-cache netcat-openbsd
COPY . .
RUN rm -rf public/*
RUN pip3 install --no-cache-dir -r requirements.txt
# CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
#                "--uid", "uwsgi", \
#                "--plugins", "python3", \
#                "--protocol", "uwsgi", \
#                "--wsgi-file", "public/main.py" ]


CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
    "--uid", "uwsgi", \
    "--plugins", "python3", \
    "--protocol", "uwsgi", \
    "--py-autoreload","1", \
    "--wsgi", "public.main:application" ]