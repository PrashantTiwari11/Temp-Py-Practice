# 75_python_command_line_tools.py
# Command-Line Tools - 10 practical programs/features
import argparse
import sys
import os

print("1. Script name:", os.path.basename(sys.argv[0]))
print("2. Argument count:", len(sys.argv) - 1)
print("3. Python executable:", sys.executable)
print("4. Working directory:", os.getcwd())

parser = argparse.ArgumentParser(description="Simple Python CLI Demo")
parser.add_argument("--name", default="Student", help="Name to display")
parser.add_argument("--age", type=int, default=20, help="Age to display")

args, unknown = parser.parse_known_args()

print("5. Name:", args.name)
print("6. Age:", args.age)
print("7. Next year age:", args.age + 1)
print("8. Unknown arguments:", unknown)
print("9. Greeting:", f"Hello, {args.name}!")
print("10. CLI tool completed successfully.")
