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
path: "/rest/api/3/field/{fieldId}/context/{contextId}/option"
category: "Issue custom field options"
writes_data: true
tool_note: "[[jira_update_custom_field_options_context]]"
---
# Jira v3 - Update custom field options (context)

**Update custom field options (context)** — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/option`

- Run by the tool [[jira_update_custom_field_options_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/option
Authorization: {{service.auth_token}}
Accept: application/json
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
  "options": [
    {
      "disabled": false,
      "id": "10001",
      "value": "Scranton"
    },
    {
      "disabled": true,
      "id": "10002",
      "value": "Manhattan"
    },
    {
      "disabled": false,
      "id": "10003",
      "value": "The Electric City"
    }
  ]
}
```

## Original description

Updates the options of a custom field.

If any of the options are not found, no options are updated. Options where the values in the request match the current values aren't updated and aren't reported in the response.

Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
