FROM python:3.10

ENV NOTION_TOKEN=
ENV TASKS_DATABASE_ID=

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "-u", "main.py"]
