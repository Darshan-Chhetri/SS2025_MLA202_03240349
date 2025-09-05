import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

print(f"Action Space: {env.action_space}")
print(f"Observation Space: {env.observation_space}")

# --- THE MAIN LOOP ---

# 1. RESET the environment
# This function is called at the beginning of every new episode.
# It returns the initial observation and some optional info.
observation, info = env.reset()

# Initialize variables to track the episode's progress
terminated = False
truncated = False
total_reward = 0.0

# The loop continues as long as the episode is not finished.
while not terminated and not truncated:
    # This displays the current state in the popup window.
    env.render()
#Q1 What type of space is the action space? How many actions are there?
    #choosing a random action from the action space
    #action space is the set of all possible actions that an agent can take in a given environment.
    #there are two possible actions in cartpole environment
    #0=push cart to the left, 1=push cart to the right
    action = env.action_space.sample()
    print(f"Taking action: {action} (0:L, 1:R)")

#Q2 What type of space is the observation space? 
#The observation space is Box(4,), meaning it contains 4 continuous values:
#Cart position (how far the cart is from the center of the track)
#Cart velocity (how fast the cart is moving)
#Pole angle (how tilted the pole is from vertical)
#Pole angular velocity (how fast the pole is falling or rising)

    next_observation, reward, terminated, truncated, info = env.step(action)

#Q3 What does the reward represent?
    #the reward is +1 for every step that the pole remains balanced.
    #once the pole falls or the cart moves out of bounds, the episode ends.

    total_reward += reward
    observation = next_observation

    # Add a small delay to make the visualization easier to follow
    time.sleep(0.2)

# After the loop, the episode is finished.
print(f"\nEpisode finished! Total Reward: {total_reward}")

# 5. CLOSE the environment
env.close()