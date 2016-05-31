You will need to install python and scipy to run this software.
see http://commonproblems.readthedocs.io/en/latest/

On Debian or Ubuntu Linux, you can use this command to get both:

sudo apt-get install python-scipy

On other operating systems, try the Canopy Express Free version:

https://store.enthought.com/

This repository is for Python 2, if you are using Python 3 please
use https://github.com/zunzun/pyeq3 instead.

See the Examples directory to get started.  All of the examples should
run by typing "python examplename.py" at a command prompt.  If your
copy of pyeq2 does not include the Examples directory, you can find
the examples at https://github.com/zunzun/pyeq2/tree/master/Examples


Prior to the invention of electronic calculation, only manual methods
were available, of course - meaning that creating mathematical models
from experimental data was done by hand.  Even Napier's invention of
logarithms did not help much in reducing the tediousness of this task.
Linear regression techniques worked, but how to then compare models?
And so the F-statistic was created for the purpose of model selection,
since graphing models and their confidence intervals was practically
out of the question.  Forward and backward regression techniques used
linear methods, requiring less calculation than nonlinear methods, but
limited the possible mathematical models to linear combinations
of functions.

With the advent of computerized calculations, nonlinear methods which
were impractical in the past could be automated and made practical.
However, the nonlinear fitting methods all required starting points
for their solvers - meaning in practice you had to have a good idea of
the final equation parameters to begin with!

If however a genetic or monte carlo algorithm searched error space for
initial parameters prior to running the nonlinear solvers, this problem
could be strongly mitigated.  This meant that instead of hit-or-miss
forward and backward regression, large numbers of known linear *and*
nonlinear equations could be fitted to an experimental data set, and
then ranked by a fit statistic such as AIC or SSQ errors.

Note that for an initial guesstimate of parameter values, not all data
need be used.  A reduced size data set with min, max, and (hopefully)
evenly spaced additional data points in between are used.  The total
number of data points required is the number of equation parameters
plus a few extra points.

Reducing the data set size used by the code's genetic algorithm greatly
reduces total processing time.  I tested many different methods before
choosing the one in the code, a genetic algorithm named
"Differential Evolution".


I hope you find this code useful, and to that end I have sprinkled
explanatory comments throughout the code.  If you have any questions
or comments, please e-mail me directly at zunzun@zunzun.com.

James R. Phillips
2548 Vera Cruz Drive
Birmingham, AL 35235 USA

email: zunzun@zunzun.com
