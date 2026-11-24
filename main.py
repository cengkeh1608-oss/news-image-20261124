#!/usr/bin/env python3
"""Entry program: copy the pre-rendered front page to the output dir.

The front page (entry.png, 1024x1024) summarises the verified world news
of Tuesday 24 November 2026. The image was drawn offline from real,
same-day reporting; this program only copies bytes, so every run produces
the identical file.

Lead story choice: the Banten factory fire (24 killed, ~30 missing) won
over COP31 because it is the day's freshest breaking story with a human
toll, while COP31's no-deal outcome — already the previous day's lead —
still appears as the first supporting story.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/output"

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
