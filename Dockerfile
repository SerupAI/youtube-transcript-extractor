# Use Python 3.11 base image optimized for Apify
FROM apify/actor-python:3.11

# Copy source code
COPY . ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install yt-dlp system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Specify how to launch the actor
CMD python -m src