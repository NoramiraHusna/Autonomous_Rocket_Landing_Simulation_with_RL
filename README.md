# Comparative Analysis: PPO Reinforcement Learning vs. Classical PD Control in LunarLander-v3

This project investigates the performance of an intelligent, machine learning-based controller versus a traditional, fixed-rule PD controller within the `LunarLander-v3` simulation environment. The core focus is to determine whether an agent trained using **Proximal Policy Optimization (PPO)** can outperform a classical controller in environments subject to nonlinear dynamics and external wind disturbances.

---

## 🚀 Project Overview
In dynamic control systems, traditional controllers like PD often struggle with complex, non-linear environments or unpredictable external forces. By utilizing Reinforcement Learning, our model learns an adaptive landing policy through trial and error. 

We developed a **split-screen GUI** to demonstrate the direct side-by-side performance of our PPO agent against the baseline PD controller under identical environmental conditions.

---

## 📊 Key Findings
The PPO reinforcement learning agent demonstrated superior robustness and adaptability compared to the classical PD controller across all tested wind disturbance levels.

| Metric | PD Controller (Baseline) | PPO AI Controller |
| :--- | :--- | :--- |
| **Avg. Reward** | Negative (~ -460 to -500) | Positive (~ 160 to 170) |
| **Success Rate** | 0% | 80% - 90% |
| **Crash Rate** | 100% | 10% |

> **Conclusion:** The machine learning controller effectively learned to compensate for lateral drift and vertical velocity, whereas the fixed-rule PD controller consistently failed to stabilize the lander under wind disturbances.

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
