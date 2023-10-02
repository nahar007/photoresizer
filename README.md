# photoresizer
This is a Python script using the tkinter library to create a graphical user interface (GUI) for an image resizing tool.
# Image Resizer

This Python script provides a simple graphical user interface (GUI) for resizing images. It uses the tkinter library for the GUI, the Pillow library for image processing, and the os library for file operations.

## Features

- Allows the user to select a source folder containing images or a single image file.
- Enables the user to specify a destination folder for the resized images.
- Provides options to set the width and height for the resized images.
- Supports the conversion of multiple image formats (jpg, png).

## Getting Started

### Prerequisites

- Python 3.x
- Pillow library (install with `pip install Pillow`)

### Running the Application

1. Run the `image_resizer.py` script using Python.

```bash
python image_resizer.py
```

2. The GUI window will appear with the following options:

   - **Source Folder/File**: Click "Browse Folder" to select a folder containing images or "Select File" to choose a single image file.

   - **Destination Folder**: Click "Browse" to choose a destination folder where the resized images will be saved.

   - **Width** and **Height**: Enter the desired dimensions for the resized images.

   - Click the "Convert" button to initiate the resizing process.

   - Close the window when you're finished.

## How It Works

- The script uses tkinter for the GUI, allowing users to interact with the application through buttons, entry fields, and labels.

- The Pillow library is used for image processing. It reads images, resizes them based on user input, and saves them in the specified destination folder.

- If a folder is selected as the source, the script will iterate through all the images in the folder, resize them, and save them in the destination folder.

- Any errors encountered during the process will be displayed in a message box.

## Example Usage

1. Select a source folder containing images.

2. Choose a destination folder where the resized images will be saved.

3. Enter the desired width and height.

4. Click the "Convert" button.

5. Success or error messages will be displayed accordingly.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Pillow library: https://pillow.readthedocs.io/en/stable/
- tkinter documentation: https://docs.python.org/3/library/tkinter.html

---

Feel free to modify this readme file to suit your specific project details and preferences.
