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
path: "/rest/api/3/jql/pdcleaner"
category: "JQL"
writes_data: false
tool_note: "[[jira_convert_user_identifiers_to_account_ids_in_jql_queries]]"
---
# Jira v3 - Convert user identifiers to account IDs in JQL queries

**Convert user identifiers to account IDs in JQL queries** — `POST /rest/api/3/jql/pdcleaner`

- Run by the tool [[jira_convert_user_identifiers_to_account_ids_in_jql_queries]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/pdcleaner
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
  "queryStrings": [
    "assignee = mia",
    "issuetype = Bug AND assignee in (mia) AND reporter in (alana) order by lastViewed DESC"
  ]
}
```

## Original description

Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.

You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/).

**[Permissions](#permissions) required:** Permission to access Jira.
