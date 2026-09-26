---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/field/{fieldId}/context/{contextId}"
category: "Issue custom field contexts"
writes_data: true
tool_note: "[[jira_delete_custom_field_context]]"
---
# Jira v3 - Delete custom field context

**Delete custom field context** — `DELETE /rest/api/3/field/{fieldId}/context/{contextId}`

- Run by the tool [[jira_delete_custom_field_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (path, string, required) — The ID of the context.

## Original description

Deletes a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).

This API will not allow removing the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
