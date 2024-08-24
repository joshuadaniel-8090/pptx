import os
import subprocess

def convert_md_to_pptx(md_file, pptx_file, reference_pptx=None):
    """
    Convert a Markdown file to a PowerPoint presentation using Pandoc.

    Args:
    - md_file: The path to the input Markdown file.
    - pptx_file: The path to the output PowerPoint file.
    - reference_pptx: (Optional) Path to the reference PowerPoint file to use for styling.
    """
    try:
        # Base command to convert markdown to pptx using Pandoc
        command = [
            'pandoc',
            md_file,
            '-o',
            pptx_file
        ]

        # Add reference PowerPoint file if provided
        if reference_pptx:
            command.extend(['--reference-doc', reference_pptx])

        # Run the command
        subprocess.run(command, check=True)
        print(f"Successfully converted '{md_file}' to '{pptx_file}'.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the folder path
    input_folder_path = r'D:\Projects\pptx\md'  # Replace with your actual folder path
    output_folder_path = r'D:\Projects\pptx\ppt'  # Replace with your actual folder path
    reference_folder_path = r'D:\Projects\pptx\scripts'  # Replace with your actual folder path



    # Define the full paths for the Markdown and PowerPoint files
    md_file = os.path.join(input_folder_path, '1p.md')  # Path to your input Markdown file
    pptx_file = os.path.join(output_folder_path, '1p.pptx')  # Path to your output PowerPoint file
    reference_pptx = os.path.join(reference_folder_path, 'reference.pptx')  # Path to the reference PowerPoint file

    convert_md_to_pptx(md_file, pptx_file, reference_pptx)
