---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-links
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issueLink/{linkId}"
category: "Issue links"
writes_data: true
tool_note: "[[jira_delete_issue_link]]"
---
# Jira v3 - Delete issue link

**Delete issue link** — `DELETE /rest/api/3/issueLink/{linkId}`

- Run by the tool [[jira_delete_issue_link]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issueLink/{{param:linkId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `linkId` (path, string, required) — The ID of the issue link.

## Original description

Deletes an issue link.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  Browse project [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues in the link.
 *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one of the projects containing issues in the link.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.
