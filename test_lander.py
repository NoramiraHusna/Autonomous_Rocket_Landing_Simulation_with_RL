import gymnasium as gym

# Initialize the environment with the updated version 3 configuration
env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset()

# Run the simulation loop with random inputs
for _ in range(300):
    # 0: Do nothing, 1: Fire left engine, 2: Fire main engine, 3: Fire right engine
    action = env.action_space.sample() 
    
    # Apply the action to the simulation
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
print("Environment runs successfully!")