import click
from binaryornot.check import is_binary
from pathlib import Path
from shutil import copyfile

@click.command()
@click.option('--path', help="Path of file to be put on gist")
def parse(path):
	'''
	Used to parse a file into html document
	'''
	if Path(path).is_file():
		if not is_binary(path):
			copyfile(path, path+".txt")
		else:
			click.echo("Files with only text format are allowed")
	else:
		click.echo("Mentioned file doesn't exist")
if __name__=='__main__':
	parse()