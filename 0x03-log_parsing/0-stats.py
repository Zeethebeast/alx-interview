#!/usr/bin/python3
"""Script that reads from stdin line by line and computes metrics."""

import sys
import signal
import re

# Initialize variables
status_counts = {}
total_file_size = 0


def signal_handler(sig, frame):
    """
    Handle SIGINT (CTRL+C) to print a summary and exit.

    Prints the total file size and count of each HTTP status code
    before exiting the program.
    """
    print(f"File size: {total_file_size}")
    for status in sorted(status_counts.keys()):
        print(f"{status}: {status_counts[status]}")
    sys.exit(0)


# Set up the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

# Regular expression to parse the log format
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.*\] ".*" (\d{3}) (\d+)'

# Read from stdin line by line
for line in sys.stdin:
    match = re.match(log_pattern, line.strip())
    if match:
        ip_address, status_code, file_size = match.groups()
        total_file_size += int(file_size)

        # Count occurrences of each status code
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

    # Print summary every 10 lines
    if sum(status_counts.values()) % 10 == 0:
        print(f"File size: {total_file_size}")
        for status in sorted(status_counts.keys()):
            print(f"{status}: {status_counts[status]}")
