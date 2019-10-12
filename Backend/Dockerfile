FROM python:3.7
WORKDIR /usr/backend
COPY . .
RUN python3 -m pip install --trusted-host pypi.org -r requirements.txt
CMD ["python3", "start_website.py"]