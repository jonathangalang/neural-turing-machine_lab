# start with CUDA runtime image
FROM nvidia/cuda:11.8.0-base-ubuntu20.04 

# set environment variables for CUDA
ENV CUDA_VERSION=11.8.0

# install dependencies
RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	&& rm -rf /var/lib/apt/lists/*

ARG USERNAME=mluser
ARG UID=1000
ARG GID=1000

RUN groupadd --gid $GID $USERNAME \
	&& useradd --uid $UID --gid $GID --create-home $USERNAME \
	&& mkdir /app \
	&& mkdir /app/outputs \
	&& mkdir /app/models \
	&& chown "$USERNAME":"$USERNAME" /app \
	&& chown "$USERNAME":"$USERNAME" /app/outputs \
	&& chown "$USERNAME":"$USERNAME" /app/models

USER $USERNAME

# set the working directory
WORKDIR /app

# copy in repo requirements
COPY --chown="$USERNAME":"$USERNAME" requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy in the remainder of the code
COPY --chown="$USERNAME":"$USERNAME" . /app

# entry point for this codebase is main
ENTRYPOINT ["python3", "main.py"]
