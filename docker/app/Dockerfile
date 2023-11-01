FROM python:3.11.6-bookworm
WORKDIR /app
ARG DEV=false
COPY ./src/requirements.txt ./src/requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    if [ $DEV = "true" ]; then pip install --no-cache-dir -r requirements-dev.txt; fi
COPY . .