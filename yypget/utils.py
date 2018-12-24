import re

def r1(pattern, text):
    m = re.search(pattern, text)
    if m:
        return m.group(1)
