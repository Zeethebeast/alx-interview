#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
status_counts = {}
total_file_size = 0


def signal_handler(sig, frame):
    """Handle CTRL+C to print a summary."""
    print("\nSummary:")
    print(f"Total file size: {total_file_size}")
    for status, count in status_counts.items():
        print(f"Status {status}: {count}")
    sys.exit(0)


# Set up the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

# Regular expression to parse log format
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.*\] ".*" (\d{3}) (\d+)'

# Read from stdin
for line in sys.stdin:
    match = re.match(log_pattern, line.strip())
    if match:
        ip_address, status_code, file_size = match.groups()
        total_file_size += int(file_size)

        # Count status codes
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

    # Print summary every 10 lines (for example)
    if sum(status_counts.values()) % 10 == 0:
        print(f"Total file size: {total_file_size}")
