This project was developed and tested using Python 3.11.1, which is what you should also use.
Use Pyenv. Make sure you have Python 3.11.1 installed by your Pyenv.

The Flask container is built using a Bitnami Python base image which is also version 3.11.1.


----

Create the Pyenv Virtualenv and name it ve.flaskstack

     pyenv virtualenv 3.11.1 ve.flaskstack

If you have a modern shell and terminal you should see in your prompt that this VE is now active.
The .python-version file already in the project specifies this "ve.flaskstack" virtual environment,
so the names must match exactly. Pyenv then automatically activates this virtual environment
anywhere inside the directory tree of the .python-version file.
This is by far the best way to manage Python virtual environments and their automatic activation.

----

The following steps must be done when the ve.flaskstack VE is active.

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

TODO: The best wording to use is currently in the requirements.txt file itself.
The best/latest I have of these (requirements.txt)instructions is in THIS project,
in that specific file. Use that wording.

Install the project dependencies. Use the requirements file which has the versions pinned.
You do not want to use the un-pinned requirements file until you want to enter a planned upgrade/test phase.
Only the pinned requirements file will give you the exact code this project was developed and tested with.

Install the dependencies from the pinned requirements file

     pip install -r requirements.pinned.txt


