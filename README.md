# 🚀 Cloud-Scaled Server Monitor (Python/AWS)

A high-performance simulation of an AWS CloudWatch-style monitoring agent. This tool tracks computational power across distributed server nodes and calculates the **minimum operational overhead ($x$)** required to maintain a non-decreasing power sequence across a cluster.

## 🛠️ Key Features
* **Real-time Simulation:** Mocks CPU load retrieval from multiple EC2 instances.
* **Greedy Optimization:** Implements a linear-time $O(n)$ algorithm to calculate scaling requirements.
* **Operational Efficiency:** Focuses on minimizing the sum of increments ($x$) to achieve cluster stability.
* **Contiguous Segment Logic:** Designed to simulate "segment lifts" in horizontally scaled architectures.

## 🧠 The Logic (The "Why")
In high-availability systems, server power must often be non-decreasing to prevent data processing bottlenecks. 
* **The Problem:** If Node A has more power than Node B, Node B becomes a single point of failure.
* **The Solution:** This monitor identifies every "power valley" and calculates the exact units needed to bridge the gap to the previous peak. 

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Git

### Installation & Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/03Sudarshan/Python-Server-Monitor.git](https://github.com/03Sudarshan/Python-Server-Monitor.git)
   cd Python-Server-Monitor
