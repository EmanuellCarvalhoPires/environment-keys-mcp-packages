---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces/{id}/classification-level/default"
category: "Classification Level"
writes_data: false
tool_note: "[[confluence_get_space_default_classification_level]]"
---
# Confluence v2 - Get space default classification level

**Get space default classification level** — `GET /spaces/{id}/classification-level/default`

- Run by the tool [[confluence_get_space_default_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:id}}/classification-level/default
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the space for which default classification level should be returned.

## Original description

Returns the [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/) 
for a specific space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission) and permission to view the space.
