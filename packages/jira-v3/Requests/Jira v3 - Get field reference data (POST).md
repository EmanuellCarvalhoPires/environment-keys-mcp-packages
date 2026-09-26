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
path: "/rest/api/3/jql/autocompletedata"
category: "JQL"
writes_data: false
tool_note: "[[jira_get_field_reference_data_post]]"
---
# Jira v3 - Get field reference data (POST)

**Get field reference data (POST)** — `POST /rest/api/3/jql/autocompletedata`

- Run by the tool [[jira_get_field_reference_data_post]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/autocompletedata
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
  "includeCollapsedFields": true,
  "projectIds": [
    10000,
    10001,
    10002
  ]
}
```

## Original description

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

This operation can filter the custom fields returned by project. Invalid project IDs in `projectIds` are ignored. System fields are always returned.

It can also return the collapsed field for custom fields. Collapsed fields enable searches to be performed across all fields with the same name and of the same field type. For example, the collapsed field `Component - Component[Dropdown]` enables dropdown fields `Component - cf[10061]` and `Component - cf[10062]` to be searched simultaneously.

**[Permissions](#permissions) required:** None.
