---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflows/defaultEditor"
category: "Workflows"
writes_data: false
tool_note: "[[jira_get_the_user_s_default_workflow_editor]]"
---
# Jira v3 - Get the user's default workflow editor

**Get the user's default workflow editor** — `GET /rest/api/3/workflows/defaultEditor`

- Run by the tool [[jira_get_the_user_s_default_workflow_editor]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflows/defaultEditor
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Get the user's default workflow editor. This can be either the new editor or the legacy editor.
