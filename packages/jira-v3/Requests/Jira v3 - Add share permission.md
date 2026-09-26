---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/filter/{id}/permission"
category: "Filter sharing"
writes_data: true
tool_note: "[[jira_add_share_permission]]"
---
# Jira v3 - Add share permission

**Add share permission** — `POST /rest/api/3/filter/{id}/permission`

- Run by the tool [[jira_add_share_permission]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/filter/{{param:id}}/permission
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the filter.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "groupname": "jira-administrators",
  "rights": 1,
  "type": "group"
}
```

## Original description

Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter.

Be aware that this operation uses different objects for updating share permissions compared to [Update filter](#api-rest-api-3-filter-id-put).

**[Permissions](#permissions) required:** *Share dashboards and filters* [global permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.
