---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/comment/{commentId}/properties/{propertyKey}"
category: "Issue comment properties"
writes_data: true
tool_note: "[[jira_set_comment_property]]"
---
# Jira v3 - Set comment property

**Set comment property** — `PUT /rest/api/3/comment/{commentId}/properties/{propertyKey}`

- Run by the tool [[jira_set_comment_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/comment/{{param:commentId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `commentId` (path, string, required) — The ID of the comment.
- `propertyKey` (path, string, required) — The key of the property. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates or updates the value of a property for a comment. Use this resource to store custom data against a comment.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** either of:

 *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on any comment.
 *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on a comment created by the user.
