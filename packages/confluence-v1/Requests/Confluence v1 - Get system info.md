---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/settings/systemInfo"
category: "Settings"
writes_data: false
tool_note: "[[confluence_v1_get_system_info]]"
---
# Confluence v1 - Get system info

**Get system info** — `GET /wiki/rest/api/settings/systemInfo`

- Run by the tool [[confluence_v1_get_system_info]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/settings/systemInfo
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the system information for the Confluence Cloud tenant. This
information is used by Atlassian.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
