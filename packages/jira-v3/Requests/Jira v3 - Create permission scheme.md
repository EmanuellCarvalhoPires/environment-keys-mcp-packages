---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/permissionscheme"
category: "Permission schemes"
writes_data: true
tool_note: "[[jira_create_permission_scheme]]"
---
# Jira v3 - Create permission scheme

**Create permission scheme** — `POST /rest/api/3/permissionscheme`

- Run by the tool [[jira_create_permission_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/permissionscheme?expand={{param:expand}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "description",
  "name": "Example permission scheme",
  "permissions": [
    {
      "holder": {
        "parameter": "jira-core-users",
        "type": "group",
        "value": "ca85fac0-d974-40ca-a615-7af99c48d24f"
      },
      "permission": "ADMINISTER_PROJECTS"
    }
  ]
}
```

## Original description

Creates a new permission scheme. You can create a permission scheme with or without defining a set of permission grants.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
