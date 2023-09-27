FROM python:3.10-slim-bullseye
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "__main__.py"]