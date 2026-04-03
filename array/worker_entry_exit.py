"""
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

records1 = [
  ["Paul",     "enter"],
  ["Pauline",  "exit"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Martha",   "exit"],
  ["Joe",      "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Joe",      "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Joe",      "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Joe",      "enter"],
  ["Joe",      "enter"],
  ["Martha",   "exit"],
  ["Joe",      "exit"],
  ["Joe",      "exit"] 
]

Other test cases:

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"],
]

Expected output: ["Raj", "Paul"], ["Paul"]

All Test Cases:
mismatches(records1) => ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]
mismatches(records2) => [], []
mismatches(records3) => ["Paul"], ["Paul"]
mismatches(records4) => ["Raj", "Paul"], ["Paul"]

n: length of the badge records array
"""

# records4 = [
#   ["Raj", "enter"],
#   ["Paul", "enter"],
#   ["Paul", "exit"],
#   ["Paul", "exit"],
#   ["Paul", "enter"],
#   ["Raj", "enter"],
# ]

# Expected output: ["Raj", "Paul"], ["Paul"]

# {
#     Paul: []
# }

# enter_without_exit = [Raj, Paul]
# exit_without_enter = [Paul]
from collections import defaultdict

def worker_miss_records(records: list[list[str]])-> list[list[str]]:
    entered_map = defaultdict(list)
    exit_without_enter = set()
    enter_without_exit = set()
    for name, log in records:
        if log == 'enter' and not entered_map[name]:
            entered_map[name].append("enter")
        elif log == 'enter' and entered_map[name] and entered_map[name][-1] == 'enter':
            enter_without_exit.add(name)
        if log == 'exit' and entered_map[name] and entered_map[name][-1] == 'enter':
            entered_map[name].pop()
        elif log == 'exit' and not entered_map[name]:
            exit_without_enter.add(name)

    for name, enter_list in entered_map.items():
        if enter_list:
            enter_without_exit.add(name)

    return [list(enter_without_exit), list(exit_without_enter)]




records1 = [
  ["Paul",     "enter"],
  ["Pauline",  "exit"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Martha",   "exit"],
  ["Joe",      "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Joe",      "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Joe",      "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Joe",      "enter"],
  ["Joe",      "enter"],
  ["Martha",   "exit"],
  ["Joe",      "exit"],
  ["Joe",      "exit"] 
]

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"],
]

print(worker_miss_records(records1)) # [["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]]
print(worker_miss_records(records2)) # [[], []]
print(worker_miss_records(records3)) # [["Paul"], ["Paul"]]
print(worker_miss_records(records4)) # [["Raj", "Paul"], ["Paul"]]



# improved version, usse set to track inside names
def worker_miss_records(records: list[list[str]]) -> list[list[str]]:
    inside = set()
    enter_without_exit = set()
    exit_without_enter = set()

    for name, log in records:
        if log == 'enter':
            if name in inside:
                enter_without_exit.add(name)  # entered again without exit
            else:
                inside.add(name)
        else:  # exit
            if name not in inside:
                exit_without_enter.add(name)  # exited without entering
            else:
                inside.discard(name)

    enter_without_exit.update(inside)  # still inside = never exited
    return [list(enter_without_exit), list(exit_without_enter)]