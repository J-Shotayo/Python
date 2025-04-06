def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

try:
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read from: ")

    # Try opening and reading the file
    with open(input_filename, 'r') as infile:
        original_content = infile.read()

    # Modify the content
    modified_content = modify_content(original_content)

    # Define the name of the output file
    output_filename = "modified_" + input_filename

    # Write the modified content to the new file
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"✅ Modified content written to '{output_filename}'")

except FileNotFoundError:
    print("❌ Error: The file was not found.")
except IOError:
    print("❌ Error: Could not read or write to the file.")
