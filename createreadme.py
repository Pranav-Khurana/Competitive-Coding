#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path


HEADER = '''# Competive-Coding
This repository keeps a track of all the competitive problems solved by me.

![GitHub](https://img.shields.io/github/license/Pranav-Khurana/Competitive-Coding.svg?style=popout)
![GitHub top language](https://img.shields.io/github/languages/top/Pranav-Khurana/Competitive-Coding.svg?style=popout)
![GitHub last commit](https://img.shields.io/github/last-commit/Pranav-Khurana/Competitive-Coding.svg?style=popout)

'''

# GET THE LIST OF ALL THE CATEGORIES
def get_dirs ():
	dirs = [x for x in os.listdir ('.') if os.path.isdir (x) and '.git' not in x]
	return dirs

#GET PROBLEM STATEMENT
def get_problem (srcfile):
	with open (srcfile) as file:
		for line in file:
			line = line.strip ()
			if line.startswith ('//') or line.startswith ('#'):
				return line.lstrip ('//').lstrip('#').lstrip()

#FOR EACH DIRECTORY GET THE LINK OF PROGRAMS IN IT
def get_program (category):
	program = [x for x in os.listdir (category)]
	titles = []
	for filename in program:
		fullname = os.path.join (category, filename)
		if (os.path.isfile (fullname)) and (fullname.endswith ('.cpp') or fullname.endswith ('.c') or fullname.endswith ('.java') or fullname.endswith ('.py')):
			problem = get_problem(fullname)
			title = Path (fullname).stem
			# changing path separator for Windows paths
			# https://mail.python.org/pipermail/tutor/2011-July/084788.html
			titles.append ((title,problem,'https://github.com/Pranav-Khurana/Competitive-Coding/blob/master/' + fullname.replace (os.path.sep, '/')))
	return titles

def get_category_dict (category_names):
	categories = {}
	count = 0
	for category in category_names:
		titles = get_program (category)
		categories[category] = titles
		count += len (titles)
	return (count, categories)

#Now we have all the information, print it out in markdown format.
def print_file (category_names, count, categories):
	with open ('README.md', 'w') as file:
		file.write (HEADER)
		if count == 1:
			file.write ('>_{0} Problem solved till date_'.format(count))
		else:
			file.write ('>_{0} Problems solved till date_'.format(count))
		file.write ('''

---
## Categories
''')
		# print the list of categories with links
		for category in sorted (category_names):
			file.write ('* [{0}](#{1})\n'.format (category,category.lower()))

		if len (category_names) > 0:
			file.write ('''

---
''')

		# print the section for each category
		for category in sorted (category_names):
			file.write ('### {0}\n'.format (category))
			file.write ('\n')
			programs = categories[category]
			c = 1
			for (title, problem, solution) in sorted (programs):
				file.write ('**' + str(c) + ') {0}**  \n'.format (title))
				file.write ('  * [Problem Statement]({0})  \n'.format (problem))
				file.write ('  * [Solution]({0})  \n\n'.format (solution))
				c+=1
			file.write ('---\n')

		if len (category_names) > 0:
			file.write ('''
---
''')



#Create a README.md file with a nice index for using it directly from GitHub.
def create_README ():
	category_names = get_dirs ()
	count, categories = get_category_dict (category_names)
	print_file (category_names, count, categories)
	os.system('git add README.md')
if __name__ == '__main__':
	create_README ()
