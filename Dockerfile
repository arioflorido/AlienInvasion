FROM python:3.8.18-alpine3.18

# Set the environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /code

# Install the dependencies
COPY Pipfile Pipfile.lock ./
RUN python3 -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --python 3

COPY . .
