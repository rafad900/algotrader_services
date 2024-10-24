FROM python:3.11-slim

# Install Python and other dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENV=PROD
WORKDIR /app

# Copy the rest of the application code
COPY . /app

EXPOSE 8000

RUN chmod +x /app/setup.sh


CMD ["/app/setup.sh"]