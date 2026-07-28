# Agent Memory DB
## Setup
1. Install: pip install aiosqlite
2. Connect via MCP: sqlite-memory
3. Use: store(key, value), recall(key), search(query)
## API
- POST /memory/store — persist key-value
- POST /memory/recall — retrieve by key
- POST /memory/search — full-text search across all stored data
- GET /memory/backup — export entire database