---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-expressions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/expression/analyse"
category: "Jira expressions"
writes_data: false
tool_note: "[[jira_analyse_jira_expression]]"
---
# Jira v3 - Analyse Jira expression

**Analyse Jira expression** — `POST /rest/api/3/expression/analyse`

- Run by the tool [[jira_analyse_jira_expression]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/expression/analyse?check={{param:check}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `check` (query, string, optional) — The check to perform: syntax Each expression's syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression's length. type EXPERIMENTAL.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "contextVariables": {
    "listOfStrings": "List<String>",
    "record": "{ a: Number, b: String }",
    "value": "User"
  },
  "expressions": [
    "issues.map(issue => issue.properties['property_key'])"
  ]
}
```

## Original description

Analyses and validates Jira expressions.

As an experimental feature, this operation can also attempt to type-check the expressions.

Learn more about Jira expressions in the [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

**[Permissions](#permissions) required**: None.
