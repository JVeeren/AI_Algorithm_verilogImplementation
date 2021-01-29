#only numpy
import numpy as np

#initialize parameters 
gamma=0.75#discount factor
alpha=0.9 #learning rate

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
rewards=np.array([
    [0,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,1,0]
])
#maps indicies to locations
state_to_location= dict((state,location) for location,state in location_to_state.items())

#get route
def get_optimal_route(start_location,end_location):
    #copy reward matrix to new matrix
    reward_new=np.copy(rewards)
    #get the ending state corresponding to ending location as given
    ending_state =location_to_state[end_location]
    #with above info automatically set priority to given ending state to highest one
    reward_new[ending_state,ending_state]=999

    #q-learn algo

    #initialize q values
    Q=np.array(np.zeros([9,9]))
    #print(Q)
    #q learning process
    for i in range(1000):
        #pick up a state randomly
        current_state=np.random.randint(0,9)#python excludes upper bound
        #for traversing thru the neighbour locations in the maze
        playable_actions=[]
        #iterate thru new rewards in matrix and get actions>0
        for j in range(9):
            if reward_new[current_state,j]>0:
                playable_actions.append(j)
        
        #pick an action randomly from the list of playable actions leading us to the next state
       # print(playable_actions)
        next_state=np.random.choice(playable_actions)
        #compute the temporal difference
        #the actions here exactly refers to going to thee next state
        TD= reward_new[current_state,next_state]+gamma*Q[next_state,np.argmax(Q[next_state,])]-Q[current_state,next_state]
        #update Q value using bellman equation
        Q[current_state,next_state] +=alpha*TD
        
       #print(np.argmax(Q[next_state,]))


    #initialize the optimal route with stating location
    route=[start_location]
    #we dontknow about nexxt location yet, so initialzie the value of startinng location
    next_location=start_location
    #we dont know about the exact no. of iterations needed to reach to the fial locarion hence while loop will be a good choice 
    while(next_location!=end_location):
        #fetch the  starting state 
        starting_state=location_to_state[start_location]
        next_state=np.argmax(Q[starting_state,])
        #we got the index of the next state but we need the corresponding letter
        next_location=state_to_location[next_state]
        route.append(next_location)
        #update the starting locationn for the next iteration
        start_location=next_location
    print(Q) 
    return route

print(get_optimal_route('L9','L6'))
   
