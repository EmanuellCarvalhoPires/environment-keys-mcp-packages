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
path: "/rest/api/3/field/{id}/trash"
category: "Issue fields"
writes_data: true
tool_note: "[[jira_move_custom_field_to_trash]]"
---
# Jira v3 - Move custom field to trash

**Move custom field to trash** — `POST /rest/api/3/field/{id}/trash`

- Run by the tool [[jira_move_custom_field_to_trash]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:id}}/trash
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of a custom field.

## Original description

Moves a custom field to trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
