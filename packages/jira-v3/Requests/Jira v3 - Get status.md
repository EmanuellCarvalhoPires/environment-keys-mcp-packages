---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-statuses
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/status/{idOrName}"
category: "Workflow statuses"
writes_data: false
tool_note: "[[jira_get_status]]"
---
# Jira v3 - Get status

**Get status** — `GET /rest/api/3/status/{idOrName}`

- Run by the tool [[jira_get_status]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/status/{{param:idOrName}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `idOrName` (path, string, required) — The ID or name of the status.

## Original description

Returns a status. The status must be associated with an active workflow to be returned.

If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable.

This operation can be accessed anonymously.

[Permissions](#permissions) required: *Browse projects* [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.
