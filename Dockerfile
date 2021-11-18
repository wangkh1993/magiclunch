FROM python:3.7

WORKDIR /magiclunch
COPY . /magiclunch

RUN pip install -r requirements.txt

# CMD ["python", "main.py"]