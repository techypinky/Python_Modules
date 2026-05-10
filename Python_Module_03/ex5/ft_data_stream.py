import random
from typing import Generator

def gen_event() -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "move", "grab", "climb", "swim", "use", "release"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(lst) -> Generator[tuple, None, None]:
    while len(lst) > 0:
        idx = random.randrange(len(lst))
        event = lst.pop(idx)
        yield event

print("=== Game Data Stream Processor ===")

g = gen_event()

for i in range(1000):
    e = next(g)
    print(f"Event {i}: Player {e[0]} did action {e[1]}")

events = []

for i in range(10):
    events.append(next(g))

print(f"Built list of 10 events: {events}")

for e in consume_event(events):
    print(f"Got event from list: {e}")
    print(f"Remains in list: {events}")