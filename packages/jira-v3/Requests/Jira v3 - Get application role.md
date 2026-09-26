---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/application-roles
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/applicationrole/{key}"
category: "Application roles"
writes_data: false
tool_note: "[[jira_get_application_role]]"
---
# Jira v3 - Get application role

**Get application role** — `GET /rest/api/3/applicationrole/{key}`

- Run by the tool [[jira_get_application_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/applicationrole/{{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `key` (path, string, required) — The key of the application role. Use the Get all application roles operation to get the key for each application role.

## Original description

Returns an application role.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
