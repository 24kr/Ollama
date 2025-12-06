import ollama
import os
model = "llama3.2"

# Paths to input and output files

input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

# check if input file exists

if not os.path.exists(input_file):
    print(f"Input file {input_file} does not exist.")
    exit(1)

# Read the uncategorized grocery items from the input file

with open(input_file, 'r') as f:
    items = f.read().strip()

# Create a prompt for categorization
prompt = f"""
Your are an asssistant that categorizes and sorts grocery items into sections.

Here is a list of grocery items:

{items}

Please categorize and sort the items into sections. 
For each item, provide a brief description of the item and the section it belongs to. 
Format the output as follows:

Item: [item name]
Description: [description of the item]
Section: [section name]

"""
# send the prompt to the model and get the response

try:
    response = ollama.generate( model=model,prompt=prompt)
    generated_text = response.get("response", "")
    # print the generated text
    print("======== Categorized Grocery List ======== \n")
    print(generated_text)
 
    # Write the categorized grocery list to the output file
    with open(output_file, 'w') as f:
        f.write(generated_text.strip())

    print(f"Categorize  d grocery list written to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")

#delete model
