def ping(host):
    try:
        # Ping the host
        subprocess.check_call(['ping', '-c', '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return 1
    except subprocess.CalledProcessError:
        return 0

def main():
    print("Starting HTTP server on port 8001...")
    start_http_server(8001)  # Expose metrics on port 8001
    print("HTTP server started.")
    while True:
        # List of hosts to ping
        for host in ['192.168.96.68', '192.168.96.69']:
            status = ping(host)
            print(f"Ping {host}: {status}")
            ping_status.labels(target=host).set(status)
        time.sleep(60)  # Ping every 60 seconds

if __name__ == '__main__':
    main()
