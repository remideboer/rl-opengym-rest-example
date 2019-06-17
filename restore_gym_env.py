import json
import jsonpickle
import gym

file = open("copy.json", "r")
json = file.read()
print(json)
json_decoded = jsonpickle.decode(json)
print(json_decoded)

env = gym.make('CartPole-v0')
env = json_decoded

for i in range(100):
    env.render()
    env.step(env.action_space.sample()) # take a random action

file.close()
