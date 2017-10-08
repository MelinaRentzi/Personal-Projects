#! python3
# mapIt.py - Launches a map in the browser using an address from the clipboard

import webbrowser, pyperclip

# Get address from clipboard
address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' +address)