FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files to working directory
COPY . .

# Expose ports for the container
EXPOSE 80 

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

# Run the application with Waitress
CMD waitress-serve --listen=*:80 app:app
