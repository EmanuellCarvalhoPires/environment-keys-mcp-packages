---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/field/{fieldId}/context/{contextId}/project"
category: "Issue custom field contexts"
writes_data: true
tool_note: "[[jira_assign_custom_field_context_to_projects]]"
---
# Jira v3 - Assign custom field context to projects

**Assign custom field context to projects** — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/project`

- Run by the tool [[jira_assign_custom_field_context_to_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/project
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (path, string, required) — The ID of the context.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "projectIds": [
    "10001",
    "10005",
    "10006"
  ]
}
```

## Original description

Assigns a custom field context to projects.

If any project in the request is assigned to any context of the custom field, the operation fails.

This API will not allow adding projects to the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
