#!/usr/bin/env python3
"""Turn a narration script into timed SRT captions.

Timing is estimated from speaking rate (words per minute), so captions line up with
text-to-speech or a steady read. Re-time in an editor if the delivery varies a lot.

Usage:
    python make_srt.py narration.txt -o captions.srt [--wpm 150] [--max-chars 42] [--start 0]
"""
import argparse
import re
import sys


def clean(text):
    # Drop producer notes like [LIB-ee], SSML tags, and stage directions in [BRACKETS].
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[[^\]]*\]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def chunk(text, max_chars):
    """Split into caption-sized chunks, preferring sentence and clause boundaries."""
    sentences = re.split(r"(?<=[.!?…])\s+", text)
    chunks = []
    for sentence in sentences:
        line = ""
        for word in sentence.split():
            candidate = f"{line} {word}".strip()
            if len(candidate) > max_chars and line:
                chunks.append(line)
                line = word
            else:
                line = candidate
        if line:
            chunks.append(line)
    return chunks


def timestamp(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build_srt(text, wpm=150, max_chars=42, start=0.0, min_dur=1.0, gap=0.05):
    seconds_per_word = 60.0 / wpm
    t = start
    blocks = []
    for i, line in enumerate(chunk(clean(text), max_chars), 1):
        words = len(line.split())
        dur = max(min_dur, words * seconds_per_word)
        if line.endswith((".", "!", "?", "…")):
            dur += 0.3  # natural pause at sentence end
        blocks.append(f"{i}\n{timestamp(t)} --> {timestamp(t + dur - gap)}\n{line}\n")
        t += dur
    return "\n".join(blocks), t


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", help="narration text file, or - for stdin")
    p.add_argument("-o", "--output", help="output .srt (default: stdout)")
    p.add_argument("--wpm", type=float, default=150, help="speaking rate, words/min (default 150)")
    p.add_argument("--max-chars", type=int, default=42, help="max characters per caption (default 42)")
    p.add_argument("--start", type=float, default=0.0, help="start offset in seconds")
    args = p.parse_args()

    text = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    srt, total = build_srt(text, args.wpm, args.max_chars, args.start)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(srt)
        print(f"Wrote {args.output} — estimated length {total:.1f}s", file=sys.stderr)
    else:
        sys.stdout.write(srt)


if __name__ == "__main__":
    main()
