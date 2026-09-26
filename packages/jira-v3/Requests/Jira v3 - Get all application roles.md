---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/application-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/applicationrole"
category: "Application roles"
writes_data: false
tool_note: "[[jira_get_all_application_roles]]"
---
# Jira v3 - Get all application roles

**Get all application roles** — `GET /rest/api/3/applicationrole`

- Run by the tool [[jira_get_all_application_roles]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/applicationrole
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
