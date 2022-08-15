from pathlib import Path, PureWindowsPath
import webbrowser

filename = Path("C:\\Users\\phils\\test.html")

windowpath = PureWindowsPath(filename)

print(windowpath)

# Opens file in web browser
webbrowser.open(filename.absolute().as_uri())
