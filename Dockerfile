FROM python:3.11-slim
RUN apt-get update && apt-get install -y chromium
RUN playwright install chromium
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "demo.py", "--server.port=8501"]
