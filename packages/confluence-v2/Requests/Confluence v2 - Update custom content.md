---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/custom-content/{id}"
category: "Custom Content"
writes_data: true
tool_note: "[[confluence_update_custom_content]]"
---
# Confluence v2 - Update custom content

**Update custom content** — `PUT /custom-content/{id}`

- Run by the tool [[confluence_update_custom_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/custom-content/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the custom content to be updated. If you don't know the custom content ID, use Get Custom Content by Type and filter the results.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a custom content by id.
At most one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is allowed in the request body.
Note that if `spaceId` is specified, it must be the same as the `spaceId` used for creating the custom content
as moving custom content to a different space is not supported.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space. Permission to update custom content in the space.
