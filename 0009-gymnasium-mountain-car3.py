import matplotlib.pyplot as plt
import gymnasium as gym

env = gym.make('MountainCar', render_mode = 'rgb_array')

initial_state, _ = env.reset()


def render():
    state_image = env.render()
    plt.imshow(state_image)
    plt.show()

  
render()
