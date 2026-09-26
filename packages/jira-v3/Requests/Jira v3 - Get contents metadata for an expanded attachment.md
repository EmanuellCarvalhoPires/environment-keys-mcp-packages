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
path: "/rest/api/3/attachment/{id}/expand/raw"
category: "Issue attachments"
writes_data: false
tool_note: "[[jira_get_contents_metadata_for_an_expanded_attachment]]"
---
# Jira v3 - Get contents metadata for an expanded attachment

**Get contents metadata for an expanded attachment** — `GET /rest/api/3/attachment/{id}/expand/raw`

- Run by the tool [[jira_get_contents_metadata_for_an_expanded_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/attachment/{{param:id}}/expand/raw
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment.

## Original description

Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported.

Use this operation if you are processing the data without presenting it to the user, as this operation only returns the metadata for the contents of the attachment. Otherwise, to retrieve data to present to the user, use [ Get all metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-human-get) which also returns the metadata for the attachment itself, such as the attachment's ID and name.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.
