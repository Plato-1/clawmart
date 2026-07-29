#!/usr/bin/env python3
"""Generate a book summary using the AI model (called from agent context)."""
import sys, os

BOOK_DIR = os.path.expandvars(r"${HOME}\trading_bot")

def generate_summary(book_file, output_file):
    """Read book, produce summary. The actual AI generation happens
    when the agent processes this in a cron/chat context."""
    path = os.path.join(BOOK_DIR, book_file)
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    
    # Truncate to manageable size for the model
    max_chars = 30000
    if len(text) > max_chars:
        text = text[:max_chars//2] + "\n...[truncated]...\n" + text[-max_chars//2:]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Prepared {book_file} ({len(text)} chars) → {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: prepare_summary.py <book_file> <output_file>")
        sys.exit(1)
    generate_summary(sys.argv[1], sys.argv[2])
