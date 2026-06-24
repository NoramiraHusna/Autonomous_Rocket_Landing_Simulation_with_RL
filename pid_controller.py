import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

def run_pid_controller():
    # Initialize environment with visual rendering
    env = gym.make("LunarLander-v3", render_mode="human")
    observation, info = env.reset()
    
    # Storage arrays for performance metrics evaluation
    altitudes = []
    vertical_velocities = []
    errors = []
    
    print("Running Classical PD Controller Baseline...")
    
    for step in range(600):
        # Extract variables from state vector
        pos_x = observation[0]
        pos_y = observation[1]
        vel_x = observation[2]
        vel_y = observation[3]
        angle = observation[4]
        angular_vel = observation[5]
        
        # Log data for metric tracking
        altitudes.append(pos_y)
        vertical_velocities.append(vel_y)
        errors.append(abs(pos_x) + abs(pos_y))
        
        # --- PD CONTROL LOGIC ---
        
        # 1. Main Engine Control (Vertical Axis)
        # Target descent velocity scales proportionally to altitude
        target_vel_y = -0.3 * (pos_y + 0.1) 
        vel_y_error = vel_y - target_vel_y
        
        # 2. Attitude Control (Horizontal Axis and Angle Alignment)
        # Target angle depends on horizontal positioning error
        target_angle = -0.5 * pos_x - 0.5 * vel_x
        angle_error = angle - target_angle
        
        # Compute tracking commands using proportional and derivative errors
        control_up = -1.5 * vel_y_error
        control_side = -1.0 * angle_error - 0.5 * angular_vel
        
        # Map continuous tracking commands to discrete thruster activations
        if control_up > 0.5 and abs(control_side) < 0.3:
            action = 2  # Fire Main Engine
        elif control_side > 0.1:
            action = 3  # Fire Right Engine (pushes lander left)
        elif control_side < -0.1:
            action = 1  # Fire Left Engine (pushes lander right)
        else:
            action = 0  # Do Nothing / Drift
            
        # Execute action in simulation
        observation, reward, terminated, truncated, info = env.step(action)
        
        if terminated or truncated:
            print(f"Simulation ended at step {step}")
            break
            
    env.close()
    
    # Plotting baseline step response for report documentation
    plt.figure(figsize=(10, 4))
    plt.plot(altitudes, label="Altitude (y)")
    plt.plot(vertical_velocities, label="Vertical Velocity (y_dot)")
    plt.title("Classical Controller Response Curve")
    plt.xlabel("Simulation Steps")
    plt.ylabel("Normalized Units")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_pid_controller()