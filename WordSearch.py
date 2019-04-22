#Word Search

def dfs(board, i, j, word):

	if len(word)==0:
		return True

	if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
		return False

	tmp = board[i][j]
	board[i][j] = "#"
	res = dfs(board,i,j+1,word[1:]) or dfs(board,i,j-1,word[1:]) or \
		dfs(board,i+1,j,word[1:]) or dfs(board,i-1,j,word[1:])
	board[i][j]=tmp
	return res

def exist(board, word):
	if not board:
		return False

	for i in range(len(board)):
		for j in range(len(board[0])):
			if dfs(board,i,j,word):
				return True

	return False

board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCED"

print(exist(board,word))

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
res = []
for w in words:
	if exist(board,w):
		res.append(w)
print(res)
