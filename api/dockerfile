FROM python:3.9.6
ADD ./ /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD ["python", "main.py"]