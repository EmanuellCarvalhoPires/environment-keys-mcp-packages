---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetype/{id}/alternatives"
category: "Issue types"
writes_data: false
tool_note: "[[jira_get_alternative_issue_types]]"
---
# Jira v3 - Get alternative issue types

**Get alternative issue types** — `GET /rest/api/3/issuetype/{id}/alternatives`

- Run by the tool [[jira_get_alternative_issue_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetype/{{param:id}}/alternatives
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the issue type.

## Original description

Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
