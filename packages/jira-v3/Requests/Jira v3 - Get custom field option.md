---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/customFieldOption/{id}"
category: "Issue custom field options"
writes_data: false
tool_note: "[[jira_get_custom_field_option]]"
---
# Jira v3 - Get custom field option

**Get custom field option** — `GET /rest/api/3/customFieldOption/{id}`

- Run by the tool [[jira_get_custom_field_option]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/customFieldOption/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the custom field option.

## Original description

Returns a custom field option. For example, an option in a select list.

Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The custom field option is returned as follows:

 *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.
