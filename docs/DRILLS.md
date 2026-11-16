# Planted-fault drills

Each blocking check counts only after it has been seen to fail.

| Date | What was planted | What refused it |
|:--|:--|:--|
| 2026-11-16 | `plugins/vibeqm/plugin.json`: the plugin version changed to 0.1.9 while the other manifests say 0.1.7, staged and committed through the committed `.githooks/pre-commit` | The hook ran `make check`; `tools/check_repo.py` reported "plugin versions differ" and the commit was refused. File restored. |
