FROM python:3.10-slim
COPY /build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ADD /src /app
CMD ["python", "app/main.py"]
