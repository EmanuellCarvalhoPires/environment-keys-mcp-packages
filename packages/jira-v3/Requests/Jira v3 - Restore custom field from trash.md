---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field/{id}/restore"
category: "Issue fields"
writes_data: true
tool_note: "[[jira_restore_custom_field_from_trash]]"
---
# Jira v3 - Restore custom field from trash

**Restore custom field from trash** — `POST /rest/api/3/field/{id}/restore`

- Run by the tool [[jira_restore_custom_field_from_trash]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:id}}/restore
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of a custom field.

## Original description

Restores a custom field from trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
