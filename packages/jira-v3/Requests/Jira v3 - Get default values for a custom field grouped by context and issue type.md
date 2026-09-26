---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldId}/context/defaultValues"
category: "Issue custom field contexts"
writes_data: false
tool_note: "[[jira_get_default_values_for_a_custom_field_grouped_by_context_an]]"
---
# Jira v3 - Get default values for a custom field grouped by context and issue type

**Get default values for a custom field grouped by context and issue type** — `GET /rest/api/3/field/{fieldId}/context/defaultValues`

- Run by the tool [[jira_get_default_values_for_a_custom_field_grouped_by_context_an]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/defaultValues?contextId={{param:contextId}}&issueTypeId={{param:issueTypeId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field, for example customfield\10000.
- `contextId` (query, string, optional) — The IDs of the contexts to return default values for. If omitted, default values for every context the custom field has are returned.
- `issueTypeId` (query, string, optional) — The IDs of the issue types to restrict the returned per-issue-type default values to. If omitted, default values for every issue type are returned.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a paginated list of default values grouped by custom field context.

Each returned `ContextDefaultValuesBean` has a `contextId` and a `defaultValues` list of `IssueTypeDefaultValueBean` entries - one per issue-type-scoped default value configured for the context. An entry with `"isAnyIssueType": true` represents the catch-all default that applies to every issue type covered by the context that is not covered by a more specific entry; a non-null `issueTypeId` represents a default that only applies to that issue type.

For contexts that have not been converted to the multiple-contexts data model, exactly one entry is returned per context with `isAnyIssueType=true`. For converted contexts, one entry is returned per configured per-issue-type default.

The value object on each entry is the same polymorphic `CustomFieldContextDefaultValueBean` exposed by the deprecated `GET /defaultValue` endpoint - its concrete subtype depends on the custom field's type (see the list of supported types on that endpoint).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
