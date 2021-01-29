#only numpy
import largestnum as t1
import random
import add as add3
import mult as mult3
import sub as sub3
import div as div3
import time

#initialize parameters 
gamma=0.75#discount factor
alpha=0.9#learning rate




#define states
location_to_state={

    'L1':0,
    'L2':1,
    'L3':2,
    'L4':3,
    'L5':4,
    'L6':5,
    'L7':6,
    'L8':7,
    'L9':8

}
	#define actions
actions=[0,1,2,3,4,5,6,7,8]
	#define rewards


rewards=[
    [0,1,0,0,0,0,0,0,0],
    [1,0,1,0,1,0,0,0,0],
    [0,1,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0],
    [0,0,0,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,1,0]
]



#maps indicies to locations
state_to_location= dict((state,location) for location,state in location_to_state.items())

#get route
def get_optimal_route(start_location,end_location):
    #copy reward matrix to new matrix
    reward_new=list(rewards)
    #get the ending state corresponding to ending location as given
    ending_state =location_to_state[end_location]
    #with above info automatically set priority to given ending state to highest one
    reward_new[ending_state][ending_state]=999

    #q-learn algo

    #initialize q values
    Q=[
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    print(Q) 
    #q learning process
    for i in range(1000):
        print(i)
        #pick up a state randomly
        current_state=random.randrange(0,9)#python excludes upper bound
        #for traversing thru the neighbour locations in the maze
        playable_actions=[]
        #iterate thru new rewards in matrix and get actions>0
        for j in range(9):
            if reward_new[current_state][j] > 0:
                playable_actions.append(j)
        
        #pick an action randomly from the list of playable actions leading us to the next state
        pick=random.randrange(0,len(playable_actions))
        next_state=playable_actions[pick]
        #compute the temporal difference
        #the actions here exactly refers to going to thee next state
        #TD = reward_new[current_state][next_state]+gamma*Q[next_state][t1.largest(Q[next_state])]-Q[current_state][next_state]
        #TD =sub3.sub(add3.sum(reward_new[current_state][next_state],int(mult3.mult(int(100*gamma),Q[next_state][t1.largest(Q[next_state])])/100)),Q[current_state][next_state])
        #m=
        p=int(mult3.mult(int(100*gamma),Q[next_state][t1.largest(Q[next_state])])/100)
        s=add3.sum(p,reward_new[current_state][next_state])
        TD=add3.sum(s,-Q[current_state][next_state])
        #print(p)
        #print(s)
        #print(TD)

        #update Q value using bellman equation
        #Q[current_state][next_state] +=alpha*TD
        t=int(mult3.mult(int(alpha*100),TD)/100)
        Q[current_state][next_state]=add3.sum(Q[current_state][next_state],t)
        #print(t)
        #print(Q[current_state][next_state])
        #b=Q[current_state][next_state] 
        #v=int(alpha*100)
        #t=int(mult3.mult(v,TD)/100)
        #b=add3.sum(b,t)
    print(Q)
    #initialize the optimal route with stating location
    route=[start_location]
    #we dontknow about nexxt location yet, so initialzie the value of startinng location
    next_location=start_location
    #we dont know about the exact no. of iterations needed to reach to the fial locarion hence while loop will be a good choice 
    while(next_location!=end_location):
        #fetch the  starting state 
        starting_state=location_to_state[start_location]
        next_state=t1.largest(Q[starting_state])
        #we got the index of the next state but we need the corresponding letter
        next_location=state_to_location[next_state]
        route.append(next_location)
        #update the starting locationn for the next iteration
        start_location=next_location
    return route

print(get_optimal_route('L9','L6'))    
