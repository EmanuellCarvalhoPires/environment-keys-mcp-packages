---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field/{fieldId}/context/{contextId}/project/remove"
category: "Issue custom field contexts"
writes_data: true
tool_note: "[[jira_remove_custom_field_context_from_projects]]"
---
# Jira v3 - Remove custom field context from projects

**Remove custom field context from projects** — `POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove`

- Run by the tool [[jira_remove_custom_field_context_from_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/project/remove
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

Removes a custom field context from projects.

A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects.

If any project in the request is not assigned to the context, or the operation would result in two global contexts for the field, the operation fails.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
