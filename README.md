# INSTAGRAM CAPTION EXTRACTER #

## Automatic caption extracter for Instagram post



This script will extract from your JSON files captions about your posts and create a directory for every post putting inside relative photos and the caption extracted.

## LIMITATIONS ##
At the moment the script will work only on Linux and only after having installed *pandas* module.
You can install *pandas* in a virtualenv or globally, this is your choice.
Follow the **Module Instructions** to install all the necessary and follow the **Script Instructions** to make it work.

## MODULE INSTRUCTIONS ##
If you have not pip installed, type:

- *sudo apt install python3-pip*

This will install it globally.

If you want to use the script in a *virtualenv* you have to install *virtualenv* first. To do that type:

- *pip3 install virtualenv*, if you have pip3 installed
- *sudo apt install virtualenv*, if you don't want to use pip3.

After that you can create a *virtualenv* typing:

- virtualenv -p python3 [choose_the_name_you_prefer]

and activate it typing

- cd the_name_you_chose && source bin/activate

Now, independently if you use *virtualenv* or not, to install all the module needed at the script to work type
  - *pip install -r requirements.txt*

## SCRIPT INSTRUCTIONS ##

Now that you have all the needed follow this simple instructions to make the script works.

- Put  all your 'media.json' file in 'media' directory.
- Put all your photos in 'photos' directory
- Launch the script invoking it typing python3 instagram_data_extracter.py

In the end you will find your posts, divided by creation date, in directories in the '*output*' directory