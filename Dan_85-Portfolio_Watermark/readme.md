# Watermark App Documentation

## Overview

The Watermark App is a Python application that adds watermarks to images. It provides a simple graphical user interface (GUI) for users to select an image file, choose a watermark image, and automatically apply the watermark to the selected image.

## Features

- **Watermarking**: Automatically adds a watermark to selected images.
- **Customizable**: Users can customize various aspects of the watermarking process.
- **Simple Interface**: Easy-to-use GUI for a seamless user experience.

## Installation

1. **Clone Repository**: Clone or download the repository to your local machine.

2. **Dependencies**: Ensure you have Python installed on your system. Install the required dependencies by running the following command:
   ```
   pip install Pillow
   ```

## Configuration

Before running the application, you can customize various aspects of the watermarking process:

- **Watermark Image**: Replace the `cropped-pmf.png` file with your desired watermark image, and change it's size and positioning.
- **Target Directory**: Modify the `TARGET_DIRECTORY` variable to change the name of the folder where watermarked images will be saved.

## Usage

1. **Run Application**: Execute the `main.py` file to launch the application.

2. **Select Image**: Click the "Browse" button to select the image you want to watermark.

3. **Apply Watermark**: Once the image is selected, the watermark will be automatically applied.

4. **View Result**: The watermarked image will be saved in the specified target directory.

5. **Quit**: Click the "Quit" button to exit the application.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

This project is developed by WLQ Innovations - Vlku Aleksa.