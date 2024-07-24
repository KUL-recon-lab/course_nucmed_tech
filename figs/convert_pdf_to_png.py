import os
import subprocess


def convert_pdf_to_png(directory, resolution=300):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            # Get the full path of the PDF file
            pdf_path = os.path.join(directory, filename)
            # Create the output PNG file path
            png_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.png")
            # Call the magick convert command with specified resolution
            subprocess.run(
                ["magick", "-density", str(resolution), pdf_path, png_path],
                check=True,
            )
            print(
                f"Converted {pdf_path} to {png_path} with resolution {resolution} DPI"
            )


if __name__ == "__main__":
    # Set the directory containing PDF files
    directory = "."
    # Set the desired resolution (e.g., 300 DPI)
    resolution = 300
    convert_pdf_to_png(directory, resolution)
