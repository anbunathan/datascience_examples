from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/q2ZOEFAaaI0?showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')

import numpy as np
import gym
import random
#Step 1: Create the environment
env = gym.make("Taxi-v2")
env.render()
#Step 2: Create the Q-table and initialize it
action_size = env.action_space.n
print("Action size ", action_size)

state_size = env.observation_space.n
print("State size ", state_size)

qtable = np.zeros((state_size, action_size))
print(qtable)

#Step 3: Create the hyperparameters

total_episodes = 50000        # Total episodes
total_test_episodes = 100     # Total test episodes
max_steps = 99                # Max steps per episode

learning_rate = 0.7           # Learning rate
gamma = 0.618                 # Discounting rate

# Exploration parameters
epsilon = 1.0                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability
decay_rate = 0.01             # Exponential decay rate for exploration prob

#Step 4: The Q learning algorithm
# 2 For life or until learning is stopped
for episode in range(total_episodes):
    # Reset the environment
    state = env.reset()
    step = 0
    done = False

    for step in range(max_steps):
        # 3. Choose an action a in the current world state (s)
        ## First we randomize a number
        exp_exp_tradeoff = random.uniform(0, 1)

        ## If this number > greater than epsilon --> exploitation (taking the biggest Q value for this state)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state, :])

        # Else doing a random choice --> exploration
        else:
            action = env.action_space.sample()

        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info = env.step(action)

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma *
                                                                         np.max(qtable[new_state, :]) - qtable[
                                                                             state, action])

        # Our new state is state
        state = new_state

        # If done : finish episode
        if done == True:
            break

    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

#Save and load qtable
with open("q_table.save", "wb") as f:
    np.save(f, qtable)

data = None
with open("q_table.save", "rb") as f:
    data = np.load(f)
data.shape

#Step 5: Use our Q-table to play Taxi !
env.reset()
rewards = []

for episode in range(total_test_episodes):
    print("Game start!!!")
    state = env.reset()
    step = 0
    done = False
    total_rewards = 0
    # print("****************************************************")
    # print("EPISODE ", episode)
    numberofsteps=0
    for step in range(max_steps):
        # UNCOMMENT IT IF YOU WANT TO SEE OUR AGENT PLAYING
        env.render()
        # Take the action (index) that have the maximum expected future reward given that state
        #action = np.argmax(qtable[state, :])
        action = np.argmax(data[state, :])

        new_state, reward, done, info = env.step(action)

        total_rewards += reward
        numberofsteps+=1
        if done:
            rewards.append(total_rewards)
            print ("Score", total_rewards)
            print("numberofsteps = ",numberofsteps)
            break
        state = new_state
env.close()
print("Score over time: " + str(sum(rewards) / total_test_episodes))