# Use the official python image as a parent image
FROM python:3.11-slim
# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file to the container
COPY ./requirements-prod.txt ./
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements-prod.txt
# Copy the rest of the application
COPY ./ ./
# Run the command to start uvicorn
CMD ["uvicorn", "app.api:model_api", "--host", "0.0.0.0"]
