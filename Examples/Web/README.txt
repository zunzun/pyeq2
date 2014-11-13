Welcome to FlaskFit, an example of creating
a web-based curve fitting tool with Python Flask
and the pyeq2 curve and surface fitting library.


Step 1: Install flask, scipy and matplotlib

On Debian or Ubuntu Linux, you can use this command:

sudo apt-get install python-flask python-scipy python-matplotlib



Step 2: Run the FlaskFit example

From a command prompt run this command:

python FlaskFit.py

The command prompt should then display:

* Running on http://127.0.0.1:5000/

When you open this URL you should see a several graphs
that were dynamically fit to example data sets.

Use Control-C to exit the Flask development server.



Step 3: Celebrate

Congratulations, you are now fitting data using Flask!



Future steps for you to try

A) Write a Flask form to submit user data for fitting

B) Present users with a menu selection of
available equations before submitting forms

C) Create scatterplots of the curve fitting errors

D) Use matplotlib's 3D capability to display 3D
surface plots of fitted 3D equations

E) Look at the included pyeq2 source code examples
for details on displaying fit statistics, etc.


