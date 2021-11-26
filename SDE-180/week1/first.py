
from collections import defaultdict as D
#! Day 1 problem 3(problem 1 is also same)
# arr=[7, 3, 4, 5, 5, 6, 2]
# n=len(arr)

# for i in range(n):
#     if arr[abs(arr[i])-1]>0:
#         arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
#     else:
#         print("duplicate : ",abs(arr[i]))
    
# for i in range(n):
#     if arr[i]>0: print("missing : ",i+1); break

#! Day 1 problem 2

# arr=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# n=len(arr)
# l=0; r=n-1
# k=0
# while k<=r:
#     if arr[k]==0:
#         arr[l],arr[k]=arr[k],arr[l]
#         l+=1; k+=1
#     elif arr[k]==2:
#         arr[r],arr[k]=arr[k],arr[r]
#         r-=1
#     else: k+=1
# print(arr)

#! Day 3 2nd problem
# def power(x,n):
#     if n==1: return 1
#     if n&1:
#         return pow(x,n-1)*x
#     else:
#         return pow(x*x,n>>1)

# print(power(2,4))

#! Day 4 4th problem

# arr=[15,-2,2,-8,1,7,10,23]
# dic={}; n=len(arr)
# cur=0; ma=0

# for i in range(n):
#     if arr[i]==0: ma=max(ma,1)
#     cur+=arr[i]
#     if cur==0: ma=max(ma,i+1)
#     if cur in dic:
#         ma=max(ma,i-dic[cur])
#     else:
#         dic[cur]=i
# print(ma)


#! Day 4 6th problem

# s="ABDEFGABEF"
# n=len(s)
# has=set(); ma=0; l=0

# for i in range(n):
#     if s[i] in has:
#         ma=max(ma,i-l)
#         while s[i] in has:
#             if s[l] in has: has.remove(s[l])
#             l+=1
#     has.add(s[i])
# print(ma)

#! Day 4 5th problem

# arr=[4, 2, 2, 6, 4]; m=6
# dic=D(bool); cur=0; c=0
# dic[0]=1
# for i in arr:
#     cur^=i
#     if dic[cur^m]:
#         c+=dic[cur^m]
#     dic[cur]+=1
#     print(dic)
# print(c)

