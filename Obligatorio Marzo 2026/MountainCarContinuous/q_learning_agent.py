import random
import numpy as np
import matplotlib.pyplot as plt


class QLearningAgent:

    def __init__(self):
        x_space = np.linspace(-1.2, 0.6, 100)
        vel_space = np.linspace(-0.07, 0.07, 100)
        self.x_space = x_space
        self.vel_space = vel_space

        self.actions = list(np.linspace(-1, 1, 18))

        self.Q = np.random.random((len(x_space) + 1, len(vel_space) + 1, len(self.actions)))

    def get_state(self, obs):

        x, vel = obs

        x_bin = np.digitize(x, self.x_space)
        vel_bin = np.digitize(vel, self.vel_space)

        return (x_bin, vel_bin)

    def get_sample_action(self):

        return random.choice(self.actions)

    def optimal_policy(self, state):

        action = self.actions[np.argmax(self.Q[state])]

        return action

    def next_action(self, obs, epsilon=1.0):

        state = self.get_state(obs)

        explore = np.random.binomial(1, epsilon)

        if explore:
            action = self.get_sample_action()
        else:
            action = self.optimal_policy(state)

        return action

    def train_agent(self, env, episodes=100000, epsilon=1.0, gamma=0.99, alpha=0.08):
        promedio = 0
        list_reward = []
        for episode in range(episodes):
            obs, _ = env.reset()
            done = False
            total_reward = 0
            steps = 0
            state = self.get_state(obs)
            while not done:
                steps += 1
                # Acción
                action = self.next_action(obs, epsilon)
                # Índice acción
                action_idx = self.actions.index(action)
                # Formato gym
                real_action = np.array([action])
                # Ejecutar acción
                obs, reward, done, truncated, _ = env.step(real_action)
                next_state = self.get_state(obs)
                # Actualización Q-learning
                self.Q[state][action_idx] = (
                    self.Q[state][action_idx]
                    + alpha * (
                        reward
                        + gamma * np.max(self.Q[next_state])
                        - self.Q[state][action_idx]
                    )
                )
                # Actualizar estado
                epsilon = epsilon * 0.9999
                state = next_state
                total_reward += reward
                if truncated:
                    break
            #print(
                #f'Episode {episode+1} | '
                #f'Reward: {total_reward:.2f} | '
                #f'Steps: {steps}'
            #)
            list_reward.append(total_reward)
            promedio += total_reward
        promedio = promedio/episode
        print(promedio)
        env.close()
        return list_reward

    def test_agent(self, env, episodes=10):
        for episode in range(episodes):
            obs, _ = env.reset()
            done = False
            total_reward = 0
            while not done:
                state = self.get_state(obs)
                action = self.optimal_policy(state)
                real_action = np.array([action])
                obs, reward, done, truncated, _ = env.step(real_action)
                total_reward += reward
                env.render()
                if truncated:
                    break
            print(
                f'Test Episode {episode+1} | '
                f'Reward: {total_reward:.2f}'
            )
        env.close()