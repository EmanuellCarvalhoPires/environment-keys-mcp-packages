---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field/{fieldId}/context/{contextId}/option"
category: "Issue custom field options"
writes_data: true
tool_note: "[[jira_create_custom_field_options_context]]"
---
# Jira v3 - Create custom field options (context)

**Create custom field options (context)** — `POST /rest/api/3/field/{fieldId}/context/{contextId}/option`

- Run by the tool [[jira_create_custom_field_options_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/option
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
      "value": "Scranton"
    },
    {
      "disabled": true,
      "optionId": "10000",
      "value": "Manhattan"
    },
    {
      "disabled": false,
      "value": "The Electric City"
    }
  ]
}
```

## Original description

Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field.

The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
