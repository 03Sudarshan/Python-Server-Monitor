import random
import time

class ServerMonitor:
    def __init__(self, node_count):
        self.nodes = [f"node-{i}" for i in range(node_count)]
        
    def get_mock_cpu_loads(self):
        """Simulates fetching real-time CPU metrics from AWS EC2"""
        return [random.randint(10, 90) for _ in self.nodes]

    def calculate_scaling_overhead(self, loads):
        """
        The 'Non-Decreasing' Logic: Calculates the min sum of 
        increments (x) to stabilize the cluster.
        """
        total_x = 0
        current_max = loads[0]
        
        for i in range(1, len(loads)):
            if loads[i] < current_max:
                # We found a 'valley', calculate the gap to the peak
                total_x += (current_max - loads[i])
            else:
                # New peak found
                current_max = loads[i]
        return total_x

if __name__ == "__main__":
    monitor = ServerMonitor(node_count=5)
    while True:
        current_loads = monitor.get_mock_cpu_loads()
        cost = monitor.calculate_scaling_overhead(current_loads)
        
        print(f"Current Metrics: {current_loads}")
        print(f"Operational Scaling Cost (x): {cost}")
        print("-" * 30)
        time.sleep(3) # Runs every 3 seconds