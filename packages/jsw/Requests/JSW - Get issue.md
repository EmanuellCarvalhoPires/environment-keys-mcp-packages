---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/issue/{issueIdOrKey}"
category: "Issue"
writes_data: false
tool_note: "[[jsw_get_issue]]"
---
# JSW - Get issue

**Get issue** — `GET /rest/agile/1.0/issue/{issueIdOrKey}`

- Run by the tool [[jsw_get_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/issue/{{param:issueIdOrKey}}?fields={{param:fields}}&expand={{param:expand}}&updateHistory={{param:updateHistory}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the requested issue.
- `fields` (query, string, optional) — The list of fields to return for each issue. By default, all navigable and Agile fields are returned.
- `expand` (query, string, optional) — A comma-separated list of the parameters to expand.
- `updateHistory` (query, string, optional) — A boolean indicating whether the issue retrieved by this method should be added to the current user's issue history

## Original description

Returns a single issue, for a given issue ID or issue key. Issues returned from this resource include Agile fields, like sprint, closedSprints, flagged, and epic.
