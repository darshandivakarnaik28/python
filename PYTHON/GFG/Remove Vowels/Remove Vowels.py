class Solution:
	def removeVowels(self, s):
	    res=""
		vowels=['a','e','i','o','u']
		for ch in s:
		    if ch not in vowels:
		        res+=ch
		return res