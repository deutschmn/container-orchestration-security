FROM python:3
COPY main.py server.py /
RUN pip install kubernetes
EXPOSE 8000
CMD [ "python", "./main.py" ]