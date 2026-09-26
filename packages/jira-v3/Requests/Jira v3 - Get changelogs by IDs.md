---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/changelog/list"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_changelogs_by_ids]]"
---
# Jira v3 - Get changelogs by IDs

**Get changelogs by IDs** — `POST /rest/api/3/issue/{issueIdOrKey}/changelog/list`

- Run by the tool [[jira_get_changelogs_by_ids]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/changelog/list
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "changelogIds": [
    10001,
    10002
  ]
}
```

## Original description

Returns changelogs for an issue specified by a list of changelog IDs.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
