import random
import numpy as np
import matplotlib.pyplot as plt


class DynaQAgent:

    def __init__(self):
        self.x_space = np.linspace(-1.2, 0.6, 40)
        self.vel_space = np.linspace(-0.07, 0.07, 40)

        self.actions = list(np.linspace(-1, 1, 8))

        self.Q = np.random.random(
            (len(self.x_space) + 1,
             len(self.vel_space) + 1,
             len(self.actions))
        )

        self.model = {}

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

        if np.random.random() < epsilon:
            return self.get_sample_action()

        return self.optimal_policy(state)

    def train_agent(
            self,
            env,
            episodes=100000,
            epsilon=1.0,
            gamma=0.99,
            alpha=0.08,
            planning_steps=20
    ):

        rewards = []
        promedio = 0

        for episode in range(episodes):

            obs, _ = env.reset()

            done = False
            total_reward = 0
            steps = 0

            state = self.get_state(obs)

            while not done:

                steps += 1

                action = self.next_action(obs, epsilon)
                action_idx = self.actions.index(action)

                real_action = np.array([action])

                obs, reward, done, truncated, _ = env.step(real_action)

                next_state = self.get_state(obs)

                self.Q[state][action_idx] += alpha * (
                    reward
                    + gamma * np.max(self.Q[next_state])
                    - self.Q[state][action_idx]
                )

                self.model[(state, action_idx)] = (
                    reward,
                    next_state
                )

                if len(self.model) > 0:

                    for _ in range(planning_steps):

                        (sim_state, sim_action) = random.choice(
                            list(self.model.keys())
                        )

                        sim_reward, sim_next_state = self.model[
                            (sim_state, sim_action)
                        ]

                        self.Q[sim_state][sim_action] += alpha * (
                            sim_reward
                            + gamma * np.max(self.Q[sim_next_state])
                            - self.Q[sim_state][sim_action]
                        )

                state = next_state
                total_reward += reward

                epsilon *= 0.9999

                if truncated:
                    break

            rewards.append(total_reward)
            promedio += total_reward

            # print(
            #     f'Episode {episode+1} | '
            #     f'Reward: {total_reward:.2f} | '
            #     f'Steps: {steps}'
            # )

        promedio /= episodes

        print("Promedio:", promedio)

        env.close()

        return rewards

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
                f"Test Episode {episode+1} | Reward: {total_reward:.2f}"
            )

        env.close()