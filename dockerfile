FROM python:3.9.7-slim-bullseye

RUN apt-get update && apt-get install -y curl unzip gcc vim \
    && rm -rf /var/lib/apt/lists/* 

COPY install_cg3.sh /tmp/install_cg3.sh

RUN bash /tmp/install_cg3.sh \
    && apt-get update && apt-get install -y cg3 \
    && rm -rf /var/lib/apt/lists/* \
    && rm /tmp/install_cg3.sh

RUN pip install --no-cache-dir virtualenv

RUN mkdir -p /usr/nobody/CyTag-main \
    && python -m virtualenv /usr/nobody/venv \
    && chmod -R 777 /usr/nobody

USER nobody

COPY . /usr/nobody/CyTag-main

SHELL ["/bin/bash", "-c"]

COPY requirements.txt /usr/nobody/requirements.txt

RUN source /usr/nobody/venv/bin/activate \
    && pip install --no-cache-dir -r /usr/nobody/requirements.txt \
    && rm /usr/nobody/requirements.txt

WORKDIR /usr/nobody/CyTag-main

#ENTRYPOINT ["/usr/nobody/venv/bin/python", "CyTag.py"]

EXPOSE 8000

ENV FLASK_APP=CyTag_Server.py
ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["/usr/nobody/venv/bin/flask", "run"]
