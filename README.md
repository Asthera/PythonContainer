### Matrix Multiplication with PyTorch and Web Application

This project consists of two Docker containers:
1. **PyTorch Container**: A Flask API that performs matrix multiplication using PyTorch.
2. **Web Container**: A Flask-based web application that allows users to input two matrices and displays the multiplication result by communicating with the PyTorch container.

---

### Running the Project

There are two ways to run the project:

#### Option 1: Running Containers Individually

1. **Build and Run PyTorch Container**:
   - Navigate to the project root directory.
   - Build the PyTorch Docker image:
     ```bash
     docker build -t pytorch-matrix-multiplier .
     ```
   - Run the PyTorch container:
     ```bash
     docker run -d -p 5001:5001 --name pytorch-container pytorch-matrix-multiplier
     ```

2. **Build and Run Web Container**:
   - Navigate to the `web_app` directory.
   - Build the web app Docker image:
     ```bash
     docker build -t web-app .
     ```
   - Run the Web container:
     ```bash
     docker run -d -p 5002:5002 --name web-container --link pytorch-container web-app
     ```

3. **Access the Web Application**:
   - Open your browser and go to `http://localhost:5002`.
   - Enter two 2x2 matrices and click "Multiply Matrices" to view the result.

#### Option 2: Running with Docker Compose (Recommended)

1. **Setup Docker Compose**:
   - Create a `docker-compose.yml` file in the root project directory:
   
   ```yaml
   version: "3.8"
   services:
     pytorch-container:
       build:
         context: .
         dockerfile: Dockerfile
       ports:
         - "5001:5001"
     
     web-container:
       build:
         context: ./web_app
         dockerfile: Dockerfile
       ports:
         - "5002:5002"
       depends_on:
         - pytorch-container
   ```

2. **Build and Run with Docker Compose**:
   - In the root project directory, run:
     ```bash
     docker-compose up --build
     ```

3. **Access the Web Application**:
   - Open your browser and go to `http://localhost:5002`.
   - Enter two 2x2 matrices and click "Multiply Matrices" to view the result.

---

### Directory Structure

```
/project-root
  ├── Dockerfile                # PyTorch container Dockerfile
  ├── docker-compose.yml        # Docker Compose configuration
  ├── /web_app
  │   ├── Dockerfile            # Web app Dockerfile
  │   ├── requirements.txt      # Python dependencies for the web app
  │   └── /templates
  │       └── index.html        # HTML template for the web app
  └── requirements.txt          # Python dependencies for the PyTorch container
```

---

### Project Overview

- **PyTorch Container**: Provides an API for multiplying matrices using PyTorch. It listens on port `5001` and expects a `POST` request to `/multiply` with the matrices in JSON format.
  
- **Web Container**: Provides a simple form where users can enter two 2x2 matrices. The form sends a `POST` request to the PyTorch container and displays the result on the web page.

---

### How Communication Works

1. The web container sends a `POST` request to the PyTorch container's `/multiply` endpoint with the matrices in JSON format.
2. The PyTorch container performs the matrix multiplication using PyTorch (`torch.matmul`) and returns the result as a JSON response.
3. The web container receives the response and displays the result on the page.

---

### Dependencies

- **PyTorch Container**:
  - `flask`: To create the Flask API.
  - `torch`: To perform matrix multiplication.

- **Web Container**:
  - `flask`: To create the Flask web application.
  - `requests`: To send HTTP requests to the PyTorch container.

---

### Stopping and Removing Containers

To stop and remove containers manually, use:

```bash
docker stop pytorch-container web-container
docker rm pytorch-container web-container
```

Or, with Docker Compose:

```bash
docker-compose down
```

---

This setup allows you to scale the project with ease and manage each service individually or together using Docker Compose.