# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn textblob \
    && python -m textblob.download_corpora

# Expose the port your app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
