# start with CUDA runtime image
FROM nvidia/cuda:11.8.0-base-ubuntu20.04 

# set environment variables for CUDA
ENV CUDA_VERSION=11.8.0

# install dependencies
RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	&& rm -rf /var/lib/apt/lists/*

# set the working directory
WORKDIR /app

# copy in repo requirements
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy in the remainder of the code
COPY . /app

# default for now: run the training script
ENTRYPOINT ["python3", "main.py"]
