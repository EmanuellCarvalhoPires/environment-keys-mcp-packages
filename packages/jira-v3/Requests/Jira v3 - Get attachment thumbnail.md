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
path: "/rest/api/3/attachment/thumbnail/{id}"
category: "Issue attachments"
writes_data: false
tool_note: "[[jira_get_attachment_thumbnail]]"
---
# Jira v3 - Get attachment thumbnail

**Get attachment thumbnail** — `GET /rest/api/3/attachment/thumbnail/{id}`

- Run by the tool [[jira_get_attachment_thumbnail]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/attachment/thumbnail/{{param:id}}?redirect={{param:redirect}}&fallbackToDefault={{param:fallbackToDefault}}&width={{param:width}}&height={{param:height}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the attachment.
- `redirect` (query, string, optional) — Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to false to avoid making multiple requests to download the attachment.
- `fallbackToDefault` (query, string, optional) — Whether a default thumbnail is returned when the requested thumbnail is not found.
- `width` (query, string, optional) — The maximum width to scale the thumbnail to.
- `height` (query, string, optional) — The maximum height to scale the thumbnail to.

## Original description

Returns the thumbnail of an attachment.

To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-id-get).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.
