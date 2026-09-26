---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/config/fieldschemes/{id}"
category: "Field schemes"
writes_data: false
tool_note: "[[jira_get_field_scheme]]"
---
# Jira v3 - Get field scheme

**Get field scheme** — `GET /rest/api/3/config/fieldschemes/{id}`

- Run by the tool [[jira_get_field_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The scheme id to fetch

## Original description

Endpoint for fetching a field association scheme by its ID

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
