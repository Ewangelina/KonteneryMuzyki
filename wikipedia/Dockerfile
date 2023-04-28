FROM python:latest
WORKDIR /container
COPY . /container
RUN pip install requests
RUN pip install wikipedia-api
CMD ["python", "wiki.py"]