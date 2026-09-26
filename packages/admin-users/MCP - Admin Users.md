---
tags:
  - moc
  - mcp
  - api/app/admin
up: "[[MCP Tools]]"
---
# MCP - Admin Users

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 10
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/admin/user-management/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Manage

- [[Admin Users - Get user management permissions]] — `GET /users/{account_id}/manage` — Get user management permissions

## Profile

- [[Admin Users - Get profile]] — `GET /users/{account_id}/manage/profile` — Get profile
- [[Admin Users - Update profile]] — `PATCH /users/{account_id}/manage/profile` — Update profile ✏️

## Email

- [[Admin Users - Set email]] — `PUT /users/{account_id}/manage/email` — Set email ✏️

## Api Tokens

- [[Admin Users - Get API tokens]] — `GET /users/{account_id}/manage/api-tokens` — Get API tokens
- [[Admin Users - Delete API token]] — `DELETE /users/{account_id}/manage/api-tokens/{tokenId}` — Delete API token ✏️

## Lifecycle

- [[Admin Users - Deactivate a user]] — `POST /users/{account_id}/manage/lifecycle/disable` — Deactivate a user ✏️
- [[Admin Users - Activate a user]] — `POST /users/{account_id}/manage/lifecycle/enable` — Activate a user ✏️
- [[Admin Users - Delete account]] — `POST /users/{account_id}/manage/lifecycle/delete` — Delete account ✏️
- [[Admin Users - Cancel delete account]] — `POST /users/{account_id}/manage/lifecycle/cancel-delete` — Cancel delete account ✏️
