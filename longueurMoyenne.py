import glob
import sys


def countLengthMoyenne():
	"""cette fontction prend le chemin relative du corpus et compte la longueur moyenne de textes contenus dans ce corpus"""
	doc = 0
	length = 0
	corpus = sys.argv[1] 
	for file in glob.glob("corpus/*/*"): 
		with open(file, 'r') as f:
			text = f.read()
			length+=len(text)
			doc+=1
	return length/doc
			
if __name__ == "__main__":
	print(countLengthMoyenne())