FROM python:latest
WORKDIR /container
COPY . /container
RUN pip install requests
RUN pip install wikipedia-api
RUN pip install pymongo
CMD ["python", "wiki.py"]
