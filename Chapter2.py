import random

class Environment:
    def __init__(self):
        
        '''
        initialize the number of steps
        '''
        
        self.num_steps_remaining = 10

    def get_observation(self):
        return [0.0, 0.0, 0.0]
    
    def get_action(self):
        
        '''
        allows the agent to query the list of 
        actions that can be executed.
        Only two actions available in any state.
        '''
        
        return [0, 1]
    
    def is_done(self):
        
        '''
        checks the number of steps we have 
        remaining. We cannot go over 10.
        '''
        
        return self.num_steps_remaining == 0
    
    def action(self, action):
        
        '''
        handles the actions for the agent
        and returns the reward. The reward 
        is random and action is discarded.
        returns reward value for a step.
        '''
        
        if self.is_done():
            raise Exception("Game is over")
        
        self.num_steps_remaining -= 1
        return random.random()
    
class Agent:
    def __init__(self):
        self.reward = 0.0
    
    def step(self, env):
        #getting the observation is of no use here
        #our agent is dumb and doesn't observe the environment.
        obs = env.get_observation()
        actions = env.get_action() 
        reward = env.action(random.choice(actions))
        self.reward += reward
        
if __name__ == "__main__":
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)
    
    print(agent.reward)
        