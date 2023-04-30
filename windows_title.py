import pygetwindow as gw

# Get a list of all running window titles
titles = gw.getAllTitles()

# Print each title
for title in titles:
    print(title)