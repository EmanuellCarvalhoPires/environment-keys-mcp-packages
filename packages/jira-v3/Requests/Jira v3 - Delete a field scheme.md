---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/config/fieldschemes/{id}"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_delete_a_field_scheme]]"
---
# Jira v3 - Delete a field scheme

**Delete a field scheme** — `DELETE /rest/api/3/config/fieldschemes/{id}`

- Run by the tool [[jira_delete_a_field_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the field association scheme to delete.

## Original description

Delete a specified field association scheme

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
