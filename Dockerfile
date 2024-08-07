# Use the official Streamlit image from Docker Hub
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "app.py"]

