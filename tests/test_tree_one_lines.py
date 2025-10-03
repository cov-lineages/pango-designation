#!/usr/bin/env python3


def check_for_tree_one_lines(filename, buffer_size=1024 * 1024):  # 1MB buffer
    """Check for erroneous 'tree one = (' lines in lineages.csv"""
    buffer = ""
    is_valid = True
    line_counter = 0

    with open(filename, "r") as f:
        while True:
            chunk = f.read(buffer_size)
            if not chunk:
                break

            buffer += chunk
            lines = buffer.split("\n")
            for i in range(len(lines) - 1):
                line_counter += 1
                line = lines[i]
                # Check for lines that start with spaces and contain "tree one = ("
                if line.startswith("  tree one = ("):
                    print(f"Error: Found erroneous 'tree one = (' line at line {line_counter}: {line}")
                    is_valid = False
            buffer = lines[-1]  # keep the last, potentially incomplete line

    return is_valid


# Usage
if check_for_tree_one_lines("lineages.csv") is False:
    exit(1)  # Exit with status 1 if errors found
else:
    exit(0)  # Exit with status 0 otherwise
