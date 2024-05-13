import sys
import re
import ppt
# Define the patterns for scenes and presentation attributes
scene_pattern = re.compile(r'^[A-Za-z0-9]+:$')
attribute_pattern = re.compile(r'^[a-z_ ]+ = .+$')

# Define the attributes for scenes and presentations with default values
scene_attributes = {
    "type": "default",
    "layout": "default",
    "title": "default",
    "subtitle": "default",
    "theme": "default",
    "color": "default",
    "background": "default"
}
presentation_attributes = {
    "type": "default",
    "layout": "default",
    "title": "default",
    "theme": "default"
}

# Read the input file from the command line argument
input_file = sys.argv[1]

# Process the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Initialize variables to store the current scene and presentation details
current_scene = None
presentation_details = {}

# Iterate over each line in the file
for line in lines:
    line = line.strip()
    if line.startswith("#") or line == '':
        continue  # Ignore comments and blank lines
    elif scene_pattern.match(line):
        current_scene = line[:-1]  # Remove the colon at the end
        presentation_details[current_scene] = scene_attributes.copy()
    elif attribute_pattern.match(line):
        value = line.split("=", 1)[1]
        key = line.split(" ")[1]
        value = value.strip('"')  # Remove any quotation marks around the value
        key = key.strip('"')
        if current_scene:
            if key in scene_attributes:
                value = value.strip('"')
                presentation_details[current_scene][key] = value
        else:
            if key in presentation_attributes:
                value = value.strip('"')
                presentation_attributes[key] = value


print("Presentation Details:", presentation_attributes)
print("Scenes:", presentation_details)

if presentation_attributes['type'] == ' slides':
    ppt.create_slides_presentation(presentation_attributes, presentation_details)
else:
    print("Unsupported presentation type.")