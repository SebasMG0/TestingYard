def longest_palindromic_substring(s:string):
	m= [[0]*len(s) for _ in range(len(s))]
	i, j= 0, len(s)-1

print(longest_palindromic_substring(s="baareconocerbb"))