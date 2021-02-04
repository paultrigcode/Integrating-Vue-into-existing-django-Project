FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN apt-get clean && apt-get -y update && apt-get install -y locales && locale-gen en_US.utf8 && update-locale && apt install -y vim
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
RUN pip install -r requirements.txt
RUN pip install inotify
RUN pip install gunicorn
RUN pip install https://github.com/oshosanya/django-angular/archive/python3-upgrade.zip
RUN export PATH=$PATH:~/.local/bin
COPY . /src/
RUN chmod +x /src/run.sh
EXPOSE 8000
CMD ["/src/run.sh"]