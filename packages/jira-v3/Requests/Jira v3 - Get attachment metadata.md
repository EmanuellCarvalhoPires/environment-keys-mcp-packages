---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/attachment/{id}"
category: "Issue attachments"
writes_data: false
tool_note: "[[jira_get_attachment_metadata]]"
---
# Jira v3 - Get attachment metadata

**Get attachment metadata** — `GET /rest/api/3/attachment/{id}`

- Run by the tool [[jira_get_attachment_metadata]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/attachment/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment.

## Original description

Returns the metadata for an attachment. Note that the attachment itself is not returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.
