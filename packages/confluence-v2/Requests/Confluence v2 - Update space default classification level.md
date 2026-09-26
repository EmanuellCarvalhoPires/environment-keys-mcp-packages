---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/spaces/{id}/classification-level/default"
category: "Classification Level"
writes_data: true
tool_note: "[[confluence_update_space_default_classification_level]]"
---
# Confluence v2 - Update space default classification level

**Update space default classification level** — `PUT /spaces/{id}/classification-level/default`

- Run by the tool [[confluence_update_space_default_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/spaces/{{param:id}}/classification-level/default
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the space for which default classification level should be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update the [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/) 
for a specific space.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
Permission to access the Confluence site ('Can use' global permission) and
[`manage/space`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
