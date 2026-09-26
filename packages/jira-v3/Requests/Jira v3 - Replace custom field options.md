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
path: "/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue"
category: "Issue custom field options"
writes_data: true
tool_note: "[[jira_replace_custom_field_options]]"
---
# Jira v3 - Replace custom field options

**Replace custom field options** — `DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue`

- Run by the tool [[jira_replace_custom_field_options]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/option/{{param:optionId}}/issue?replaceWith={{param:replaceWith}}&jql={{param:jql}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (path, string, required) — The ID of the context.
- `optionId` (path, string, required) — The ID of the option to be deselected.
- `replaceWith` (query, string, optional) — The ID of the option that will replace the currently selected option.
- `jql` (query, string, optional) — A JQL query that specifies the issues to be updated. For example, project=10000.

## Original description

Replaces the options of a custom field.

Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect or Forge apps.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
