from prometheus_client import start_http_server, Gauge
import time
import os
# Define the metrics to monitor
dc_status = Gauge('cassandra_dc_status', 'Status of the DC node')
dr_status = Gauge('cassandra_dr_status', 'Status of the DR node')
replication_status = Gauge('cassandra_replication_status', 'Status of data replication between DC and DR')
# Function to check the connection status of a Cassandra node
def check_node_status(ip):
    response = os.system(f"ping -c 1 {ip}")
    return response == 0  # Returns True if the node is up
# Function to check the replication status
def check_replication_status():
    # Implement the logic to check data replication status
    # For simplicity, let's assume it's up if both nodes are up
    return check_node_status('192.168.96.74') and check_node_status('192.168.96.75')
def main():
    # Start the Prometheus serve
    start_http_server(8001)  # Expose metrics on port 8001
    while True:
        # Check and update the status of the DC and DR nodes
        dc_status.set(1 if check_node_status('192.168.96.74') else 0) # mention your dc and dr IPs
        dr_status.set(1 if check_node_status('192.168.96.75') else 0)
        # Check and update the data replication status
        replication_status.set(1 if check_replication_status() else 0)
        # Wait for the next check
        time.sleep(60)  # Ping every 60 seconds
if __name__ == "__main__":
    main()
