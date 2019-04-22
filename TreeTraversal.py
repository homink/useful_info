# Tree Traversal - horizonal, vertical

class Node():
	def __init__(self,data,left=None,right=None):
		self.val = data
		self.left = left
		self.right = right

def LevelOrder(root):
	if not root:
		return root
	queue = [root]
	res = []
	while queue:
		level = []
		nextqueue = []
		for node in queue:
			level.append(node.val)	
			if node.left:
				nextqueue.append(node.left)
			if node.right:
				nextqueue.append(node.right)
		queue = nextqueue
		res.append(level)
	return res

def LevelOrderBottom(root):
	if not root:
		return root
	queue = [root]
	res = []
	while queue:
		level = []
		nextqueue = []
		for node in queue:
			level.append(node.val)	
			if node.left:
				nextqueue.append(node.left)
			if node.right:
				nextqueue.append(node.right)
		queue = nextqueue
		res.insert(0,level)
	return res

def averageOfLevels(root):
	if not root:
		return root
	queue = [root]
	res = []
	while queue:
		avg = 0
		nextqueue = []
		for node in queue:
			avg = avg + node.val	
			if node.left:
				nextqueue.append(node.left)
			if node.right:
				nextqueue.append(node.right)
		res.append(avg*1.0/len(queue))
		queue = nextqueue
		
	return res
	
def zigzagLevelOrder(root):
	if not root:
		return root
	queue = [root]
	res = []
	z_count = 0
	while queue:
		level = []
		nextqueue = []
		for node in queue:
			if z_count==0:
				level.append(node.val)
			else:
				level.insert(0,node.val)

			if node.left:
				nextqueue.append(node.left)
			if node.right:
				nextqueue.append(node.right)
		queue = nextqueue
		res.append(level)
		if z_count == 0:
			z_count = 1
		elif z_count == 1:
			z_count = 0
	return res

def findMinMax(root,minimum,maximum,hd):
	if not root:
		return

	if hd<minimum[0]:
		minimum[0] = hd
	elif hd>maximum[0]:
		maximum[0] = hd

	findMinMax(root.left,minimum,maximum,hd-1)
	findMinMax(root.right,minimum,maximum,hd+1)

def printVerticalLine(root,line_no,hd,vl):
	if not root:
		return

	if line_no == hd:
		#print(root.val),
		vl.append(root.val)

	printVerticalLine(root.left,line_no,hd-1,vl)
	printVerticalLine(root.right,line_no,hd+1,vl)

def VerticalOrder(root):

	minimum, maximum, res = [0], [0], []
	findMinMax(root,minimum,maximum,0)

	for line_no in range(minimum[0],maximum[0]+1):
		vl = []
		printVerticalLine(root,line_no,0,vl)
		#print
		res.append(vl)
	return res

def getVerticalOrder(root, hd, table):
	if not root:
		return

	try:
		table[hd].append(root.val)
	except:
		table[hd] = [root.val]

	getVerticalOrder(root.left, hd-1,table)
	getVerticalOrder(root.right, hd+1,table)

def VerticalOrder_v2(root):
	table = dict()
	res = []
	getVerticalOrder(root, 0, table)

	for v in sorted(table):
		res.append(table[v])

	return res

t9 = Node(9)
t7 = Node(7,None,t9)
t8 = Node(8)
t6 = Node(6,None,t8)
t3 = Node(3,t6,t7)
t4 = Node(4)
t5 = Node(5)
t2 = Node(2,t4,t5)
t1 = Node(1,t2,t3)

print("LevelOrder")
print(LevelOrder(t1))
print("LevelOrderBottom")
print(LevelOrderBottom(t1))
print("averageOfLevels")
print(averageOfLevels(t1))
print("zigzagLevelOrder")
print(zigzagLevelOrder(t1))
print("VerticalOrder")
print(VerticalOrder(t1))
print("VerticalOrder v2")
print(VerticalOrder_v2(t1))
