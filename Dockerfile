FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
COPY main.py .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 21080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "21080"]