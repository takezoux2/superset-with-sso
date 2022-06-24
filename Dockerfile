FROM apache/superset:latest

RUN pip install pybigquery pyathenajdbc Authlib

COPY config/* /app/pythonpath/

RUN superset db upgrade && superset init
# RUN superset db upgrade && superset init



