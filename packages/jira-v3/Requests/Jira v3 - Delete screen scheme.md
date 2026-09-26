---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/screenscheme/{screenSchemeId}"
category: "Screen schemes"
writes_data: true
tool_note: "[[jira_delete_screen_scheme]]"
---
# Jira v3 - Delete screen scheme

**Delete screen scheme** — `DELETE /rest/api/3/screenscheme/{screenSchemeId}`

- Run by the tool [[jira_delete_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/screenscheme/{{param:screenSchemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `screenSchemeId` (path, string, required) — The ID of the screen scheme.

## Original description

Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme.

Only screens schemes used in classic projects can be deleted.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
