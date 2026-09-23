# 95_python_command_pattern_parser.py
# Command Parsing and Validation - 10 practical features
import shlex
import re

commands = [
    "add user Prashant 20",
    "delete user Aman",
    "show users",
    "update marks 101 85",
    "search Python programming"
]

# 1. Split command safely
for command in commands:
    print("1. Parsed:", shlex.split(command))

# 2. Identify command
tokens = shlex.split(commands[0])
print("2. Main command:", tokens[0])

# 3. Identify entity
print("3. Entity:", tokens[1])

# 4. Extract user name
print("4. User name:", tokens[2])

# 5. Extract integer argument
print("5. Age:", int(tokens[3]))

# 6. Regular expression command validation
pattern = r"^add user [A-Za-z]+ \d+$"
print("6. Valid add command:", bool(re.match(pattern, commands[0])))

# 7. Parse marks update
match = re.match(r"update marks (\d+) (\d+)", commands[3])
if match:
    print("7. Roll and marks:", match.groups())

# 8. Search phrase
search = commands[4].split(maxsplit=1)
print("8. Search keyword:", search[1])

# 9. Command dispatcher
def dispatch(command):
    if command.startswith("add user"):
        return "Adding user"
    if command.startswith("delete user"):
        return "Deleting user"
    if command == "show users":
        return "Showing users"
    return "Unknown command"

print("9. Dispatch:", [dispatch(c) for c in commands])

# 10. Help command
help_text = {
    "add user": "add user NAME AGE",
    "delete user": "delete user NAME",
    "show users": "show users",
    "update marks": "update marks ROLL MARKS"
}
print("10. Help:", help_text)
