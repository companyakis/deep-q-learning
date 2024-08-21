Gymnasium packages contain a list of environments to test our "Reinforcement Learning (RL)" algorithm.

We often want to customize the provided environment to see how an agent behaves in different environments.

It is also a great interest to create our custom environment and test our algorithm.

## Basic structure of Gymnasium environment

Each gymnasium environment contains 4 main functions:

1- reset() : Resets the environment to the initial state, required before calling step. Returns the first agent observation for an episode and information, i.e. metrics, debug info.

2- step() : Updates an environment with actions returning the next agent observation, the reward for taking that actions, if the environment has terminated or truncated due to the latest action and information from the environment about the step, i.e. metrics, debug info.

3- render() : Renders the environments to help visualise what the agent see, examples modes are “human”, “rgb_array”, “ansi” for text

4- close() : Closes the environment, important when external software is used, i.e. pygame for rendering, databases

![image](https://github.com/user-attachments/assets/45d14698-00c9-49da-ac6d-d265b068611b)
