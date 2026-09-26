---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/space/{spaceKey}"
category: "Space"
writes_data: true
tool_note: "[[confluence_v1_delete_space]]"
---
# Confluence v1 - Delete space

**Delete space** — `DELETE /wiki/rest/api/space/{spaceKey}`

- Run by the tool [[confluence_v1_delete_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to delete.

## Original description

Permanently deletes a space without sending it to the trash. Note, the space will be deleted in a long running task.
Therefore, the space may not be deleted yet when this method has
returned. Clients should poll the status link that is returned in the
response until the task completes.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
