#!/usr/bin/python3
"""Module performs a log parsing """

import sys


def compute_metrics(line):
    """ displays function """
    try:
        parts = line.split()
        ip_address = parts[0]
        status = int(parts[-2])
        file_size = int(parts[-1])

        return ip_address, status, file_size
    except None:
        return None, None, None


def print_statistics(total_size, status_code):
    print(f"Total file size: {total_size}")
    for status in sorted(status_code.keys()):
        print(f"{status}: {status_code[status]}")


if __name__ == "__main__":
    total_size = 0
    status_code = {}

    try:
        line_count = 0
        for line in sys.stdin:
            ip_address, status, file_size = compute_metrics(line.strip())

            if ip_address is None:
                continue

            total_size += file_size
            status_code[status] = status_code.get(status, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_code)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code)
