# Comparative Analysis: PPO Reinforcement Learning vs. Classical PD Control in LunarLander-v3

This project investigates the performance of an intelligent, machine learning-based controller versus a traditional, fixed-rule PD controller within the `LunarLander-v3` simulation environment. The core focus is to determine whether an agent trained using **Proximal Policy Optimization (PPO)** can outperform a classical controller in environments subject to nonlinear dynamics and external wind disturbances.

---

## 🚀 Project Overview
In dynamic control systems, traditional controllers like PD often struggle with complex, non-linear environments or unpredictable external forces. By utilizing Reinforcement Learning, our model learns an adaptive landing policy through trial and error. 

We developed a **split-screen GUI** to demonstrate the direct side-by-side performance of our PPO agent against the baseline PD controller under identical environmental conditions.

---

## ⚙️ Training Configuration
The PPO agent was trained using the following parameters:

| Parameter | Value |
| :--- | :--- |
| **Simulation Environment** | `LunarLander-v3` |
| **Algorithm** | Proximal Policy Optimization (PPO) |
| **Policy** | `MlpPolicy` |
| **Learning Rate** | 0.0003 |
| **Training Duration** | 100,000 timesteps |
| **Logging** | `./ppo_lunar_tensorboard/` |
| **Saved Model** | `ppo_lunar_lander.zip` |

---

## 📊 Evaluation Results

### Batch Performance Comparison
The controllers were evaluated across three levels of wind disturbance (0, 8, and 12). 

| Wind Power | Controller | Avg. Reward | Avg. Steps | Avg. Tracking Error | Success Rate | Crash Rate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | PD Controller | -500.01 | 78.1 | 0.980 | 0% | 100% |
| 0 | PPO AI | 169.06 | 630.4 | 0.579 | 80% | 10% |
| 8 | PD Controller | -496.48 | 67.8 | 0.949 | 0% | 100% |
| 8 | PPO AI | 159.57 | 553.5 | 0.588 | 90% | 10% |
| 12 | PD Controller | -468.97 | 61.5 | 0.953 | 0% | 100% |
| 12 | PPO AI | 167.71 | 624.7 | 0.622 | 80% | 10% |

### Result Interpretation
The batch results show a clear performance difference. The PD controller produced negative average rewards and a 100% crash rate across all tested wind levels, as its fixed-rule logic could not compensate for environmental disturbances. In contrast, the PPO AI achieved consistently positive rewards and high success rates (80-90%), demonstrating superior adaptability, robustness, and lower tracking error.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Environment:** Gymnasium (LunarLander-v3)
* **Machine Learning:** Stable-Baselines3 (PPO)
* **GUI:** Pygame
* **Simulation/Control:** Classical PD Implementation

---

## 📂 Project Structure
```text
.
├── models/             # Saved PPO trained policy (.zip)
├── scripts/            # Training and evaluation scripts
├── gui/                # Pygame split-screen implementation
├── results/            # Performance graphs and data logs
└── README.md
