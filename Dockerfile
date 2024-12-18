# start with lightweight system image
FROM python:3.11-slim

# set the working directory
WORKDIR /app

# copy in repo requirements
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy in the remainder of the code
COPY . /app

# default for now: run the training script
ENTRYPOINT ["python", "main.py"]
