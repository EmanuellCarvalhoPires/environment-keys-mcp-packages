---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/properties"
category: "Issue properties"
writes_data: false
tool_note: "[[jira_get_issue_property_keys]]"
---
# Jira v3 - Get issue property keys

**Get issue property keys** — `GET /rest/api/3/issue/{issueIdOrKey}/properties`

- Run by the tool [[jira_get_issue_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The key or ID of the issue.

## Original description

Returns the URLs and keys of an issue's properties.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Property details are only returned where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
