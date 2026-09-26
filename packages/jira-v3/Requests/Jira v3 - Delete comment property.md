---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/comment/{commentId}/properties/{propertyKey}"
category: "Issue comment properties"
writes_data: true
tool_note: "[[jira_delete_comment_property]]"
---
# Jira v3 - Delete comment property

**Delete comment property** — `DELETE /rest/api/3/comment/{commentId}/properties/{propertyKey}`

- Run by the tool [[jira_delete_comment_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/comment/{{param:commentId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `commentId` (path, string, required) — The ID of the comment.
- `propertyKey` (path, string, required) — The key of the property.

## Original description

Deletes a comment property.

**[Permissions](#permissions) required:** either of:

 *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from any comment.
 *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from a comment created by the user.
