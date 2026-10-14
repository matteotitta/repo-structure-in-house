#!/usr/bin/env python3
"""ASCII result-card generator for /level --format ascii.

Reads a JSON payload from stdin and prints a fixed-width, copy-paste-shareable
card. Writes the same to ~/Desktop/claude-code-level.txt. Asserts every line is
identical width so the box stays aligned in any monospace surface (terminal,
GitHub, Slack/Discord code block).

Payload:
{
  "level": 10, "name": "Swarm", "vibe": "the apex · agents managing agents",
  "pillars": {"Context": 4, "Skills": 4, "Integrations": 4, "Orchestration": 4},
  "takeaway": ["line 1 (<= ~48 chars)", "line 2", "line 3"],
  "brand_name": "Acme", "brand_url": "acme.com"
}

Usage:  echo '<json>' | python3 ascii-card.py
Brand:  brand_name/brand_url come from the resolved brand kit's `name`/domain
        (see SKILL.md "Resolve the brand" — from context/brand/brand-kit.md).
        ASCII is monochrome — brand presence
        is the wordmark + domain, not colour.
"""
import sys, json, os

W = 54  # inner width; box renders W+2 wide. Keep <=58 for mobile sharing.


def row(s=""):
    s = " " + s
    assert len(s) <= W, f"line too long ({len(s)}): {s!r}"
    return "│" + s.ljust(W) + "│"


def hdr(left, right):
    gap = W - 2 - len(left) - len(right)
    assert gap >= 1, f"header too long: {left!r} / {right!r}"
    return "│" + " " + left + " " * gap + right + " " + "│"


def bar(score, width=18):
    f = round(score / 4 * width)
    return "█" * f + "░" * (width - f)


def render(p):
    level = int(p["level"])
    name = str(p["name"]).upper()
    vibe = str(p.get("vibe", ""))
    pillars = p["pillars"]
    takeaway = p.get("takeaway", [])
    brand_name = p.get("brand_name", "Your Marketing OS")
    brand_url = p.get("brand_url", "")

    top, mid, bot = "┌" + "─" * W + "┐", "├" + "─" * W + "┤", "└" + "─" * W + "┘"
    nums = " ".join(f"{n:>2}" for n in range(11))
    # ● cleared (n<level) · ◆ current (n==level) · ○ ahead (n>level)
    mk = lambda n: "◆" if n == level else ("●" if n < level else "○")
    mark = " ".join(f"{mk(n):>2}" for n in range(11))

    out = [top, hdr("THE 10 LEVELS OF CLAUDE CODE", brand_name), mid, row(),
           row(f"LEVEL  {level} / 10   —   {name}")]
    if vibe:
        out.append(row(vibe))
    out += [row(), row("YOUR CLIMB"), row(nums), row(mark + "   you are here"), row(),
            row("THE 4 SYSTEMS")]
    for n, s in pillars.items():
        out.append(row(f"{n:<14}{bar(int(s))}  {int(s)}/4"))
    if takeaway:
        out.append(row())
        for t in takeaway:
            out.append(row(t))
    out += [row(), mid, hdr(brand_url, "run /level for your score"), bot]

    widths = {len(l) for l in out}
    assert widths == {W + 2}, f"MISALIGNED line widths: {widths}"
    return "\n".join(out)


if __name__ == "__main__":
    payload = json.load(sys.stdin)
    chart = render(payload)
    out_path = os.path.expanduser("~/Desktop/claude-code-level.txt")
    with open(out_path, "w") as f:
        f.write(chart + "\n")
    print(chart)
    print(f"\n[saved: {out_path}]")
