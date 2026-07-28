#!/usr/bin/env python3
"""Send promotional email batches via AgentMail background jobs."""
import json, subprocess, time, os

BATCHES_FILE = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\campaigns\send_batches.json")
with open(BATCHES_FILE) as f:
    data = json.load(f)

batches = data['batches']
total = len(batches)

# Skip first batch (already sent manually)
remaining = batches[1:]

print(f'Sending {len(remaining)} remaining batches ({total} total, 1 already sent)')
print(f'Each batch: 5 emails. Total emails to send: {len(remaining) * 5}')
print(f'Expected completion: {len(remaining) * 3} minutes (at ~3 sec per batch + rate limiting)')
print()
print('Batch index ranges (for reference):')
for i in range(0, len(remaining), 50):
    end = min(i + 50, len(remaining))
    print(f'  Batches {i+1}-{end}: {len(remaining[i:end])} batches ({len(remaining[i:end])*5} emails)')
