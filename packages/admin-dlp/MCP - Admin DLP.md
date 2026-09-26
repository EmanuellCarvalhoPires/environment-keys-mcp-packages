---
tags:
  - moc
  - mcp
  - api/app/admin
up: "[[MCP Tools]]"
---
# MCP - Admin DLP

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 8
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/admin/dlp/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Classification Level

- [[Admin DLP - Get all classification levels by orgId]] — `GET /orgs/{orgId}/classification-levels` — Get all classification levels by orgId
- [[Admin DLP - Create a new classification level]] — `POST /orgs/{orgId}/classification-levels` — Create a new classification level ✏️
- [[Admin DLP - Get a classification level]] — `GET /orgs/{orgId}/classification-levels/{levelId}` — Get a classification level
- [[Admin DLP - Edit a classification level]] — `PUT /orgs/{orgId}/classification-levels/{levelId}` — Edit a classification level ✏️
- [[Admin DLP - Publish classification level(s)]] — `POST /orgs/{orgId}/classification-levels/publish` — Publish classification level(s) ✏️
- [[Admin DLP - Archive a data classification level]] — `POST /orgs/{orgId}/classification-levels/archive` — Archive a data classification level ✏️
- [[Admin DLP - Restore a classification level]] — `POST /orgs/{orgId}/classification-levels/restore` — Restore a classification level ✏️
- [[Admin DLP - Reorder classification levels]] — `POST /orgs/{orgId}/classification-levels/reorder` — Reorder classification levels ✏️
