FROM ubuntu:20.04
RUN apt-get update
RUN apt install python3.8 -y python3-pip docker.io docker-compose supervisor
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /var/log/supervisor
COPY /config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
