    	    # State Space Search #

'''
Three water jugs  -> (j1,j2,j3)

Possible moves:
j1 ==>	j1 -> j2 , j1 -> j3
j2 ==>	j2 -> j3 , j2 -> j1
j3 ==>	j3 -> j1 , j3 -> j2

Capacity of three water jugs = ( 8, 5, 3)
							-> (c1,c2,c3)
'''

capacity = (8,5,3)
c1,c2,c3 = capacity[0],capacity[1],capacity[2]

#initial state - (8,0,0)
istate = (8,0,0)

#goal state - (4,1,3)
gstate = (4,1,3)

'''
 Function next states(s) that returns a list of successor states of a given state s
'''
explored ={}

def next_states(s):
	s1,s2,s3 = s[0],s[1],s[2]

	sstate=[] #successor state

	#Move from j1
	if(s1>0):
		#j1 -> j2
		if (s1+s2<=c2):
			state = (0,s1+s2,s3)
			if state!=s and state not in explored:
				sstate.append(state)
		else:
			state = (s1+s2-c2,c2,s3)
			if state!=s and state not in explored:
				sstate.append(state)
		
		#j1 -> j3
		if (s1+s3<=c3):
			state = (0,s2,s1+s3)
			if state!=s and state not in explored:
				sstate.append(state)
		else:
			state = (s1+s3-c3,s2,c3)
			if state!=s and state not in explored:
				sstate.append(state)
	

	#Move from j2
	if(s2>0):
		#j2 -> j3
		if(s2+s3<=c3):
			state = (s1,0,s2+s3)
			if state!=s and state not in explored:
				sstate.append(state)
		else:
			state = (s1,s2+s3-c3,c3)
			if state!=s and state not in explored:
				sstate.append(state)
		
		#j2 -> j1
		if(s1+s2<=c1):
			state = (s1+s2,0,s3)
			if state!=s and state not in explored:
				sstate.append(state)
		else:
			state = (c1,s1+s2-c1,s3)
			if state!=s and state not in explored:
				sstate.append(state)
	

	#Move from j3
	if(s3>0):
		#j3 -> j1
		if(s1+s3<=c1):
			state = (s1+s3,s2,0)
			if state!=s and state not in explored:
				sstate.append(state)
		else:
			state = (c1,s2,s1+s3-c1)
			if state!=s and state not in explored:
				sstate.append(state)

		#j3 -> j2
		if(s2+s3<=c2):
			state = (s1,s2+s3,0)
			if state!=s and state not in explored:
				sstate.append(state)
		else:
			state = (s1,c2,s2+s3-c2)
			if state!=s and state not in explored:
				sstate.append(state)

	#explored[s]=sstate
	return sstate


ppaths=[] #Possible paths
def path_finder(path):
	parent = path[len(path)-1]
	if parent==gstate:
		ppaths.append(path)
		if(len(explored[parent])==0):
			return
	for s in explored[parent]:
		path_finder(path+[s]) 
 


def sort():
	for path in range(0,len(ppaths)-1):
			if len(ppaths[path]) > len(ppaths[path+1]):
				ppaths[path+1],ppaths[path]=ppaths[path],ppaths[path+1]


NumOfStates = 0

def BFS(istate):

	global NumOfStates

	#Queue as frontier that stores the discovered states yet be explored
	q=[]
	q.append(istate)
	while(len(q)!=0):
	#pop out the state yet to be visited from q
		s = q.pop(0)

		#Mark it explored
		explored[s]=next_states(s)

		#Add next states of s to q that are not explored
		for ns in explored[s]: #ns - next state of s
			if ns not in explored:
				NumOfStates+=1
				q.append(ns)



def main():
	BFS(istate)

	print("  State   :\t\tNext states")
	for s in explored:
		print(s,":",explored[s])

	path_finder([istate])	
	print("\nPossible Paths to reach goal state :")
	for path in ppaths:
		print(path)

	sort()
	print("\nOptimal Path to reach Goal state \n:",ppaths[0])

	print("\nTotal number of states explored :",NumOfStates)


if __name__ == "__main__":
	main()	
