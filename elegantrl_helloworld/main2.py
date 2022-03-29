import time
import gym
import numpy as np

if __name__ == '__main__':
    # env = gym.make('ALE/Asteroids-v5', render_mode='human')
    # BreakoutNoFrameskip-v4
    # ALE/Asteroids-v5
    env = gym.make('ALE/Asteroids-v5', render_mode='human', obs_type='grayscale')
    print("Observation Space: ", env.observation_space)
    print("Action Space       ", env.action_space)

    obs = env.reset()

    for i in range(2000):
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        if done:
            break
        else:
            print(obs)
        pass
        time.sleep(0.01)
    env.close()
