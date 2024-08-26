import gymnasium as gym

env = gym.make("MountainCar", render_mode = "rgb_array") # for visualization

# Get the initial state
initial_state, info = env.reset(seed = 42) # seed is for reproducibility

position = initial_state[0]

velocity = initial_state[1]

print(f"The position of the car along the x-axis is {position} (m)")

print(f"The velocity of the car is {velocity} (m/s)")

    # The position of the car along the x-axis is -0.4452087879180908 (m)
    # The velocity of the car is 0.0 (m/s)
