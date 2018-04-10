"""Some simple utils for gild"""

import glob
import os.path
import sys

if False:
	from typing import List

def is_gild_root(path):
	# type: (str) -> bool
	"""Checks if the given path is a valid gild root"""
	urls = glob.glob(os.path.join(path,"*","*.url"))
	return len(urls) > 0

def get_gild_root():
	# type: () -> str
	"""Returns the gild root or None if none could be found."""
	root = os.getcwd()
	while True:
		if is_gild_root(root): return root;
		last_root = root
		root = os.path.dirname(root)
		if root == last_root: sys.exit("No gild folder structure found.")
	return None

def find_component_base(component):
	# type: (str) -> str
	"""Returns the base directory of the given component or exits the program"""
	root = os.getcwd()
	while True:
		base = os.path.join(root, component)
		if os.path.isdir(base): break
		last_root = root
		root = os.path.dirname(root)
		if root == last_root: sys.exit("No gild folder structure found.")
	return base

def get_components():
	# type: () -> List[str]
	"""Returns the names all components."""
	root = get_gild_root()
	if root is None: sys.exit("No gild folder structure found.")
	# FIXME: Should probably return all names without the prefix (instead just the last pathname)
	return [os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(root, "*","*.url"))]

def get_repo_url(component_base):
	# type: (str) -> str
	"""Given the full path to a component, returns it repo URL"""
	return open(os.path.join(component_base, "repo.url")).readline().strip()
