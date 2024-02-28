#!/usr/bin/python3
"""Module performs a log parsing """

import sys

def compute_metrics(line):
    """ displays function """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        return ip_address, status_code, file_size
    except:
        return None, None, None

def print_statistics(total_file_size, lines_by_status_code):
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(lines_by_status_code.keys()):
        print(f"{status_code}: {lines_by_status_code[status_code]}")

if __name__ == "__main__":
    total_file_size = 0
    lines_by_status_code = {}

    try:
        line_count = 0
        for line in sys.stdin:
            ip_address, status_code, file_size = compute_metrics(line.strip())

            if ip_address is None:
                continue

            total_file_size += file_size
            lines_by_status_code[status_code] = lines_by_status_code.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, lines_by_status_code)

    except KeyboardInterrupt:
        print_statistics(total_file_size, lines_by_status_code)
