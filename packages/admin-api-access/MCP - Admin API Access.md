---
tags:
  - moc
  - mcp
  - api/app/admin
up: "[[MCP Tools]]"
---
# MCP - Admin API Access

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 21
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/admin/api-access/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## API Token

- [[Admin API Access - Get all API tokens in an org]] — `GET /orgs/{orgId}/api-tokens` — Get all API tokens in an org
- [[Admin API Access - Bulk revoke API tokens in an organization]] — `DELETE /orgs/{orgId}/api-tokens` — Bulk revoke API tokens in an organization ✏️
- [[Admin API Access - Get API token count in an org]] — `GET /orgs/{orgId}/api-tokens/count` — Get API token count in an org
- [[Admin API Access - Get service account API token count in an org]] — `POST /orgs/{orgId}/service-accounts/count` — Get service account API token count in an org
- [[Admin API Access - Revoke all API tokens for a service account]] — `DELETE /orgs/{orgId}/service-accounts/{serviceAccountId}/api-tokens` — Revoke all API tokens for a service account ✏️

## API Key

- [[Admin API Access - Get API key count in an org]] — `GET /orgs/{orgId}/api-keys/count` — Get API key count in an org
- [[Admin API Access - Get all API keys in an org]] — `GET /orgs/{orgId}/api-keys` — Get all API keys in an org
- [[Admin API Access - Revoke an API key for an org]] — `PATCH /orgs/{orgId}/api-keys/revoke/{apiKeyId}` — Revoke an API key for an org ✏️

## OAuth Client

- [[Admin API Access - Get all OAuth clients in an org]] — `GET /orgs/{orgId}/oauth-clients` — Get all OAuth clients in an org
- [[Admin API Access - Create an OAuth client]] — `POST /orgs/{orgId}/oauth-clients` — Create an OAuth client ✏️
- [[Admin API Access - Get OAuth client count in an org]] — `POST /orgs/{orgId}/oauth-clients/count` — Get OAuth client count in an org
- [[Admin API Access - Get an OAuth client]] — `GET /orgs/{orgId}/oauth-clients/{clientId}` — Get an OAuth client
- [[Admin API Access - Delete an OAuth client]] — `DELETE /orgs/{orgId}/oauth-clients/{clientId}` — Delete an OAuth client ✏️

## Service Account

- [[Admin API Access - Get API tokens for all service accounts in an org]] — `GET /orgs/{orgId}/service-accounts/api-tokens` — Get API tokens for all service accounts in an org
- [[Admin API Access - Get API tokens for a service account]] — `GET /orgs/{orgId}/service-accounts/{serviceAccountId}/api-tokens` — Get API tokens for a service account
- [[Admin API Access - List service accounts in an org]] — `GET /orgs/{orgId}/service-accounts` — List service accounts in an org
- [[Admin API Access - Create a service account]] — `POST /orgs/{orgId}/service-accounts` — Create a service account ✏️
- [[Admin API Access - Update a service account]] — `PATCH /orgs/{orgId}/service-accounts` — Update a service account ✏️
- [[Admin API Access - Delete a service account]] — `DELETE /orgs/{orgId}/service-accounts/{serviceAccountId}` — Delete a service account ✏️
- [[Admin API Access - Get OAuth clients for all service accounts in an org]] — `GET /orgs/{orgId}/service-accounts/oauth-clients` — Get OAuth clients for all service accounts in an org
- [[Admin API Access - Get OAuth clients for a service account]] — `GET /orgs/{orgId}/service-accounts/{serviceAccountId}/oauth-clients` — Get OAuth clients for a service account
