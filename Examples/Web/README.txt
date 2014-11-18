Welcome to FlaskFit, an example of creating a
a web-based curve and surface fitting tool with
Python Flask and the pyeq2 fitting library.


Step 1: Install flask, scipy and matplotlib

On Debian or Ubuntu Linux, you can use this command:

sudo apt-get install python-flask python-scipy python-matplotlib

On other operating systems, try the Canopy Express Free version:

https://store.enthought.com/

and then install Flask with:

easy_install Flask


Step 2: Run the FlaskFit example

From a command prompt run this command:

python FlaskFit.py

The command prompt should then display:

* Running on http://127.0.0.1:5000/

When you open this URL you should see a several graphs
that were dynamically fit to example data sets.

Use Control-C to exit the Flask development server.



Step 3: Celebrate

You are now curve and surface fitting data using Flask!



Future steps for you to try

A) Write a Flask form to submit user data for fitting

B) Present users with a menu selection of
available equations before submitting forms

C) Create scatterplots of the curve fitting errors
