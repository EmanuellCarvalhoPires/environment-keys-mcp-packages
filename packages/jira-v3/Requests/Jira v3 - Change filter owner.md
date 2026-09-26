---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/filter/{id}/owner"
category: "Filters"
writes_data: true
tool_note: "[[jira_change_filter_owner]]"
---
# Jira v3 - Change filter owner

**Change filter owner** — `PUT /rest/api/3/filter/{id}/owner`

- Run by the tool [[jira_change_filter_owner]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/filter/{{param:id}}/owner
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the filter to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "accountId": "0000-0000-0000-0000"
}
```

## Original description

Changes the owner of the filter.

**[Permissions](#permissions) required:** Permission to access Jira. However, the user must own the filter or have the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
