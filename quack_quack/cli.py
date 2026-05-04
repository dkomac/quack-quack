import time
import sys
import shutil

DUCK_A = [
    "    ___   ",
    " __(o  )> ",
    "(       ) ",
    " \\_____/  ",
    "   /  \\   ",
]

DUCK_B = [
    "    ___   ",
    " __(o  )> ",
    "(       ) ",
    " \\_____/  ",
    "   \\  /   ",
]

DUCK_WIDTH = 10


def term_width():
    return shutil.get_terminal_size((80, 24)).columns


def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def draw(pose, x, text=""):
    clear()
    sys.stdout.write("\n\n")
    pad = " " * max(0, x)
    if text:
        w = len(text)
        lines = [
            pad + pose[0],
            pad + pose[1] + " .-" + "-" * w + "-.",
            pad + pose[2] + " | " + text + " |",
            pad + pose[3] + " '-" + "-" * w + "-'",
            pad + pose[4],
        ]
    else:
        lines = [pad + line for line in pose]
    sys.stdout.write("\n".join(lines) + "\n")
    sys.stdout.flush()


def walk_in():
    tw = term_width()
    center = min((tw - DUCK_WIDTH) // 2, 20)
    for x in range(0, center + 1, 5):
        draw([DUCK_A, DUCK_B][(x // 5) % 2], x)
        time.sleep(0.1)
    return center


def quack(x):
    full = "QUACK QUACK!"
    for i in range(1, len(full) + 1):
        draw(DUCK_A, x, full[:i])
        time.sleep(0.12)
    time.sleep(1.0)


def walk_out(x):
    for xx in range(x, x + 20, 5):
        draw([DUCK_A, DUCK_B][(xx // 5) % 2], xx)
        time.sleep(0.1)
    clear()


def main():
    try:
        center = walk_in()
        quack(center)
        walk_out(center)
    except KeyboardInterrupt:
        clear()
