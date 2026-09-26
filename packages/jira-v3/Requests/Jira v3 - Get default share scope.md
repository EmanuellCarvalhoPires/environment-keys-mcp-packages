---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/filter/defaultShareScope"
category: "Filter sharing"
writes_data: false
tool_note: "[[jira_get_default_share_scope]]"
---
# Jira v3 - Get default share scope

**Get default share scope** — `GET /rest/api/3/filter/defaultShareScope`

- Run by the tool [[jira_get_default_share_scope]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/filter/defaultShareScope
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the default sharing settings for new filters and dashboards for a user.

**[Permissions](#permissions) required:** Permission to access Jira.
