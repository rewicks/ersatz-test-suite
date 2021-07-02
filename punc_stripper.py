#!/usr/bin/env python3

import sys
import string

from ersatz import determiner

det = determiner.MultilingualPunctuation()

skipped = []
for line in sys.stdin:
    line = line.rstrip()
    right_context = " "
    if det(line, right_context):
        print(line)
