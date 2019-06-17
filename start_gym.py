import json
import jsonpickle
from pprint import pprint
from collections import deque
import csv
import copy
import gym

env = gym.make('CartPole-v0')
env.reset()
# pprint(vars(env))
# print(vars(env.observation_space))

file = open('state.csv', 'w')
file2 = open('copy.json', 'w')

writer = csv.writer(file, lineterminator='\n')

for i in range(50):
    # env.render()
    env.step(env.action_space.sample())  # take a random action
    # print(vars(env.observation_space.low))
    l = deque(env.env.state)
    l.appendleft(i)

    writer.writerow(tuple(l))
save_point = copy.deepcopy(env)
# dit gaat goed
file2.write(jsonpickle.encode(env))

env.close()
file.close()
file2.close()
