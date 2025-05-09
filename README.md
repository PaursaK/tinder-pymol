# tinder-pymol
simple script that aligns protein structures and allows you to quickly select ones to keep and ones to discard in PyMol.

<!-- # create a Tinder-like app for molecules comparison in PyMol

#implement it via multi-threading 

#use pymol api commands like cmd.load, cmd.show, cmd.align, etc.

#create a discard (not liked) list and a liked list

#save both in a designated directory 

#get familiar with argparse library to handle command line arguments 

# I imagine the program will flow like this:

    ## PREREQUISITES ##
    # 1. Import necessary libraries related to this program (e.g., pymol, argparse, threading)
    # 2. Directory containing the proteins to be compared + target protein

#you run the program either by using the cmd.run python script or you can run it directly from the command line
          #in both cases the program needs 2 arguments:
          # 1. Directory containing the proteins to be compared (pdb files)
          # 2. Target protein to be compared (pdb file)

# Next you load the target protein and then load all the proteins in the directory
# Then you align the target protein with each of the proteins in the directory
# Then you show the proteins in a nice way (e.g., cartoon, sticks, etc.)
# Then one by one you the proteins in the compare directory and ask the user if they like it or not (swipe left (left arrow) for discard, swipe right (right arrow) for like)
# If the user likes the protein, it is added to the liked list, otherwise it is added to the discard list
# finally, you save both lists in a designated directory (e.g. discarded and matches)
    # These two directories will be in a output directory that is created in the same directory as current working directory -->