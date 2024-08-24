def convert_text_to_markdown(input_file, output_file):
    """
    Convert a plain text file into a markdown file.

    Args:
    - input_file: The path to the input text file.
    - output_file: The path to the output markdown file.
    """
    try:
        # Open the input text file for reading
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Open the output markdown file for writing
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    # Write each line from the text file to the markdown file
                    outfile.write(line)

        print(f"Conversion successful! Markdown file saved as '{output_file}'.")
    except Exception as e:
        print(f"An error occurred during the conversion: {e}")

if __name__ == "__main__":
    input_file = "extracted_content.txt"     # Path to your input text file
    output_file = "output.md"      # Path to your output markdown file

    convert_text_to_markdown(input_file, output_file)
