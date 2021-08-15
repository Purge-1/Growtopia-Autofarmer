# Growtopia-Autofarmer
A simple Growtopia autofarmer made with python

# Requirements
python -- https://python.org | pyautogui -- https://pypi.org/project/PyAutoGUI/ | tkinter -- https://pypi.org/project/tk-tools/

# Usage
Head to https://python.org and install the latest version of python.
Download the main.py file (green code button -> download zip)
Run the main.py file, once you run the file you should be able to see a GUI with some buttons.

What are the buttons for? 
POS 1 -> Used to set the first block position (where the first block is going to be placed)
POS 2 -> Used to set the second block position (where the second block is going to be placed)
Block Pos -> Used to locate the block in your inventory.
Fist Pos -> Used to locate the fist in your inventory.

To set the first block position, click the button labeled "POS 1" and hover over wherever you'd like to set the position to. 
To set the second block position, click the button labeled "POS 2" and hover over wherever you'd like to set the position to.
To set the block position, click the button labeled "Block Pos" and hover over the block you'd like to autofarm (make sure that the block is in your inventory)
To set the fist position, click the button labeled "Fist Pos" and hover over the fist.

# Notes
- Tested on Growtopia private servers and Growtopia it self
- Not tested on older versions of python
- Not tested on older versions of windows
- There's no key to stop the autofarmer, you may stop it by quickly moving your mouse to the side of your screen. (This will trigger PyAutoGUI fail-safe) If you'd like to disable this built-in feature and add your own key to stop the autofarmer, then uncomment the 6th line (pyautogui.FAILSAFE = False)
