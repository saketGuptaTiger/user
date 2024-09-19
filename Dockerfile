FROM ubuntu:rolling

RUN apt-get update && apt-get install -y sudo

RUN \
sudo apt-get update && \
sudo apt-get install -y \
        software-properties-common build-essential 



RUN \
sudo apt-get update && \
sudo apt-get install -y \
        pkg-config

RUN \
sudo apt-get update && \
sudo apt-get install -y \
	  libssl-dev libdbus-1-dev libdbus-glib-1-dev

RUN \
sudo apt-get update && \
sudo apt-get install -y \
        python3.12 python3-venv 


RUN \
sudo apt-get update && \
sudo apt-get install -y \
	   python3-dbus libffi-dev libkrb5-dev

# Install required packages
RUN apt-get update && \
    apt-get install -y python3-pip


COPY . /app

WORKDIR /app


# Create a virtual environment
RUN python3 -m venv venv

# Upgrade pip inside the virtual environment and install dependencies
RUN ./venv/bin/pip install --upgrade pip && ./venv/bin/pip install -r requirements.txt

WORKDIR /app/user-sync.py

RUN ../venv/bin/pip install external/okta-0.0.3.1-py2.py3-none-any.whl

RUN ../venv/bin/pip install ./sign_client

RUN ../venv/bin/pip install -e .

RUN make

EXPOSE 8080
ENTRYPOINT ["../venv/bin/python3"]
CMD ["../src/app.py"]

 
