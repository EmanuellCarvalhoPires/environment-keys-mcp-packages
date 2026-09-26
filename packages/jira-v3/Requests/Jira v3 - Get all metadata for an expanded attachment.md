---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/attachment/{id}/expand/human"
category: "Issue attachments"
writes_data: false
tool_note: "[[jira_get_all_metadata_for_an_expanded_attachment]]"
---
# Jira v3 - Get all metadata for an expanded attachment

**Get all metadata for an expanded attachment** — `GET /rest/api/3/attachment/{id}/expand/human`

- Run by the tool [[jira_get_all_metadata_for_an_expanded_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/attachment/{{param:id}}/expand/human
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment.

## Original description

Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the attachment itself. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format is supported.

Use this operation to retrieve data that is presented to the user, as this operation returns the metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which only returns the metadata for the attachment's contents.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.
