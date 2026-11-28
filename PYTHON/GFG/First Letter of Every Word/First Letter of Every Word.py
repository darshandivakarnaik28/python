class Solution:
	def firstAlphabet(self, s):
		words=s.split()
		res=""
		for word in words:
		    res+=word[0]
		return res