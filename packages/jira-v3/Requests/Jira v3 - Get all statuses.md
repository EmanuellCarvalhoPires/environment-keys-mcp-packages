---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-statuses
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/status"
category: "Workflow statuses"
writes_data: false
tool_note: "[[jira_get_all_statuses]]"
---
# Jira v3 - Get all statuses

**Get all statuses** — `GET /rest/api/3/status`

- Run by the tool [[jira_get_all_statuses]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/status
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns a list of all statuses associated with active workflows.

This operation can be accessed anonymously.

[Permissions](#permissions) required: *Browse projects* [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.
