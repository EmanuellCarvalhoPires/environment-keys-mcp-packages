---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/custom-content"
category: "Custom Content"
writes_data: true
tool_note: "[[confluence_create_custom_content]]"
---
# Confluence v2 - Create custom content

**Create custom content** — `POST /custom-content`

- Run by the tool [[confluence_create_custom_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/custom-content
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new custom content in the given space, page, blogpost or other custom content.

Only one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is required in the request body.
**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space. Permission to create custom content in the space.
