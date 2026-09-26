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
path: "/rest/api/3/attachment/content/{id}"
category: "Issue attachments"
writes_data: false
tool_note: "[[jira_get_attachment_content]]"
---
# Jira v3 - Get attachment content

**Get attachment content** — `GET /rest/api/3/attachment/content/{id}`

- Run by the tool [[jira_get_attachment_content]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/attachment/content/{{param:id}}?redirect={{param:redirect}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the attachment.
- `redirect` (query, string, optional) — Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to false to avoid making multiple requests to download the attachment.

## Original description

Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) for details.

To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-thumbnail-id-get).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.
