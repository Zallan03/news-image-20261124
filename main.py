#!/usr/bin/env python3
"""Copy entry.png to the output directory and verify its checksum.

Standard library only. The image is pre-rendered and shipped in this
repository; this program only copies it to $MAKEFUN_OUTPUT_DIR
(default /output) and checks its sha256 before writing, so repeated
runs always produce byte-identical output.
"""
import hashlib
import os
import sys

EXPECTED_SHA256 = "7d2d4b457472e83654d2954bbe90b4806906e27fb0a3d574cbfdcee55851a99d"
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("checksum mismatch: %s != %s" % (digest, EXPECTED_SHA256),
              file=sys.stderr)
        return 1
    with open(dst, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
