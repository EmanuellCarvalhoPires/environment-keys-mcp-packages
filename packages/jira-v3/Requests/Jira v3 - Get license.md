---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/license-metrics
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/instance/license"
category: "License metrics"
writes_data: false
tool_note: "[[jira_get_license]]"
---
# Jira v3 - Get license

**Get license** — `GET /rest/api/3/instance/license`

- Run by the tool [[jira_get_license]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/instance/license
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns licensing information about the Jira instance.

**[Permissions](#permissions) required:** None.
