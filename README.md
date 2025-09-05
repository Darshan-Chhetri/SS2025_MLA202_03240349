SS2025_MLA202_03240349
Darshan Chhetri

The task was about setting up a vertual environment specifically, catrpole and frozenlake. And i also learned to implement agent-environment looping 
For frozenlake, a 1000 episode was initiated in order to check the performance of the agent which lead me to the result of the average and total rewards over the episodes. 

Q1 What type of space is the action space? How many actions are there?
Action space is the set of all possible actions that an agent can take in a given environment. There are two possible actions in cartpole environment 0=push cart to the left, 1=push cart to the right

Q2 What type of space is the observation space? 
The observation space is the information the agent receives at each stepmeaning, it contains 4 continuous values, the cart position (how far the cart is from the center of the track), cart velocity (how fast the cart is moving), pole angle (how tilted the pole is from vertical), pole angular velocity (how fast the pole is falling or rising) 

Q3 What does the reward represent?
The reward is +1 for every step that the pole remains balanced. Once the pole falls or the cart moves out of bounds, the episode ends.


![image alt](https://github.com/Darshan-Chhetri/SS2025_MLA202_03240349/blob/master/frozenlake_avg_and_total_reward.png?raw=true)

The challenges i faced while doing this task was that there was some issue with looping and slight problems with indentation, however these issues with quickly and properly dealt with.

My key takeaway from this is that, gymnasium is a standard toolkit for comparing and developing RL algorithms, the agent-environment looping becomes easier once the concept becomes clear and the random agent is not that effecient. 
