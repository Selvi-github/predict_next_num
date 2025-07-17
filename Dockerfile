# Use official Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy local files to container
COPY . .

# Upgrade pip and install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Set environment variable to prevent Streamlit from asking for user input
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_PORT=8501 \
    STREAMLIT_SERVER_ENABLECORS=false

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
