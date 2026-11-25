"""Write the tech-support one-liner to /output/entry.txt.

Gate: UTF-8 text, 1-199 characters, not only whitespace.
"""

import os

LINE = "Have you tried turning it off and on again? I have. Three times. The computer is fine now. It is just pretending not to know you anymore."

if len(LINE) > 199 or not LINE.strip():
    raise SystemExit(f"line must be 1-199 characters, got {len(LINE)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"wrote /output/entry.txt: {len(LINE)} characters")
