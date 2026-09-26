---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/issue/rank"
category: "Issue"
writes_data: true
tool_note: "[[jsw_rank_issues]]"
---
# JSW - Rank issues

**Rank issues** — `PUT /rest/agile/1.0/issue/rank`

- Run by the tool [[jsw_rank_issues]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/issue/rank
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issues": [
    "PR-1",
    "10001",
    "PR-3"
  ],
  "rankBeforeIssue": "PR-4",
  "rankCustomFieldId": 10521
}
```

## Original description

Moves (ranks) issues before or after a given issue. At most 50 issues may be ranked at once.

This operation may fail for some issues, although this will be rare. In that case the 207 status code is returned for the whole response and detailed information regarding each issue is available in the response body.

If rankCustomFieldId is not defined, the default rank field will be used.
