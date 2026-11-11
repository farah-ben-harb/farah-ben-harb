"""Deterministic integrity checks for the profile README and local SVG assets."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
URL_RE = re.compile(r"\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LOCAL_EXTENSIONS = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"}


def is_remote(value: str) -> bool:
    return value.startswith(("http://", "https://", "mailto:", "#"))


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


if not README.is_file():
    fail("README.md is missing")

readme = README.read_text(encoding="utf-8")
if "github-hero.svg" not in readme:
    fail("README does not reference the hero asset")

for target in IMAGE_RE.findall(readme):
    target = target.split("#", 1)[0].strip()
    if not target or is_remote(target):
        continue
    path = (README.parent / target).resolve()
    if ROOT not in path.parents and path != ROOT:
        fail(f"local image escapes repository: {target}")
    if not path.is_file():
        fail(f"referenced local image is missing: {target}")

for target in URL_RE.findall(readme):
    target = target.strip()
    if not target or target.startswith("#") or target.startswith("mailto:"):
        continue
    if target.startswith(("http://", "https://")):
        parsed = urlparse(target)
        if not parsed.netloc or " " in target:
            fail(f"invalid external URL: {target}")
        continue
    local = (README.parent / target.split("#", 1)[0]).resolve()
    if not local.is_file():
        fail(f"referenced local link is missing: {target}")

for svg in sorted((ROOT / "assets").glob("*.svg")):
    try:
        root = ET.fromstring(svg.read_text(encoding="utf-8"))
    except (ET.ParseError, UnicodeDecodeError) as exc:
        fail(f"invalid SVG {svg.name}: {exc}")
    if root.tag.rsplit("}", 1)[-1] != "svg":
        fail(f"SVG root element is not svg: {svg.name}")
    if root.get("viewBox") is None:
        fail(f"SVG has no viewBox: {svg.name}")
    if "<script" in svg.read_text(encoding="utf-8").lower():
        fail(f"script element is not allowed in SVG: {svg.name}")

print(f"OK: README links and {len(list((ROOT / 'assets').glob('*.svg')))} SVG assets validated")
