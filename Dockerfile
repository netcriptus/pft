FROM python:3.8.3-alpine
WORKDIR /app
COPY . .
RUN pip install -U pip
RUN pip install -r requirements.txt
CMD sleep 3600
