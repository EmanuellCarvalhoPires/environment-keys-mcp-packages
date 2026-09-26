---
tags:
  - atlassian/instance
  - template
type: Cloud
url: https://empresa.atlassian.net
cloud_id:
assets_workspace_id:
api_version: 3
email:
account_id:
token_type: API token
auth_token:
org_id:
admin_auth_token:
scim_directory_id:
scim_auth_token:
---
# Atlassian instance - Template

## Properties used by the tools

This is a **service note** for the Environment Keys plugin. The downloaded Atlassian MCP tools pick this instance through the `instance` parameter and read the properties below. No request or tool note stores instance values: they live only here.

| Property | Used by |
| --- | --- |
| `url` | Jira, JSW, JSM, Confluence and Automation (calls on the site itself) |
| `cloud_id` | Automation, Assets, Forms, CSM and JSM Ops |
| `assets_workspace_id` | Assets (find it with the `jsm_get_assets_workspaces` tool) |
| `auth_token` | `Authorization` header of every API on the site and on `api.atlassian.com` |
| `org_id`, `admin_auth_token` | Admin APIs (organization) |
| `scim_directory_id`, `scim_auth_token` | SCIM (User Provisioning) |

Tokens are stored in the plugin vault (key icon → New variable) and appear here only as a placeholder, e.g. `"{{basic:NAME}}"` or `"{{bearer:NAME}}"`. The scope of each token is defined by the variable in the secrets vault.

## To register a real instance

1. Duplicate this note.
2. Remove the `template` tag (keep `atlassian/instance`).
3. Fill in `url` and the tokens your APIs need (see the table above) — create each token with the key icon → New variable, then reference it here, e.g. `auth_token: "{{basic:MY_TOKEN}}"`.
