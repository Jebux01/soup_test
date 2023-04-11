FROM python:3.11
# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 8000
CMD ["python", "main.py"]