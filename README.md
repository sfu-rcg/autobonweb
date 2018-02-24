# autobonweb

A cheap web interface for bon_csv2html. Ingests bonnie++ disk benchmark output, converts all units to milliseconds, and writes results to disk with appropriate filename.

# Requirements
  - bonnie++
  - Python >= 2.7
  - nginx or Apache with autoindex/DirectoryIndex enabled for viewing saved results (optional)

# Installation
  - clone repo
  - cd ~/autobonweb
  - edit autobonweb.conf
  - pip install --user -r requirements.txt
  - python run.py
 
# Release Notes

**v0.01**, 23-Feb-2018. BEGIN

