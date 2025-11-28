#!/usr/bin/env python3
import csv

path = "analytics/data.csv"

with open(path, newline='', encoding="utf8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("=== Analytics Script Output ===")
print(f"Total movies: {len(rows)}")
print(f"Columns: {', '.join(rows[0].keys())}")
print("First row:", rows[0])
