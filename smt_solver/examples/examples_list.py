import os

path = os.getcwd()
pl = path.split("\\",-1)

if(pl[-1]!="examples"):
	path += "\\examples\\"

class examples(object):
	def __init__(self):
		self.data = {}
		self.load_examples()
		
	def load_examples(self):
		get_dir = os.listdir(path)  
		for i in get_dir:          
			sub_dir = os.path.join(path,i)  
			if os.path.isdir(sub_dir):
					self.data[sub_dir] = list()
					self.data[sub_dir] = os.listdir(sub_dir)
			else:
				pass

	def all(self):
		ans = []
		for i in self.data:
			p = i.split("\\", -1)
			if(p[-1]=="__pycache__"): continue
			for j in self.data[i]:
				ans.append(".\\examples\\" + str(p[-1]) + "\\" + j)
		return ans

if(__name__=="__main__"):
	ex = examples()
	print(ex.all())