### This file defines the application's image content ###

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Setup working directory
WORKDIR /src

# Install dependencies
COPY app/requirements.txt /src/app/
RUN pip install --no-cache-dir -r /src/app/requirements.txt

# Copy project
COPY . /src/

# Make the check_code.sh script executable
RUN chmod +x /src/sdlc/check_code

# Expose the application port
EXPOSE 8000

# Start the Django server
ENTRYPOINT ["/src/cmd/run"]