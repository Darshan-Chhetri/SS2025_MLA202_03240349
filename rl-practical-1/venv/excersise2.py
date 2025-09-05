import gymnasium as gym

env = gym.make('FrozenLake-v1', render_mode='human')


num_episodes = 1000
rewards_per_episode = []

for episode in range(num_episodes):
    observation, info = env.reset()

    # Initialize variables to track the episode's progress
    terminated = False
    truncated = False
    total_reward = 0.0

    # The loop continues as long as the episode is not finished.
    while not terminated and not truncated:

        # choosing a completely random action from the action space.
        action = env.action_space.sample()
        
        next_observation, reward, terminated, truncated, info = env.step(action)

        # Update the tracking variables
        total_reward += reward
        observation = next_observation

        rewards_per_episode.append(total_reward)
    # After the loop, the episode is finished.
    print(f"\nEpisode finished! Total Reward: {total_reward}")
# Calculate and print the average and total reward over all episodes
average_reward = sum(rewards_per_episode) / num_episodes
print(f"Average Reward over {num_episodes} episodes: {average_reward:.4f}")

print(f'total reward after {num_episodes} episodes is {sum(rewards_per_episode)}')

# 5. CLOSE the environment
env.close()
