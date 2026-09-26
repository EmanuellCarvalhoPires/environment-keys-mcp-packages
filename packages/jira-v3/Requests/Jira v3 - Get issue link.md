---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-links
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issueLink/{linkId}"
category: "Issue links"
writes_data: false
tool_note: "[[jira_get_issue_link]]"
---
# Jira v3 - Get issue link

**Get issue link** — `GET /rest/api/3/issueLink/{linkId}`

- Run by the tool [[jira_get_issue_link]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issueLink/{{param:linkId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `linkId` (path, string, required) — The ID of the issue link.

## Original description

Returns an issue link.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.
