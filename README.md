# EAN-13 Code Generator with Tkinter


## Overview

This Python application generates and displays EAN-13 codes using the Tkinter GUI library. EAN-13 codes are widely used for product identification and can be scanned by barcode readers.


>**Disclaimer:**
This is a tool for generating fictitious EAN-13 codes for testing. It's important to note that fictitious codes may not behave exactly like real-world codes in all scenarios. Fictitious means that the EAN-13 code has not been assigned to a company or product, but it adheres to the specific algorithm for its generation.


## Features
### 1. EAN-13 Code Generation
The application can generate random EAN-13 codes, adhering to the standard format. The generated codes consist of 12 random digits followed by a calculated check digit.

### 2. Code Display
The Tkinter window displays 10 generated EAN-13 codes in a LabelFrame. The codes are updated each time the "Generate New Codes" button is pressed.

### 3. Code Copying
The user can easily copy all displayed EAN-13 codes to the clipboard by clicking the "Copy Codes" button. This facilitates seamless integration with other applications or data storage.

### 4. User Interaction
The application provides a user-friendly interface with three main buttons: "Copy Codes," "Generate New Codes," and "Exit." These buttons enable users to interact with the application efficiently.

### 5. GitHub Integration
The footer of the application includes a clickable image linked to the project's GitHub repository. Users can easily access and explore the codebase by clicking on the image.


## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/loginLayer/ean13-code-gen-tkinter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ean13-code-gen-tkinter
    ```

3. Run the application:
    ```bash
    python ean13_gen_tk.py
    ```


## Usage
1. Launch the application using the provided installation instructions.
2. The window displays 10 randomly generated EAN-13 codes.
3. Click "Copy Codes" to copy all codes to the clipboard.
4. Click "Generate New Codes" to refresh and display 10 new codes.
5. Use the "Exit" button to close the application.


## Dependencies
* Python 3.x
* Tkinter library


## Contributing
Feel free to contribute by opening issues or submitting pull requests.


## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE.md file for details.


## Acknowledgments
Special thanks to the GitHub community for contributions and feedback.







