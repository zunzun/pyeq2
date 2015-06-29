These examples show how to run pyeq2 in parallel
on multiple computers working together as a cluster.


Step 1: Install and test dispy (DIStributed PYthon)

Instructions are at http://dispy.sourceforge.net/index.html

I personally used the command "pip install dispy".



Step 2: Install pyeq2 on remote cluster nodes

The dispy code uses a python file named dispynode.py
to run jobs on the remote cluster nodes.  The examples
will import pyeq2, so that must be available for import
on the remote nodes.  I personally used the command
"pip install pyeq2" (after installing scipy).



Step 3: Start the remote cluster nodes

On Debian, I personally use the command

"python /usr/local/bin/dispynode.py --clean".

DOCKER-ONLY NOTE: if you use docker containers to
provision the remote nodes, you will need to make
dispynode's TCP and UDP communication ports available.
I personally create containers with the command

"docker run -it -p 51348:51348 -p 51348:51348/udp debian"

which makes dispy's default TCP and UDP port available.



Step 4: Test remote cluster fitting of one equation

From a command prompt, run this command:

python Test_Single_Fit.py

If everything works, you should see the following:

Creating dispy JobCluster
[date time] - dispy - Storing fault recovery information in [filename]
Submitting job to the cluster
Waiting on job completion  and collecting results

Success! Results from job:
The equation pyeq2.Models_2D.Polynomial.Linear
yielded SSQABS of 0.00223880166667
with coefficients  [-0.07726667  1.15795   ]



Step 5: Test remote cluster fitting in parallel

From a command prompt, run this command:

python Test_Parallel_Fit.py

If everything works, you should see the following:

Creating dispy JobCluster
[date time] - dispy - Storing fault recovery information in [filename]
Submitting 20 jobs to the cluster
Waiting on jobs to complete  and collecting results

Success from job number 0

Success from job number 1

Success from job number 2

Success from job number 3

Success from job number 4

Success from job number 5

Success from job number 6

Success from job number 7

Success from job number 8

Success from job number 9

Success from job number 10

Success from job number 11

Success from job number 12

Success from job number 13

Success from job number 14

Success from job number 15

Success from job number 16

Success from job number 17

Success from job number 18

Success from job number 19

Done.



Step 6: Celebrate

You are now parallel cluster fitting with pyeq2 and dispy!



Look at the other pyeq2 examples for more information on
topics such as SMP parallel processing or "function finding".
