---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/component/{id}"
category: "Project components"
writes_data: true
tool_note: "[[jira_update_component]]"
---
# Jira v3 - Update component

**Update component** — `PUT /rest/api/3/component/{id}`

- Run by the tool [[jira_update_component]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/component/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the component.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "assigneeType": "PROJECT_LEAD",
  "description": "This is a Jira component",
  "isAssigneeTypeValid": false,
  "leadAccountId": "5b10a2844c20165700ede21g",
  "name": "Component 1"
}
```

## Original description

Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an empty string ("") the component lead is removed.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
