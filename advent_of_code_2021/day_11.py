"""
Day 11: Dumbo Octopus
"""
import time
import numpy as np
from rich.console import Console
from rich.highlighter import Highlighter
from rich.panel import Panel
from rich.live import Live
from rich import box

class FlashHighlighter(Highlighter):
    color_map = {
        "0": "color(15)",
        "1": "color(16)",
        "2": "color(17)",
        "3": "color(18)",
        "4": "color(19)",
        "5": "color(20)",
        "6": "color(21)",
        "7": "color(27)",
        "8": "color(33)",
        "9": "color(39)",
    }
    def highlight(self, text):
        for i in range(len(text)):
            text.stylize(self.color_map.get(text.plain[i:i+1]), i, i + 1)
console = Console(highlighter=FlashHighlighter())


with open("data/day-11-test.txt") as f:
    x = np.array([
        [int(c) for c in line.strip()]
        for line in f
    ])

def array_to_string(a):
    return "\n".join(
        "".join(str(a[i,j]) for i in range(a.shape[0]))
        for j in range(a.shape[1])
    )

def generate_panel(a):
    return Panel(
        array_to_string(x),
        box=box.SQUARE, width=14, height=12, highlight=True
    )


with Live(generate_panel(x), console=console) as live:
    flashes = 0
    for step in range(1000):
        x += 1
        while x.max() > 9:
            for i,j in np.transpose((x > 9).nonzero()):
                a,b,c,d = max(0,i-1), min(x.shape[0],i+2), max(0,j-1), min(x.shape[1],j+2)
                x[a:b,c:d] = np.where(x[a:b,c:d] == 0, x[a:b,c:d], x[a:b,c:d]+1)
                x[i,j] = 0
                flashes += 1
        live.update(generate_panel(x), refresh=True)
        time.sleep(0.10)
        if step == 99:
            print("part 1:", flashes)
        if (x == 0).all():
            print("part 2:", step+1)
            break
