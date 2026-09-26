---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters"
category: "Field schemes"
writes_data: false
tool_note: "[[jira_get_field_parameters]]"
---
# Jira v3 - Get field parameters

**Get field parameters** — `GET /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters`

- Run by the tool [[jira_get_field_parameters]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}/fields/{{param:fieldId}}/parameters
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — the ID of the field association scheme to retrieve parameters for
- `fieldId` (path, string, required) — the ID of the field

## Original description

Retrieve field association parameters on a field association scheme

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
