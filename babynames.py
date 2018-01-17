#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename,summary):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  #print 'extract names yo'
  
  file = open(filename,'rU')
  dict = {}
  for line in file:
    year = re.search(r'Popularity in (\d\d\d\d)',line)
    rank_name = re.findall(r'<td>(\w+)<\/td>',line)
    #print rank_name
    if year:
      #print 'Year is:',year.group(1)
      current_year=year.group(1)
    if rank_name:
      #print '\nRank =',rank_name[0],'\nBoy=',rank_name[1],'Girl=',rank_name[2]
      dict[rank_name[1]]=rank_name[0]
      dict[rank_name[2]]=rank_name[0]

#output operations
  if summary:
    #print 'summary flag----'
    #w = open(
    #print dict
    #print '\n\n\n*******LOOP********\n\n\n'
    #print '\n\n\nPRINTING',current_year,'FILE\n\n\n'
    #print filename
    outfile = open(filename+'.summary','w')
    outfile.write(current_year+'\n')
    for i in sorted(dict.items()):
      outfile.write(i[0]+' '+i[1]+'\n')
    outfile.close()
    #print for i in sorted(dict.items()):
      #print i[0],i[1]

  else:
    print current_year
    for i in sorted(dict.items()):
      print i[0],i[1]
  file.close()

  return dict


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  #import re
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  filename = args[0]
  if summary:
    #print 'summary = True, will come back to this'
    for i in args:
      extract_names(i,summary)
      #print 'args =',i
  else:
    #print 'summary = False, beginning program\n\n\n********************\n\n\nBEEP BOOP BEEP BOOP\n\n\n********************\n\n\n\n\n'
    extract_names(filename,summary)
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
