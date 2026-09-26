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
method: GET
path: "/rest/api/3/jql/autocompletedata"
category: "JQL"
writes_data: false
tool_note: "[[jira_get_field_reference_data_get]]"
---
# Jira v3 - Get field reference data (GET)

**Get field reference data (GET)** — `GET /rest/api/3/jql/autocompletedata`

- Run by the tool [[jira_get_field_reference_data_get]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/jql/autocompletedata
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
