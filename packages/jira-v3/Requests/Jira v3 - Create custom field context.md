---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field/{fieldId}/context"
category: "Issue custom field contexts"
writes_data: true
tool_note: "[[jira_create_custom_field_context]]"
---
# Jira v3 - Create custom field context

**Create custom field context** — `POST /rest/api/3/field/{fieldId}/context`

- Run by the tool [[jira_create_custom_field_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:fieldId}}/context
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "A context used to define the custom field options for bugs.",
  "issueTypeIds": [
    "10010"
  ],
  "name": "Bug fields context",
  "projectIds": []
}
```

## Original description

Creates a custom field context.

If `projectIds` is empty, a global context is created. A global context is one that applies to all project. If `issueTypeIds` is empty, the context applies to all issue types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
