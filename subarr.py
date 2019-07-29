def arr(x,n):
	found=False
	lsum=0
	for i in range(n-1):
		lsum+=x[i]
		rsum=0
		for j in range(i+1,n):
			rsum+=x[j]
		if((lsum*(n-i-1))==(rsum*(i+1))):
			found=True
			print("yes")
	if found==False:
		print("no")
n=int(input())
l=list(map(int,input().split()))
arr(l,n)
