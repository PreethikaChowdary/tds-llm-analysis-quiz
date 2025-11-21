# Use official Playwright image (comes with Chromium pre-installed 🎉)
FROM mcr.microsoft.com/playwright/python:v1.56.0-jammy

# Set work directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the code
COPY . /app

# Expose port for Render
ENV PORT=8000

# Start FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
