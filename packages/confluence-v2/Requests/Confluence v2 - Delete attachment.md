---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/attachments/{id}"
category: "Attachment"
writes_data: true
tool_note: "[[confluence_delete_attachment]]"
---
# Confluence v2 - Delete attachment

**Delete attachment** — `DELETE /attachments/{id}`

- Run by the tool [[confluence_delete_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/attachments/{{param:id}}?purge={{param:purge}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the attachment to be deleted.
- `purge` (query, string, optional) — If attempting to purge the attachment.

## Original description

Delete an attachment by id.

Deleting an attachment moves the attachment to the trash, where it can be restored later. To permanently delete an attachment (or "purge" it),
the endpoint must be called on a **trashed** attachment with the following param `purge=true`.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
Permission to view the container of the attachment.
Permission to delete attachments in the space.
[`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
