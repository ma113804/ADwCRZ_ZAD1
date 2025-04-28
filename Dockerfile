FROM python:3.11-slim-buster import builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
 
# Użyj innego obrazu dla obrazu końcowego
FROM python:3.11-slim
WORKDIR /app
# Skopiuj zależności z obrazu budującego
COPY --from=builder /app /app
 
COPY app.py .
 
ENV FLASK_APP=app
 
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
