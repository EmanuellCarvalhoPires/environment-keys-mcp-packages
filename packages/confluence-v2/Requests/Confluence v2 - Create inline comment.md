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
path: "/inline-comments"
category: "Comment"
writes_data: true
tool_note: "[[confluence_create_inline_comment]]"
---
# Confluence v2 - Create inline comment

**Create inline comment** — `POST /inline-comments`

- Run by the tool [[confluence_create_inline_comment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/inline-comments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create an inline comment. This can be at the top level (specifying pageId or blogPostId in the request body)
or as a reply (specifying parentCommentId in the request body). Note the inlineCommentProperties object in the
request body is used to select the text the inline comment should be tied to. This is what determines the text 
highlighting when viewing a page in Confluence.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
