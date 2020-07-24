import webbrowser, sys, pyperclip

if len(sys.argv) > 1:  # If the address is given as arguments
    address = ' '.join(sys.argv[1:])
else:  # get it from clipboard
    address = pyperclip.paste()

webbrowser.open('www.google.com/maps/place/' + address)
