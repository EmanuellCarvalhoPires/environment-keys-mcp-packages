---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/jql/sanitize"
category: "JQL"
writes_data: false
tool_note: "[[jira_sanitize_jql_queries]]"
---
# Jira v3 - Sanitize JQL queries

**Sanitize JQL queries** — `POST /rest/api/3/jql/sanitize`

- Run by the tool [[jira_sanitize_jql_queries]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/sanitize
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
  "queries": [
    {
      "query": "project = 'Sample project'"
    },
    {
      "accountId": "5b10ac8d82e05b22cc7d4ef5",
      "query": "project = 'Sample project'"
    },
    {
      "accountId": "cda2aa1395ac195d951b3387",
      "query": "project = 'Sample project'"
    },
    {
      "accountId": "5b10ac8d82e05b22cc7d4ef5",
      "query": "invalid query"
    }
  ]
}
```

## Original description

Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity.

For example, if the query contains the clause *project = 'Secret project'*, and a user does not have browse permission for the project "Secret project", the sanitized query replaces the clause with *project = 12345"* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user.

Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-api-3-jql-sanitize-post).

Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
