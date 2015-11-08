This creates a curve-fitting specific
teaching tool with animated GIF files
using pyeq2 and matplotlib.  The purpose
is to visually  illustrate many commonly
encountered problems in curve fitting.

A large number of animation frames are
individually created, and this takes a
long time to complete.  Pay close attention
to how and where the 95% confidence intervals
change as the animations run. Let me know if
you have any questions by email to zunzun@zunzun.com
or by posting to the user group at the URL
https://groups.google.com/forum/#!forum/zunzun_dot_com


Step 1: Install matplotlib, imagemagick and gifsicle

On Debian or Ubuntu Linux, you can use this command:

sudo apt-get install imagemagick python-matplotlib gifsicle



Step 2: Run the CommonProblems generator

From a command prompt run this command:

python generateOutput.py

The generator will display its progress
as it runs, and will create both HTML
files and animated GIF files.



Step 3: View the animations

You can open the index.html file in a
browser to see the animations.  The animations
may appear to stutter or jerk until fully loaded
from the computer's hard disk drive into the browser.
