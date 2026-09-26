---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/attachment/{id}"
category: "Issue attachments"
writes_data: true
tool_note: "[[jira_delete_attachment]]"
---
# Jira v3 - Delete attachment

**Delete attachment** — `DELETE /rest/api/3/attachment/{id}`

- Run by the tool [[jira_delete_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/attachment/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the attachment.

## Original description

Deletes an attachment from an issue.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the project holding the issue containing the attachment:

 *  *Delete own attachments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by the calling user.
 *  *Delete all attachments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by any user.
