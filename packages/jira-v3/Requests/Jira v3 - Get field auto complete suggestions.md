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
path: "/rest/api/3/jql/autocompletedata/suggestions"
category: "JQL"
writes_data: false
tool_note: "[[jira_get_field_auto_complete_suggestions]]"
---
# Jira v3 - Get field auto complete suggestions

**Get field auto complete suggestions** — `GET /rest/api/3/jql/autocompletedata/suggestions`

- Run by the tool [[jira_get_field_auto_complete_suggestions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/jql/autocompletedata/suggestions?fieldName={{param:fieldName}}&fieldValue={{param:fieldValue}}&predicateName={{param:predicateName}}&predicateValue={{param:predicateValue}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldName` (query, string, optional) — The name of the field.
- `fieldValue` (query, string, optional) — The partial field item name entered by the user.
- `predicateName` (query, string, optional) — The name of the CHANGED operator predicate for which the suggestions are generated. The valid predicate operators are by, from, and to.
- `predicateValue` (query, string, optional) — The partial predicate item name entered by the user.

## Original description

Returns the JQL search auto complete suggestions for a field.

Suggestions can be obtained by providing:

 *  `fieldName` to get a list of all values for the field.
 *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
 *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
 *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing the text in `predicateValue`.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
