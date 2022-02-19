FROM python:alpine 

LABEL maintainer="Jeeva S. Chelladhurai"

COPY src/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]

