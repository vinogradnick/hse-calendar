FROM python:3.7
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python","setup.py","install" ]
CMD ["pip3","install","requests",'google-api-python-client','google-auth-httplib2','google-auth-oauthlib'];

RUN ["python","./index.py"];