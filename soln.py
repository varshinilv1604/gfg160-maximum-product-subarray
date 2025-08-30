class Solution:
	def maxProduct(self,arr):
	    prod=1
	    for i in range(len(arr)):
	        curr=1
	        for j in range(i,len(arr)):
	            curr*=arr[j]
	            if(curr>prod):
	                prod=curr
	    return prod