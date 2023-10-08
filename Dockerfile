FROM python:3.8.18-alpine3.18

# Set the environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /code

# Install the dependencies
COPY Pipfile Pipfile.lock ./
RUN apt-get update && apt-get install -y python-dev-is-python3 libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
RUN python3 -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --python 3

COPY . .
