import os
import sys
import random

global v,h,b,x,tem,hi,vi,bi
v=[]
h=[]
b=[]
x=[]
hi=[]
vi=[]
bi=[]
f=[]
rf=[]
tem=[]
all=['1','2','3','4','5','6','7','8','9']
finish=0
test=1
for i in range(9):
	x.append([])
	v.append([])
	h.append([])
	b.append([])
	hi.append([])
	vi.append([])
	bi.append([])
	f.append([])
	rf.append([])
	tem.append([])
	for j in range(9):
		x[i].append(0)
		v[i].append([])
		h[i].append([])
		b[i].append([])
		hi[i].append([])
		vi[i].append([])
		bi[i].append([])
		f[i].append([])
		rf[i].append([])
		tem[i].append([])

print "Enter the values:"
for i in range(9):
	temp=raw_input("")
	t=temp.split()
	for j in range(9):
		x[i][j]=t[j]
		tem[i][j]=t[j]
#temp=x
#print x
for i in range(9):
	print x[i]
def logic(ch):
	print ch
	idle=0
	global test,tem,x,hi,vi,bi
	done='n'
	#x=tem
	for i in range(9):
		for j in range(9):
			x[i][j]=tem[i][j]
	for repeat in range(100):
		done='n'
		for i in range(9):
			for j in range(9):
				if x[i][j]=='0':
					h[i][j]=[]
					v[i][j]=[]
					b[i][j]=[]
					f[i][j]=[]
					rf[i][j]=[]
					hi[i][j]=[]
					vi[i][j]=[]
					bi[i][j]=[]
					#print "Reset"
					for k in range(9):
						if x[i][k]!='0':
							h[i][j].append(x[i][k])
						if x[k][j]!='0':
							v[i][j].append(x[k][j])
					if i<3 and j<3:
						for p in range(3):
							for q in range(3):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif i<3 and (j>=3 and j<6):
						for p in range(3):
							for q in range(3,6):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif i<3 and j>=6:
						for p in range(3):
							for q in range(6,9):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif (i>=3 and i<6) and j<3:
						for p in range(3,6):
							for q in range(3):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif (i>=3 and i<6) and (j>=3 and j<6):
						for p in range(3,6):
							for q in range(3,6):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif (i>=3 and i<6) and j>=6:
						for p in range(3,6):
							for q in range(6,9):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif i>=6 and j<3:
						for p in range(6,9):
							for q in range(3):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif i>=6 and (j>=3 and j<6):
						for p in range(6,9):
							for q in range(3,6):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
					elif i>=6 and j>=6:
						for p in range(6,9):
							for q in range(6,9):
								if x[p][q]!='0':
									b[i][j].append(x[p][q])
				else:
					h[i][j]=[]
					v[i][j]=[]
					b[i][j]=[]
					f[i][j]=[]
					rf[i][j]=[]
					hi[i][j]=[]
					vi[i][j]=[]
					bi[i][j]=[]
		for i in range(9):
			for j in range(9):
				if x[i][j]=='0' and done=='n':
					#print h[i][j]
					#print v[i][j]
					#print b[i][j]
					for p in range(9):
						for q in range(9):
							hi[p][q]=[]
							vi[p][q]=[]
							bi[p][q]=[]
							f[p][q]=[]
							rf[p][q]=[]
					for p in range(9):
						for q in range(9):
							if x[p][q]=='0':
								f[p][q]=h[p][q]
								[f[p][q].append(item) for item in v[p][q] if item not in f[p][q]]
								[f[p][q].append(item) for item in b[p][q] if item not in f[p][q]]
								for element in all:
									if element not in f[p][q]:
       										rf[p][q].append(element)
									if element not in h[p][q]:
       										hi[p][q].append(element)
									if element not in v[p][q]:
       										vi[p][q].append(element)
									if element not in b[p][q]:
       										bi[p][q].append(element)
					if len(rf[i][j])==1:
						x[i][j]=rf[i][j][0]
						print i,j,x[i][j]
						idle=0
						done='y'
					else:
						#print "checking",idle
						#idle=idle+1
						#if idle>200:
						if idle>2 and len(rf[i][j])==2:
							x[i][j]=rf[i][j][ch]
							print i,j,x[i][j],"########################### Random",rf[i][j]
							idle=0
						#if test==1:
						#	for i in range(9):
						#		for j in range(9):
						#			print "$$",i,j,rf[i][j]
						#test=0
							#print "++++++++",len(rf[i][j])
						if len(rf[i][j])>1:
							#print "rf=2"
							#for p in range(9):
							#	for q in range(9):
							#		tem[p][q]=x[p][q]
							#x[i][j]=rf[i][j][ch]		#Decision needs to be done here with feature of backtracking
							#print rf[i][j][0]
							c1=1
							c2=1
							c3=1
							#print "************"
							for y in range(len(rf[i][j])):
								c1=1
								'''if done=='y':
									c1=0
									continue'''
								for z in range(9):
									if (rf[i][j][y] in rf[i][z]) and z!=j:
										c1=0
								if c1==1 and done=='n':
									print "horizontal decision"
									x[i][j]=rf[i][j][y]
									print i,j,x[i][j],"###########################"
									idle=0
									done='y'
							for y in range(len(rf[i][j])):
								c2=1
								'''if done=='y':
									c2=0
									continue'''
								for z in range(9):
									if (rf[i][j][y] in rf[z][j]) and z!=i:
										c2=0
								if c2==1 and done=='n':
									print "vertical decision"
									x[i][j]=rf[i][j][y]
									print i,j,x[i][j],"###########################"
									idle=0
									done='y'
							for y in range(len(rf[i][j])):
								c3=1
								'''if done=='y':
									c3=0
									continue'''
								bc=0
								if i<3 and j<3:
									for p in range(3):
										for q in range(3):
											bc=0
											if p==i and q==j:
												bc=1
												#print "kjfweuf"
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif i<3 and (j>=3 and j<6):
									for p in range(3):
										for q in range(3,6):
											bc=0
											if p==i and q==j:
												bc=1
												#print "kjfweuf"
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif i<3 and j>=6:
									for p in range(3):
										for q in range(6,9):
											bc=0
											if p==i and q==j:
												#print "kjfweuf"
												bc=1
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif (i>=3 and i<6) and j<3:
									for p in range(3,6):
										for q in range(3):
											bc=0
											if p==i and q==j:
												#print "kjfweuf"
												bc=1
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif (i>=3 and i<6) and (j>=3 and j<6):
									for p in range(3,6):
										for q in range(3,6):
											bc=0
											if p==i and q==j:
												#print "kjfweuf"
												bc=1
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif (i>=3 and i<6) and j>=6:
									for p in range(3,6):
										for q in range(6,9):
											bc=0
											if p==i and q==j:
												#print "kjfweuf"
												bc=1
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif i>=6 and j<3:
									for p in range(6,9):
										for q in range(3):
											bc=0
											if p==i and q==j:
												#print "kjfweuf"
												bc=1
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif i>=6 and (j>=3 and j<6):
									for p in range(6,9):
										for q in range(3,6):
											bc=0
											if p==i and q==j:
												#print "kjfweuf"
												bc=1
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								elif i>=6 and j>=6:
									for p in range(6,9):
										for q in range(6,9):
											bc=0
											if p==i and q==j:
												bc=1
												#print "kjfweuf"
											if (rf[i][j][y] in rf[p][q]) and bc!=1:
												c3=0
								#print i,j,rf[i][j],"***************",rf[i][k]
								if c3==1 and done=='n':
									print "Box decision"
									x[i][j]=rf[i][j][y]
									print i,j,x[i][j],"###########################"
									idle=0
									done='y'
							#print "Hello"
		if done=='n':
			idle=idle+1


logic(0)
'''
logic(0)

for i in range(9):
	for j in range(9):
		if x[i][j]=='0':
			print "Wrong"
			logic(1)
			break

'''
for i in range(9):
	print x[i]
w=0
for i in range(9):
	for j in range(9):
		if x[i][j]=='0':
			print "Wrong"
			w=1
			break

if w==1:
	logic(1)

for i in range(9):
	for j in range(9):
		if x[i][j]=='0':
			print "Wrong"
			break
if w==1:
	for i in range(9):
		print x[i]


#print tem
'''
0 0 0 0 0 0 9 0 0
0 1 0 0 6 4 5 3 0
3 2 4 0 0 0 7 0 0
0 5 0 0 8 0 0 0 0
0 3 0 4 7 6 0 9 0
0 0 0 0 3 0 0 6 0
0 0 3 0 0 0 1 2 8
0 4 6 8 2 0 0 5 0
0 0 9 0 0 0 0 0 0
'''

'''
6 0 5 7 2 0 0 3 9
4 0 0 0 0 5 1 0 0
0 2 0 1 0 0 0 0 4
0 9 0 0 3 0 7 0 6
1 0 0 8 0 9 0 0 5
2 0 4 0 5 0 0 8 0
8 0 0 0 0 3 0 2 0
0 0 2 9 0 0 0 0 1
3 5 0 0 6 7 4 0 8
'''
'''				Hard
5 4 0 2 0 9 0 0 1
0 0 0 5 0 0 0 0 4
0 0 7 0 0 0 9 0 0
8 0 0 0 3 0 0 6 7
0 0 0 6 0 5 0 0 0
9 3 0 0 1 0 0 0 2
0 0 1 0 0 0 6 0 0
2 0 0 0 0 6 0 0 0
3 0 0 1 0 7 0 4 9
'''
'''				Hard
0 1 0 0 0 0 0 2 0
2 0 0 0 0 0 0 0 8
6 0 0 4 0 8 0 0 9
0 0 3 7 0 9 5 0 0
5 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 0
9 0 0 2 0 3 0 0 6
8 0 0 9 0 7 0 0 4
0 4 0 0 0 0 0 1 0
'''
'''
0 3 0 8 0 6 4 0 0
0 8 6 7 9 0 0 0 2
9 0 0 0 0 0 0 0 0
0 4 0 0 0 7 0 5 0
0 0 3 0 0 0 6 0 0
0 7 0 3 0 0 0 2 0
0 0 0 0 0 0 0 0 6
2 0 0 0 6 8 9 4 0
0 0 9 1 0 2 0 7 0
'''
'''				Hardest puzzle in the world
8 0 0 0 0 0 0 0 0
0 0 3 6 0 0 0 0 0
0 7 0 0 9 0 2 0 0
0 5 0 0 0 7 0 0 0
0 0 0 0 4 5 7 0 0
0 0 0 1 0 0 0 3 0
0 0 1 0 0 0 0 6 8
0 0 8 5 0 0 0 1 0
0 9 0 0 0 0 4 0 0
'''