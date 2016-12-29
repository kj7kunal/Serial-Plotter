Plotter for real time serial data

Arduino is used to send preformatted serial data, each line of which contains delimiter separated real values for separate plots, and ending with a newline character.

PySerial is used to acquire the serial data, while matplotlib for python is used to plot the data in real time. 

Currently, only one plot can be generated at a time.

Future additions:
Multiple real time plots.
Fix bugs if any.
Add serial input feature.
Possibly integrate everything using a pyQt interface.