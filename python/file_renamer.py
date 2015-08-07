#File Renamer
#Written for linux
# I think i worked out most of the bugs, but who the hell knows, its 3:23 am...

import os;
import shutil;


directory = raw_input( 'Please insert directory name: ' ) # User sets source directory
new_dir = raw_input('Would you like to move file after rename, Yes or no? ' ) # Option to move to new directory after rename.

# runs ls -a in the directory set above, greps for certain file extensions and writes them to rename.txt
search_dir = [os.system("ls -a " + directory + " | grep '.mkv\|.mp4\|.avi' > rename.txt")] # Searches for common video file extensions.

# Handles move after rename choice
if new_dir.lower() in {"y", "yes"}:
	mv_dir = raw_input('Please enter directory to move after rename: ' )
elif new_dir.lower() in {"n", "no"}:
	print 'Your files will not be moved after rename.'
else:
	print "You didnt choose a valid option"
	os.system("rm rename.txt")
	exit()

# Renaming Loop
with open('rename.txt') as f:
	for line in f:
		if new_dir.lower() in {'y', 'yes'}:
			rename = raw_input('Would you like to rename: ' + line + 'Yes or No? ')
			if rename.lower() in {'y', 'yes'}:
				old_name = directory + '/' + line.rstrip('\n')
				user_name = raw_input('Enter the new file name: ')
				new_name = mv_dir + '/' + user_name
				shutil.move(old_name, new_name)
				print old_name + ' moved to ' + new_name
			elif rename.lower() in {'n', 'no'}:
				print 'Skipping ' + line
			else:
				os.system("rm rename.txt")
				break
		elif new_dir.lower() in {'n', 'no'}:
			rename = raw_input('Would you like to rename: ' + line + 'Yes or No? ')
			if rename.lower() in {'y', 'yes'}:
				old_name = directory + '/' + line.rstrip('\n')
				user_name = raw_input('Enter the new file name: ')
				new_name = directory + '/' + user_name
				shutil.move(old_name, new_name)
				print old_name + ' moved to ' + new_name
			elif rename.lower() in {'n', 'no'}:
				print 'Skipping ' + line
			else:
				os.system("rm rename.txt")
				break
		else:
			os.system("rm rename.txt")




