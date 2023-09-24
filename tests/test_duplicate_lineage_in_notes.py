#!/usr/bin/env python3


def check_for_duplicates(filename, buffer_size=1024 * 1024):  # 1MB buffer
    seen = set()
    buffer = ""
    is_valid = True
    line_counter = 0  # Counter for tracking the number of lines seen

    with open(filename, "r") as f:
        while True:
            chunk = f.read(buffer_size)
            if not chunk:
                break

            buffer += chunk
            lines = buffer.split("\n")
            for i in range(len(lines) - 1):
                line_counter += 1  # Increment the line counter
                fields = lines[i].split("\t")

                if len(fields) > 2:
                    print(f"lineage_notes.txt: Line {line_counter} has more than 2 fields `{fields}`")
                    is_valid = False

                field = fields[0]
                if field in seen:
                    print(f"Duplicate {field} found in line {line_counter}")
                    is_valid = False
                seen.add(field)
            buffer = lines[
                -1
            ]  # keep the last, potentially incomplete line for the next iteration

    return is_valid


# Usage
if check_for_duplicates("lineage_notes.txt") is False:
    exit(1)  # Exit with status 1 if duplicates found
else:
    exit(0)  # Exit with status 0 otherwise
