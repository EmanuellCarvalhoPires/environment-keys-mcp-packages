---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-navigator-settings
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/settings/columns"
category: "Issue navigator settings"
writes_data: false
tool_note: "[[jira_get_issue_navigator_default_columns]]"
---
# Jira v3 - Get issue navigator default columns

**Get issue navigator default columns** — `GET /rest/api/3/settings/columns`

- Run by the tool [[jira_get_issue_navigator_default_columns]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/settings/columns
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the default issue navigator columns.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
