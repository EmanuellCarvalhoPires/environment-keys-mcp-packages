---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/server-info
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/serverInfo"
category: "Server info"
writes_data: false
tool_note: "[[jira_get_jira_instance_info]]"
---
# Jira v3 - Get Jira instance info

**Get Jira instance info** — `GET /rest/api/3/serverInfo`

- Run by the tool [[jira_get_jira_instance_info]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/serverInfo
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns information about the Jira instance.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
