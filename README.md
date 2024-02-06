[![logo.png](logo.png)](https://hpi.de/en/kisz/home.html)

# Containerize your intelligence: A hands-on Workshop on Deploying AI models with Docker
Welcome to our workshop on deploying machine learning models using Docker, hosted by the AI Service Center in Berlin-Brandenburg. 
Visit our [website](https://hpi.de/en/kisz/home.html) for more details about our offerings!

## Open this Repository on Gitpod
We can follow this workshop fully through Gitpod's VSCode, **no need to install software locally**, but we also provide the instructions for a local installation as an option.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/KISZ-BB/kisz-mlops-docker/)

## Local Installation Guide
This guide provides instructions for installing and setting up all the tools and environments you need to participate in the workshop.
Familiarity with opening and using a terminal is required. Here's how you can start a terminal:

- **On Windows:** Search for `cmd` or `Command Prompt` in the Start menu.
- **On Mac:** Open the `Terminal` app from the Utilities folder.
- **On Linux:** Use your distribution's default terminal.

### Step 1: Install Git
- **Purpose of Git:** Git is a version control system essential for managing code changes and collaboration.
- **How to Install:** Download and install Git by following the instructions on [Git Guides](https://github.com/git-guides/install-git).
- **Verify Installation:** In the terminal, run `git --version`. The output should display the Git version. You may need to restart your terminal before this command becomes accessible.

### Step 2: Install Docker
Please install Docker before attending the workshop. Detailed instructions are provided below.

- **Purpose of Docker:** Docker is key for creating and running containerized applications, ensuring consistency across environments.
- **How to Install:** Follow the installation instructions based on your OS:
  - [Windows](https://docs.docker.com/desktop/install/windows-install/)
  - [Mac](https://docs.docker.com/desktop/install/mac-install/)
  - [Linux](https://docs.docker.com/desktop/install/linux-install/)
- **Verify Installation:** In the terminal, run `docker --version`. The output should display the Docker version. Restarting your computer may be necessary before this command becomes accessible.

### Step 3: Install an IDE
- **What's an IDE?** An Integrated Development Environment (IDE) is a platform for coding, editing, and debugging your code. It also serves as a graphical user interface for Git.
- **Recommended IDEs:** 
  - [Visual Studio Code](https://code.visualstudio.com/) - Versatile and lightweight.
  - [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) - Tailored for Python development.
- **Verify Installation:** You can verify your installation by cloning a GitHub repository. Please refer to the following guides:
  - [Visual Studio Code - Clone Guide](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette#clone-repository)
  - [PyCharm - Clone Guide](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)

### Troubleshooting and Support
If you encounter installation issues, consult the respective software's documentation or contact us at [kisz@hpi.de](mailto:kisz@hpi.de) for assistance.

### What's Next?
Once you've installed Git, Docker, and an IDE, you're all set for our workshop. We're excited to introduce you to the world of MLOps and Docker!

## Workshop Hands-On
### Hands-On 1: Hello-World toy example
1. (Optional) Look for the ```hello-world``` Docker image on Docker hub: https://hub.docker.com/
2. Download the Docker image using the command: ```docker pull hello-world```
3. List your Docker images with the command: ```docker image ls```
4. Create a container using the ```hello-world``` image by running: ```docker run hello-world```
5. List your Docker containers using: ```docker ps --all```
6. Remove your Docker container with the command: ```docker rm [ID]```
7. Create a self-deleting container with the ```hello-world``` image using: ```docker run --rm hello-world```

### Hands-On 2: Running Jupyter with Docker
1. Download the image: ```docker pull jupyter/base-notebook```
2. Start a self-deleting container using the command: ```docker run --rm jupyter/base-notebook```
3. Read the terminal output can you access it?
5. Forward the port ```8888``` from the Docker container to the host machine: ```docker run -p 8888:8888 --rm jupyter/base-notebook```

### Hands-On 3: Bind Mount
**Problem:** The container cannot access our file on our host machine. 

**Solution:** Use a bind mount to access our **model** directory inside the Jupyter Notebook.

**Task:** Complete the following command: ```docker run […] -p 8888:8888 --rm jupyter/base-notebook```

1. Read Docker Documentation: https://docs.docker.com/storage/bind-mounts/
2. **Hint:**  Mount the **model** source folder from the clone of the workshop code to the ```/home/jovyan/work``` target folder in the Docker container.

### Hands-On 4: FastAPI
**Task:** Fill out the **TODOs** in the ```app/api.py``` file
1. Read the FastAPI documentation: https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter
2. Read about the request body: https://fastapi.tiangolo.com/tutorial/body/
3. Setup a test environment by running `docker run --rm -it -p 8000:8000 -v .:/app python:3.11 bash` in the base directory of the checked out repository.
4. You should be dropped into a `bash` environment in a new python docker container. You can run `cd /app` to change the current path to the repository.
5. You can test if your API is correctly defined py running `python3 app/api.py` and opening `http://0.0.0.0:8000` in your browser.


### Hands-On 5: Dockerfile
1. Create a file with the name **Dockerfile**
2. Find **Python version 3.11** on [Docker Hub](https://hub.docker.com/) and use it as a Base Image: ```FROM your-base-image:1.0```
3. Change the working directory inside of the container: ```WORKDIR /app```
4. Copy the ```requirements.txt``` file from the host file system into the docker container: ```COPY requirements.txt /to-container/```
5. Run a pip install for all the packages required: ```RUN pip install -r requirements.txt```
6. Copy the rest of the application into the container: ```COPY /from-host/ /to-container/```
7. Start the uvicorn server through the terminal command: ```CMD uvicorn app.location:api_name --host 0.0.0.0```

### Live-Demo: Deploying the Container with Docker Compose
1. Build and run the Docker container with Docker Compose: ```docker compose up --build```
2. **Problem:** Container shuts down when terminal closes. **Solution:** ```docker compose up -d```
3. **Problem:** Container doesn't restart when machine restarts. **Solution:** Add ```restart:always``` to the ```compose.yaml``` file.
4. **Problem:** Application has errors and I need to see the logs. **Solution:** Use ```docker ps``` to get the container ID and then use  ```docker logs [ID]``` to read the logs.
5. Close the container using  ```docker compose down```
