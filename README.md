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

This script is experimental and may not work with all keyboard layouts.

It is also known, that layout with shortcuts, fixed with this method may not work the same way in many programs. This depends on the way program checks for shortcuts, but all common system shortcuts, such as copy/paste should work properly. I'm still trying to find a way to fix it.

## What is an MSKLC file?

An MSKLC file is a file format used by the Microsoft Keyboard Layout Creator tool to define custom keyboard layouts. You can compile and test your custom layouts using the MSKLC tool.

Download the Microsoft Keyboard Layout Creator tool [here](https://www.microsoft.com/en-us/download/details.aspx?id=102134).

For further details about MSKLC, refer to [this guide](https://msklc-guide.github.io/).

## Extra: Configuring the CAPSLOCK Key to Function as BACKSPACE

While this is not directly related to `qwertyfier`, it is an essential step in the "layout fixing" process using MSKLC files.

If you want your CAPSLOCK key to act as BACKSPACE and eliminate its default behavior, follow these steps:

1. **Download the files from the BACKSPACE FIX folder** and replace the corresponding file in the Microsoft Keyboard Layout Creator (MSKLC) installation folder.
2. After making this change, you can build layouts using this modified version of the program as usual.

If you encounter any issues, ensure that you have installed MSKLC to `C:/MSKLC`. The file you need to replace will be located at `C:/MSKLC/inc/kbd.h`. Note that this program is very sensitive to spaces (see [this Stack Overflow discussion](https://stackoverflow.com/a/60048017)).

For further customization options, check out the detailed information in [this guide](https://msklc-guide.github.io/).

## License

This project is licensed under the MIT License.

