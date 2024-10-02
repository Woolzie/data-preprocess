import json

def convert_text_to_dict(text):
    # Split the text into lines
    lines = text.strip().split('\n')
    
    # Initialize the dictionary to hold the structured data
    result = {}
    current_dict = result
    
    # Iterate through each line
    for line in lines:
        # Determine the heading size by counting the '#' characters
        if line.startswith('#'):
            heading_size = line.count('#')
            heading_text = line[heading_size:].strip()  # Get the heading text
            
            # Create a new dictionary for this heading if it doesn't exist
            if heading_size not in current_dict:
                current_dict[heading_size] = {}
            
            # Set the current dictionary to the new heading's dictionary
            current_dict = current_dict[heading_size]
            
            # Add the heading text as a key with an empty dictionary as its value
            if heading_text not in current_dict:
                current_dict[heading_text] = {}
        else:
            # If it's not a heading, add it to the innermost dictionary
            if isinstance(current_dict, dict):
                if 'content' not in current_dict:
                    current_dict['content'] = []
                current_dict['content'].append(line.strip())

    return result

# Example usage
text_input = """
# Heading 1
This is some content under heading 1.

## Heading 2
This is some content under heading 2.

### Heading 3
This is some content under heading 3.
More details about heading 3.

## Another Heading 2
Content under another H2.
"""

# Convert the text to dictionary format
structured_data = convert_text_to_dict(text_input)

# Print the resulting structured data as JSON
print(json.dumps(structured_data, indent=4))
