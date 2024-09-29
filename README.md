
# Slide Camera Presentation

This is a simple Python application to present slides while displaying your webcam feed in the corner of the screen.

## Requirements

### 1. Install Anaconda (if not already installed)

If you don't have Anaconda installed, you can download and install it from [here](https://www.anaconda.com/products/distribution).

### 2. Create and Activate a Conda Environment

You can create an isolated environment using Anaconda to manage dependencies easily.

1. **Create the environment**: Open a terminal (or Anaconda Prompt) and run:

    ```bash
    conda create -n slide_camera python=3.9
    ```

    This creates a new environment named `slide_camera` with Python 3.9.

2. **Activate the environment**:

    ```bash
    conda activate slide_camera
    ```

    Now, your environment is active, and you can proceed to install the required libraries.

### 3. Install the Required Libraries

With the environment activated, you can install the necessary packages. Run the following command:

```bash
pip install -r requirements.txt
```

This will install `opencv-python` and `Pillow`. **Tkinter** is not included in `requirements.txt` because it usually comes pre-installed with Python. If you are on Linux, you might need to install Tkinter separately (see below for details).

### 4. Install Tkinter (if necessary)

In some cases, Tkinter might not be pre-installed, depending on your operating system. Follow the instructions below based on your OS:

- **Linux (Ubuntu/Debian)**: Install Tkinter using:

    ```bash
    sudo apt-get install python3-tk
    ```

- **Windows**: Tkinter is usually included with the Python installation on Windows, so no additional steps are required.

- **macOS**: Tkinter is also generally included with Python on macOS. If needed, you can install or update Tkinter with:

    ```bash
    brew install python-tk
    ```

## How to Run

1. Ensure your Anaconda environment is activated:

    ```bash
    conda activate slide_camera
    ```

2. Run the application:

    ```bash
    python main.py
    ```

3. Use the **"Load Slides"** button to select the images you want to use as slides.

4. Navigate through the slides using the **"Next"** and **"Previous"** buttons. Your webcam feed will be displayed in the corner of the screen during the presentation.

## Features

- Display slides from selected image files.
- Show webcam feed in a corner during the presentation.
- Navigate through slides with 'Next' and 'Previous' buttons.

## Troubleshooting

- **Camera not working**: Ensure that no other application is using the camera and that the correct camera driver is installed.
- **Tkinter not found**: If Tkinter is not installed, follow the instructions in the [Install Tkinter](#4-install-tkinter-if-necessary) section.
- **Issues with OpenCV**: Sometimes OpenCV has issues with certain camera models or drivers. Make sure your version of OpenCV is compatible with your hardware.
