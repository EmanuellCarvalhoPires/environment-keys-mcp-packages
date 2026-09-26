---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/config/fieldschemes/{id}/fields"
category: "Field schemes"
writes_data: false
tool_note: "[[jira_search_field_scheme_fields]]"
---
# Jira v3 - Search field scheme fields

**Search field scheme fields** — `GET /rest/api/3/config/fieldschemes/{id}/fields`

- Run by the tool [[jira_search_field_scheme_fields]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}/fields?startAt={{param:startAt}}&maxResults={{param:maxResults}}&fieldId={{param:fieldId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The scheme ID to search for child fields
- `startAt` (query, string, optional) — The starting index of the returned fields. Base index: 0.
- `maxResults` (query, string, optional) — The maximum number of fields to return per page, maximum allowed value is 100.
- `fieldId` (query, string, optional) — The field IDs to filter by, if empty then all fields belonging to a field association scheme will be returned

## Original description

Search for fields belonging to a given field association scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
