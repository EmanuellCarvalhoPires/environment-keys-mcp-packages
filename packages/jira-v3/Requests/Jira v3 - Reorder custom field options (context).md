---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/field/{fieldId}/context/{contextId}/option/move"
category: "Issue custom field options"
writes_data: true
tool_note: "[[jira_reorder_custom_field_options_context]]"
---
# Jira v3 - Reorder custom field options (context)

**Reorder custom field options (context)** — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move`

- Run by the tool [[jira_reorder_custom_field_options_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/option/move
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
  "customFieldOptionIds": [
    "10001",
    "10002"
  ],
  "position": "First"
}
```

## Original description

Changes the order of custom field options or cascading options in a context.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
