---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldId}/context/{contextId}/option"
category: "Issue custom field options"
writes_data: false
tool_note: "[[jira_get_custom_field_options_context]]"
---
# Jira v3 - Get custom field options (context)

**Get custom field options (context)** — `GET /rest/api/3/field/{fieldId}/context/{contextId}/option`

- Run by the tool [[jira_get_custom_field_options_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/option?optionId={{param:optionId}}&onlyOptions={{param:onlyOptions}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (path, string, required) — The ID of the context.
- `optionId` (query, string, optional) — The ID of the option.
- `onlyOptions` (query, string, optional) — Whether only options are returned.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). *Edit Workflow* [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)
