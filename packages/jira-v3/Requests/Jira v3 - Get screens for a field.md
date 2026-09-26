---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldId}/screens"
category: "Screens"
writes_data: false
tool_note: "[[jira_get_screens_for_a_field]]"
---
# Jira v3 - Get screens for a field

**Get screens for a field** — `GET /rest/api/3/field/{fieldId}/screens`

- Run by the tool [[jira_get_screens_for_a_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/screens?startAt={{param:startAt}}&maxResults={{param:maxResults}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the field to return screens for.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `expand` (query, string, optional) — Use expand to include additional information about screens in the response. This parameter accepts tab which returns details about the screen tabs the field is used in.

## Original description

Returns a [paginated](#pagination) list of the screens a field is used in.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
