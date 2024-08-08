# qwertyfier

`qwertyfier` is a Python script designed to modify Microsoft Keyboard Layout Creator (MSKLC) files. Its sole function is to replace the Virtual Key (VK) codes in a specified `.klc` file with a predefined set of VK codes from a QWERTY keyboard layout. 
This adjustment ensures that all CTRL shortcuts, such as `Ctrl+C` for copy and `Ctrl+V` for paste, work correctly, regardless of the custom keyboard layout in use.

## Usage

1. Place your `.klc` file in the same directory as the `qwertyfier.py` script.
2. Run the script from the command line:
   ```sh
   python qwertyfier.py <input_file.klc>
   ```
3. The script will generate a new file with `_Fixed` appended before the `.klc` extension.
4. You can now compile it using Microsoft Keyboard Layout Creator tool and test if it works.

## Warning

This script is experimental and may not work with all keyboard layouts (or any, as of the moment of writing this readme).

## What is an MSKLC file?

An MSKLC file is a file format used by the Microsoft Keyboard Layout Creator tool to define custom keyboard layouts. You can compile and test your custom layouts using the MSKLC tool.

Download the Microsoft Keyboard Layout Creator tool [here](https://www.microsoft.com/en-us/download/details.aspx?id=102134).

For further details about MSKLC, refer to [this guide](https://msklc-guide.github.io/).

## License

This project is licensed under the MIT License.

