# Create the Cliff Walking environment

env = gym.make('CliffWalking')

num_actions = env.action_space.n # Up, Down, Right, Left

num_states = env.observation_space.n # 12 * 4

print("Number of actions:", num_actions)

print("Number of states:", num_states)
