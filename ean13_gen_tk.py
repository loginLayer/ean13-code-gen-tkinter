import random
import tkinter as tk
import os


def generate_ean13():
    """
    Generates a random EAN-13 code.

    Returns:
        str: The generated EAN-13 code.
    """
    # Generate the first 12 random digits
    digits = [random.randint(0, 9) for _ in range(12)]

    # Calculate the check digit
    even_sum = sum(digits[-2::-2])
    odd_sum = sum(digits[-1::-2])
    total_sum = even_sum + odd_sum * 3
    check_digit = (10 - (total_sum % 10)) % 10

    # Add the check digit to the list
    digits.append(check_digit)

    # Convert the list of digits to an EAN-13 string
    ean13_code = ''.join(map(str, digits))

    return ean13_code


def copy_codes():
    """
    Copies EAN-13 codes to the clipboard.

    Copies all EAN-13 codes displayed on the window to the clipboard.

    Returns:
        None
    """
    # Get all EAN-13 codes from labels
    codes = [label.cget("text") for label in code_labels]

    # Join codes into a single string with newline characters
    copied_text = "\n".join(codes)

    # Copy the text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(copied_text)
    root.update()


def generate_new_codes():
    """
    Generates and displays 10 new EAN-13 codes.

    Clears existing labels and generates 10 new EAN-13 codes,
    displaying them on the Tkinter window.

    Returns:
        None
    """
    # Clear existing labels
    for label in code_labels:
        label.destroy()

    # Clear the list of code labels
    code_labels.clear()

    # Generate and display 10 new EAN-13 codes
    for i in range(10):
        generated_code = generate_ean13()

        # Create a Label for each EAN-13 code inside the LabelFrame
        label = tk.Label(label_frame, text=generated_code)

        # Place the Label inside the LabelFrame, adjusting y position
        label.grid(row=i, column=0)

        # Append label to the list
        code_labels.append(label)


# Get the current script's path
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# Build the full path for the image
image_path = os.path.join(script_directory, "img", "footer.png")

# Create Tkinter window
root = tk.Tk()
root.title("EAN-13 Codes")
root.geometry("300x550")
root.resizable(width=False, height=False)

# Create a LabelFrame with 50 pixels padding
label_frame = tk.LabelFrame(root, text="EAN-13 Codes", padx=30, pady=40)
label_frame.place(x=75, y=30)

# Display 10 EAN-13 codes in a Tkinter window using place
code_labels = []
for i in range(10):
    generated_code = generate_ean13()

    # Create a Label for each EAN-13 code inside the LabelFrame
    label = tk.Label(label_frame, text=generated_code)

    # Place the Label inside the LabelFrame, adjusting y position
    label.grid(row=i, column=0)

    # Append label to the list
    code_labels.append(label)


# Function to close the program
def close_program():
    """
    Closes the Tkinter program.

    Destroys the Tkinter root window, closing the program.

    Returns:
        None
    """
    root.destroy()


# Create a Button for copying codes
copy_button = tk.Button(root, text="Copy Codes", command=copy_codes, width=15)
copy_button.place(x=93, y=365)

# Create a Button for generating new codes
generate_button = tk.Button(root, text="Generate New Codes", command=generate_new_codes, width=18)
generate_button.place(x=82, y=405)

# Create a Button for closing the program
close_button = tk.Button(root, text="Exit", command=close_program, width=15, height=1)
close_button.place(x=93, y=445)

# Create a Canvas for the footer
footer_canvas = tk.Canvas(root, bg="black", height=60, width=300)
footer_canvas.place(x=0, y=490)

# Add the image to the Canvas
image = tk.PhotoImage(file=image_path)

# Create a link to open github.com when clicking on the image
def open_github(event):
    import webbrowser
    webbrowser.open("https://github.com/loginLayer/ean13-code-gen-tkinter")


# Add the image to the Canvas and bind mouse events
image_id = footer_canvas.create_image(0, 0, anchor=tk.NW, image=image)
footer_canvas.tag_bind(image_id, "<Button-1>", open_github)
footer_canvas.tag_bind(image_id, "<Enter>", lambda event: root.config(cursor="hand2"))
footer_canvas.tag_bind(image_id, "<Leave>", lambda event: root.config(cursor=""))

# Run the Tkinter main loop
root.mainloop()
