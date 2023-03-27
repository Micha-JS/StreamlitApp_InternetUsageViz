FROM python:3.9-slim

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements_docker.txt ./

# install  pip in conda base environment
RUN conda install pip -y

# Install all the dependencies
RUN pip install -r requirements_docker.txt

COPY . . 

RUN /Users/mjs/Documents/DS_Projects/StreamlitApp_InternetUsageViz/app/internet_world.py


#CMD echo 'Hello from the other side'


