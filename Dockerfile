# Use Python base image with CUDA support - much smaller and faster
FROM pytorch/pytorch:2.9.0-cuda12.8-cudnn9-runtime

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    libsndfile1 \
    libsndfile1-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PIP_CACHE_DIR="/tmp/pip-cache"
ENV TORTOISE_MODELS_DIR="/app/models"

# Copy requirements first for better caching of dependency installation
COPY requirements.txt ./

# Install Python dependencies using pip (much faster than conda)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch==2.9.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 && \
    # Install core dependencies that were in the original conda environment
    pip install --no-cache-dir numba inflect

# Copy the entire application (needed for setup.py to have all required files)
COPY . .

# Install the package itself - this will handle all dependencies from setup.py
# Skip problematic packages from requirements.txt and let setup.py control versions
RUN pip install --no-cache-dir -e . && \
    # Install additional packages from requirements.txt that aren't in setup.py
    pip install --no-cache-dir \
        threadpoolctl \
        llvmlite \
        appdirs \
        nbconvert==5.3.1 \
        tornado==4.2 \
        pydantic==2.9.2 \
        deepspeed==0.8.3 \
        py-cpuinfo \
        hjson \
        sounddevice \
        spacy==3.7.5 && \
    python -m pip install --no-cache-dir \
        https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1.tar.gz


# Create models directory
RUN mkdir -p /app/models
