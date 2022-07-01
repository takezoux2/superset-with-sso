FROM apache/superset:latest

USER root
RUN pip install pybigquery Authlib
RUN superset db upgrade && superset init

RUN pip install shillelagh[gsheetsapi] PyAthena
USER superset
COPY config/* /app/pythonpath/
