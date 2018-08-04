# RealTimeFileLogger


Real Time File logger or rtfilelogger for short, is a simple desktop application written in Python. The tool allows you to read text\log\non-binary files in real time. It also allows you to pause or resume reading files. The tool is cross-platform.

Due to my limited time, the tool has some bugs, but it works for the most part :)

![Simple file logger](https://github.com/minaandrawos/RealTimeFileLogger/blob/master/screenshot.png)

----
**How to run:**

 - Make sure you have Python 3, preferrably Python 3.6.
 - Clone this repository: `git clone https://github.com/minaandrawos/RealTimeFileLogger.git`.
 - Run `python rtfilelogger.py`, assuming that the `python` command invokes python3 in your terminal, otherwise the command is likely `python3`.
 - In Linux, you might need to run `sudo apt-get install python3-tk`.

That's it. The project does not use any third party packages. It relies on Tkinter for the UI, which in a lot of cases comes pre-loaded with Python. 

----
**How to use the tool?**

![rtfilelogger with some files running](https://github.com/minaandrawos/RealTimeFileLogger/blob/master/screenshotwithfiles.png)

The tool consists of only two buttons:

 1. *Add New File*: Opens a new file for monitoring. The file will open in a new tab.
 2. *Play/Pause*:  Pauses or resumes the read operation of the currently selected file.

----
Happy hacking!!
www.minaandrawos.com
