---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/custom-content/{id}"
category: "Custom Content"
writes_data: true
tool_note: "[[confluence_delete_custom_content]]"
---
# Confluence v2 - Delete custom content

**Delete custom content** — `DELETE /custom-content/{id}`

- Run by the tool [[confluence_delete_custom_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/custom-content/{{param:id}}?purge={{param:purge}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the custom content to be deleted.
- `purge` (query, string, optional) — If attempting to purge the custom content.

## Original description

Delete a custom content by id.

Deleting a custom content will either move it to the trash or permanently delete it (purge it), depending on the apiSupport.
To permanently delete a **trashed** custom content, the endpoint must be called with the following param `purge=true`.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
Permission to view the content of the page or blogpost and its corresponding space.
Permission to delete custom content in the space.
[`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
