import os

LINE = "Today my agent fixed its chess engine's endgame, then lost four games in a row to a fish."

MAX_CHARS = 200

def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
