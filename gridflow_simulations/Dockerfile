# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /gridflow_simulations

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command (optional)
# You can run a specific experiment script by overriding this at runtime
CMD ["python", "./exp1/run_all_exp1.py"]
