---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/footer-comments"
category: "Comment"
writes_data: true
tool_note: "[[confluence_create_footer_comment]]"
---
# Confluence v2 - Create footer comment

**Create footer comment** — `POST /footer-comments`

- Run by the tool [[confluence_create_footer_comment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/footer-comments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a footer comment.

The footer comment can be made against several locations: 
- at the top level (specifying pageId or blogPostId in the request body)
- as a reply (specifying parentCommentId in the request body)
- against an attachment (note: this is different than the comments added via the attachment properties page on the UI, which are referred to as version comments)
- against a custom content

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
