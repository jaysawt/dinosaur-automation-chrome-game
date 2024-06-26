# 🦖 Dinosaur Automation Chrome Game 🕹️

This Python project automates the Chrome Dinosaur game using the PyAutoGUI library. It allows the dinosaur to jump over obstacles like cacti and flying dinosaurs during both day and night modes. The screenshot area is dynamically adjusted to adapt to changing game conditions.

## Requirements 📋

To run this project, you will need the following:

- Python 3.x
- PyAutoGUI: You can install it using pip: `pip install pyautogui`

## Usage 🚀

1. Open the Chrome Dinosaur game in your web browser. You can access the game by disconnecting from the internet or by visiting [https://elgoog.im/t-rex/](https://elgoog.im/t-rex/).
2. Start the Python script to automate the game.
3. The script will continuously monitor the game and make the dinosaur jump when it detects obstacles.

## Working 🛠️

- This code captures a screenshot of the specified region (to detect cacti and flying dinosaurs) defined by the left, top, width, and height coordinates using PyAutoGUI's screenshot function.
- After capturing the screenshot, PyAutoGUI uses the `locate()` function to identify predefined images that resemble the obstacles in the game. Once a match is found, the program triggers the dinosaur to jump in response.

## Adjusting Screenshot Area 📷

The game's screenshot area may change from time to time due to updates or screen resolution changes. You may need to manually adjust the screenshot coordinates in the `main.py` file to match your current game window. Look for the following lines of code:

```python
# Define the screenshot area (left, top, width, height)
pyautogui.screenshot(region=(left, top, width, height))```
