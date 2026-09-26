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
path: "/rest/api/3/attachment/meta"
category: "Issue attachments"
writes_data: false
tool_note: "[[jira_get_jira_attachment_settings]]"
---
# Jira v3 - Get Jira attachment settings

**Get Jira attachment settings** — `GET /rest/api/3/attachment/meta`

- Run by the tool [[jira_get_jira_attachment_settings]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/attachment/meta
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed.

Note that there are also [project permissions](https://confluence.atlassian.com/x/yodKLg) that restrict whether users can create and delete attachments.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
