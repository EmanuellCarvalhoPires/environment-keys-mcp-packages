---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/search/approximate-count"
category: "Issue search"
writes_data: false
tool_note: "[[jira_count_issues_using_jql]]"
---
# Jira v3 - Count issues using JQL

**Count issues using JQL** — `POST /rest/api/3/search/approximate-count`

- Run by the tool [[jira_count_issues_using_jql]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/search/approximate-count
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "jql": "project = HSP"
}
```

## Original description

Provide an estimated count of the issues that match the [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned output. This endpoint requires JQL to be bounded.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issues are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
