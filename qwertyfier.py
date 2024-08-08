import sys
import re

# Define the predetermined list of VK codes
new_vks = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "OEM_MINUS", "OEM_PLUS", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "OEM_4", "OEM_6", "A", "S", "D", "F", "G", "H", "J", "K", "L", "OEM_1",
    "OEM_7", "OEM_3", "OEM_5", "Z", "X", "C", "V", "B", "N", "M", "OEM_COMMA",
    "OEM_PERIOD", "OEM_2", "SPACE", "OEM_102", "DECIMAL"
]

input_file = sys.argv[1]
output_file = input_file.replace('.klc', '_Fixed.klc')

def read_file_with_encoding(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines(), 'utf-8'
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='utf-16') as f:
            return f.readlines(), 'utf-16'

lines, encoding = read_file_with_encoding(input_file)
in_layout_section = False
vk_index = 0

with open(output_file, 'w', encoding=encoding) as outfile:
    for line in lines:
        if line.strip() == "LAYOUT":
            in_layout_section = True
            continue
        
        if in_layout_section:
            if line.startswith("02"):
                match = re.match(r'(\S+)\s+(\S+)(.*)', line)
                if match and vk_index < len(new_vks):
                    new_line = f"{match.group(1)}\t{new_vks[vk_index]}{match.group(3)}"
                    vk_index += 1
                else:
                    new_line = line
            else:
                new_line = line
        else:
            new_line = line
        
        outfile.write(new_line)

print(f"Processing completed. Output file: {output_file}")
