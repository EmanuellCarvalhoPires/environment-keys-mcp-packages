---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}"
category: "Issue custom field options"
writes_data: true
tool_note: "[[jira_delete_custom_field_options_context]]"
---
# Jira v3 - Delete custom field options (context)

**Delete custom field options (context)** — `DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}`

- Run by the tool [[jira_delete_custom_field_options_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/option/{{param:optionId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (path, string, required) — The ID of the context from which an option should be deleted.
- `optionId` (path, string, required) — The ID of the option to delete.

## Original description

Deletes a custom field option.

Options with cascading options cannot be deleted without deleting the cascading options first.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
