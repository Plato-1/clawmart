#!/usr/bin/env python3
"""Generate a BisonQuant MCP license key for a paying customer.
Usage: python make_key.py customer@email.com
Send the printed key to the customer after payment confirmation."""
import hashlib, hmac, sys

_SECRET = b"bq-mcp-2026-v1"

if len(sys.argv) != 2:
    sys.exit(__doc__)
email = sys.argv[1].strip().lower()
sig = hmac.new(_SECRET, email.encode(), hashlib.sha256).hexdigest()[:16]
print(f"{email}-{sig}")