---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/pages/{id}"
category: "Page"
writes_data: true
tool_note: "[[confluence_delete_page]]"
---
# Confluence v2 - Delete page

**Delete page** — `DELETE /pages/{id}`

- Run by the tool [[confluence_delete_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/pages/{{param:id}}?purge={{param:purge}}&draft={{param:draft}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the page to be deleted.
- `purge` (query, string, optional) — If attempting to purge the page.
- `draft` (query, string, optional) — If attempting to delete a page that is a draft.

## Original description

Delete a page by id.

By default this will delete pages that are non-drafts. To delete a page that is a draft, the endpoint must be called on a 
draft with the following param `draft=true`. Discarded drafts are not sent to the trash and are permanently deleted.

Deleting a page moves the page to the trash, where it can be restored later. To permanently delete a page (or "purge" it),
the endpoint must be called on a **trashed** page with the following param `purge=true`.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
Permission to view the page and its corresponding space.
Permission to delete pages in the space.
[`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
