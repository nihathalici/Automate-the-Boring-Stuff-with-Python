import pyperclip
text = pyperclip.paste()

# Separate line and add stars.
lines = text.split('/n')
for i in range(len(lines)):     # loop through all indexes in the "line" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list

text = '/n'.join(lines)

pyperclip.copy(text)

print(text)
