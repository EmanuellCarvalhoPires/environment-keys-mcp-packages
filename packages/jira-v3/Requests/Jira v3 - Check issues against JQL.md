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
path: "/rest/api/3/jql/match"
category: "Issue search"
writes_data: false
tool_note: "[[jira_check_issues_against_jql]]"
---
# Jira v3 - Check issues against JQL

**Check issues against JQL** — `POST /rest/api/3/jql/match`

- Run by the tool [[jira_check_issues_against_jql]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/match
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
  "issueIds": [
    10001,
    1000,
    10042
  ],
  "jqls": [
    "project = FOO",
    "issuetype = Bug",
    "summary ~ \"some text\" AND project in (FOO, BAR)"
  ]
}
```

## Original description

Checks whether one or more issues would be returned by one or more JQL queries. Up to 10 JQL queries can be specified and up to 50 issue IDs included in the request.

**[Permissions](#permissions) required:** None, however, issues are only matched against JQL queries where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
