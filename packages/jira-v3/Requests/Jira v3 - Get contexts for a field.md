---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldId}/contexts"
category: "Issue fields"
writes_data: false
tool_note: "[[jira_get_contexts_for_a_field]]"
---
# Jira v3 - Get contexts for a field

**Get contexts for a field** — `GET /rest/api/3/field/{fieldId}/contexts`

- Run by the tool [[jira_get_contexts_for_a_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/contexts?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the field to return contexts for.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get custom field contexts](#api-rest-api-3-field-fieldId-context-get).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
