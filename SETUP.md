The project was developed and tested using Python 3.11.1, which is what you should also use.
Use Pyenv. Make sure you have Python 3.11.1 installed by your Pyenv.


----

Created the Pyenv Virtualenv and name it ve.flaskstack

     pyenv virtualenv 3.11.1 ve.flaskstack

If you have a modern shell and terminal you should see in your prompt that this VE is now active.

----

Upgrade pip

    pip install --upgrade pip

----

Upgrade setuptools

     pip install --upgrade setuptools

----

Install/upgrade wheel

     pip install --upgrade wheel

----

TODO: Rewrite this section. I want the pinned file to be just requirements.txt.
Make this the default. Make a separate one that is unpinned and call it upgrade or planned upgrade.

Install the project dependencies. Use the requirements file which has the versions pinned.
You do not want to use the un-pinned requirements file until you want to enter a planned upgrade/test phase.
Only the pinned requirements file will give you the exact code this project was developed and tested with.

Install the dependencies from the pinned requirements file

     pip install -r requirements.pinned.txt


