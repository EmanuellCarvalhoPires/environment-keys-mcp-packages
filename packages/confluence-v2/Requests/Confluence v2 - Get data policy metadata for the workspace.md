---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/data-policies
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/data-policies/metadata"
category: "Data Policies"
writes_data: false
tool_note: "[[confluence_get_data_policy_metadata_for_the_workspace]]"
---
# Confluence v2 - Get data policy metadata for the workspace

**Get data policy metadata for the workspace** — `GET /data-policies/metadata`

- Run by the tool [[confluence_get_data_policy_metadata_for_the_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/data-policies/metadata
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns data policy metadata for the workspace.

**[Permissions](#permissions) required:**
Only apps can make this request.
Permission to access the Confluence site ('Can use' global permission).
