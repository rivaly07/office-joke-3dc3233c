import os
import sys

LINE = "I replied-all to warn the office about reply-all; forty-one colleagues replied-all to say I was right."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(LINE)
    except OSError as exc:
        sys.stderr.write("could not write entry: %s\n" % (exc,))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
