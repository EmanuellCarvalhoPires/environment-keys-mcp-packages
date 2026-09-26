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
path: "/rest/api/3/search/jql"
category: "Issue search"
writes_data: false
tool_note: "[[jira_search_for_issues_using_jql_enhanced_search_post]]"
---
# Jira v3 - Search for issues using JQL enhanced search (POST)

**Search for issues using JQL enhanced search (POST)** — `POST /rest/api/3/search/jql`

- Run by the tool [[jira_search_for_issues_using_jql_enhanced_search_post]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/search/jql
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned search results. If you need [read-after-write](https://developer.atlassian.com/cloud/jira/platform/search-and-reconcile/) consistency, you can utilize the `reconcileIssues` parameter to ensure stronger consistency assurances. This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issues are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
