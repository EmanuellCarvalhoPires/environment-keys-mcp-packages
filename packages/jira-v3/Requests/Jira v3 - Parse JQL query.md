---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/jql/parse"
category: "JQL"
writes_data: false
tool_note: "[[jira_parse_jql_query]]"
---
# Jira v3 - Parse JQL query

**Parse JQL query** — `POST /rest/api/3/jql/parse`

- Run by the tool [[jira_parse_jql_query]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/parse?validation={{param:validation}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `validation` (query, string, required) — How to validate the JQL query and treat the validation results. Validation options include: strict Returns all errors. If validation fails, the query structure is not returned.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "queries": [
    "summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER startOfMonth(-1M) ORDER BY updated DESC",
    "issue.property[\"spaces here\"].value in (\"Service requests\", Incidents)",
    "invalid query",
    "summary = test",
    "summary in test",
    "project = INVALID",
    "universe = 42"
  ]
}
```

## Original description

Parses and validates JQL queries.

Validation is performed in context of the current user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
