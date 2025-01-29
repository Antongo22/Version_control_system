# Version Control System

## Installation and Running

### Prerequisites
1. **Python** - Ensure that you have Python 3.6 or higher installed.
2. **Flask** - A library for creating web applications in Python.

### Step 1: Cloning the Repository

To begin, you need to clone the repository to your local machine:

```bash
git clone https://github.com/Antongo22/Version_control_system.git
cd Version_control_system
```

### Step 2: Installing Python

If you don't have Python installed yet, follow these steps:

#### For Windows:
1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download and install the latest version of Python (3.6 or higher).
3. During installation, make sure to check the option "Add Python to PATH".

#### For macOS:
1. Open a terminal and run the following command:
   ```bash
   brew install python
   ```

#### For Linux:
1. Open a terminal and run the following commands:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

### Step 3: Installing Flask

After installing Python, you need to install Flask. This can be done using the pip package manager.

Open a terminal and navigate to the project directory:

```bash
cd Version_control_system
```

Then, install Flask:

```bash
pip install Flask
```

### Step 4: Running the Application

Now that all the necessary components are installed, you can run the application.

In the terminal, execute the following command:

```bash
python app.py
```

This will start the built-in Flask server at `http://127.0.0.1:5000/`.

### Step 5: Using the Application

Open a browser and go to `http://127.0.0.1:5000/`.

You will see a form where you can enter the position number for the Fibonacci sequence. After entering the number and clicking the "Calculate" button, the application will compute the corresponding value and display it on the page.