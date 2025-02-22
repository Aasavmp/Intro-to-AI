# Overview
This is a repository for the development of a Genetic Algorithm developed to play standard Open Gym games.

## Initial resources
Basics: Open AI Gym: https://gymnasium.farama.org/content/basic_usage/
Youtube Tutorial: https://www.youtube.com/watch?v=Mut_u40Sqz4

## Algorithm resources
https://openai.com/blog/openai-baselines-ppo/
https://stable-baselines3.readthedocs.io/en/master/
https://jonathan-hui.medium.com/rl-reinforcement-learning-algorithms-comparison-76df90f180cf

### Potential algorithms
PPO
A2C
DQN
DDPG
Genetic Algorithm
TRPO

## Dependencies
Python dependencies are listed in `requirements.txt`. To install them, run `pip install -r requirements.txt`.
Additionally, install PyTorch from https://pytorch.org/

## Custom environment
Follow the following steps to install the custom environment:
    conda create --name ga_env python=3.10.8
    pip install numpy pandas matplotlib
    pip install gym[box2d]
    pip install tensorflow