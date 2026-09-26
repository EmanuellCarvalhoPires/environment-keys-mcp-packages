---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-watchers
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/watching"
category: "Issue watchers"
writes_data: false
tool_note: "[[jira_get_is_watching_issue_bulk]]"
---
# Jira v3 - Get is watching issue bulk

**Get is watching issue bulk** — `POST /rest/api/3/issue/watching`

- Run by the tool [[jira_get_is_watching_issue_bulk]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/watching
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
    "10001",
    "10002",
    "10005"
  ]
}
```

## Original description

Returns, for the user, details of the watched status of issues from a list. If an issue ID is invalid, the returned watched status is `false`.

This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
