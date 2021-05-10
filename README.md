# INSTAGRAM CAPTION EXTRACTER #

## Automatic caption extracter for Instagram post



This script will extract from your JSON files captions about your posts and create a directory for every post putting inside relative photos and the caption extracted.

## LIMITATIONS ##
At the moment the script will work only on Linux and only after having installed *pandas* module.
Follow the **Module Instructions** to install all the necessary and follow the **Script Instructions** to make it work.

## SCRIPT INSTRUCTIONS ##

To create the environment use the Dockerfile.
Once you have all the needed follow this simple instructions to make the script works.

- Put  all your 'media.json' file in 'media' directory.
- Put all your photos in 'photos' directory
- Use "docker run [image]" to run the script

In the end you will find your posts, divided by creation date, in directories in the '*output*' directory