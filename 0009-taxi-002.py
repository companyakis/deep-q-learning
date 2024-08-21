import gymnasium as gym

# create our environment

env = gym.make("Taxi-v3", render_mode = "ansi") # text-based mode suitable for displaying the environment in a text console

env.reset()

print(env.render())
