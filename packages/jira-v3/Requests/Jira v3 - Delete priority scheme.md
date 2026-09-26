---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/priorityscheme/{schemeId}"
category: "Priority schemes"
writes_data: true
tool_note: "[[jira_delete_priority_scheme]]"
---
# Jira v3 - Delete priority scheme

**Delete priority scheme** — `DELETE /rest/api/3/priorityscheme/{schemeId}`

- Run by the tool [[jira_delete_priority_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/priorityscheme/{{param:schemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `schemeId` (path, string, required) — The priority scheme ID.

## Original description

Deletes a priority scheme.

This operation is only available for priority schemes without any associated projects. Any associated projects must be removed from the priority scheme before this operation can be performed.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
