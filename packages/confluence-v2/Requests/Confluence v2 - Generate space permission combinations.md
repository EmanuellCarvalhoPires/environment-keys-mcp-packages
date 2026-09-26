---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/action
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/space-permissions/transition/combinations"
category: "Space Permission Transition"
writes_data: true
tool_note: "[[confluence_generate_space_permission_combinations]]"
---
# Confluence v2 - Generate space permission combinations

**Generate space permission combinations** — `POST /space-permissions/transition/combinations`

- Run by the tool [[confluence_generate_space_permission_combinations]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/space-permissions/transition/combinations
Authorization: {{service.auth_token}}
```

## Original description

Submits a task to refresh the space permission combinations in the database, which identifies
all unique permission combinations across the site. This provides permission combination IDs
that can be used with the assign-roles and remove-access endpoints.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a Confluence administrator.
