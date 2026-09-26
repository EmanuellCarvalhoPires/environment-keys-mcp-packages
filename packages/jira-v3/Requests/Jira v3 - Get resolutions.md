---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/resolution"
category: "Issue resolutions"
writes_data: false
tool_note: "[[jira_get_resolutions]]"
---
# Jira v3 - Get resolutions

**Get resolutions** — `GET /rest/api/3/resolution`

- Run by the tool [[jira_get_resolutions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/resolution
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns a list of all issue resolution values.

**[Permissions](#permissions) required:** Permission to access Jira.
