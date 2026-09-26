---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}"
category: "Issue properties"
writes_data: false
tool_note: "[[jira_get_issue_property]]"
---
# Jira v3 - Get issue property

**Get issue property** — `GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`

- Run by the tool [[jira_get_issue_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The key or ID of the issue.
- `propertyKey` (path, string, required) — The key of the property.

## Original description

Returns the key and value of an issue's property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
