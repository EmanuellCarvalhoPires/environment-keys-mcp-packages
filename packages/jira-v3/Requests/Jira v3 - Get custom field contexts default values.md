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
path: "/rest/api/3/field/{fieldId}/context/defaultValue"
category: "Issue custom field contexts"
writes_data: false
tool_note: "[[jira_get_custom_field_contexts_default_values]]"
---
# Jira v3 - Get custom field contexts default values

**Get custom field contexts default values** — `GET /rest/api/3/field/{fieldId}/context/defaultValue`

- Run by the tool [[jira_get_custom_field_contexts_default_values]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/defaultValue?contextId={{param:contextId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field, for example customfield\10000.
- `contextId` (query, string, optional) — The IDs of the contexts.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is returned.  
The returned object depends on type of the custom field:

 *  `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
 *  `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
 *  `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons.
 *  `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes.
 *  `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists.
 *  `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
 *  `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
 *  `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers.
 *  `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers.
 *  `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
 *  `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
 *  `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
 *  `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
 *  `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
 *  `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
 *  `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
 *  `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers.
 *  `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers.

Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

 *  `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields.
 *  `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields.
 *  `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields.
 *  `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields.
 *  `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
 *  `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields.
 *  `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields.
 *  `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
 *  `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields.

**Deprecated:** This API is deprecated and will be removed in October 2026. A replacement API that supports multiple default values per issue type within a context is coming soon. See the deprecation notice [CHANGE-3082](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3082) for more details.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
