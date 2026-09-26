---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options-apps
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/field/{fieldKey}/option/{optionId}"
category: "Issue custom field options (apps)"
writes_data: true
---
# Jira v3 - Delete issue field option

**Delete issue field option** — `DELETE /rest/api/3/field/{fieldKey}/option/{optionId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Delete issue field option"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/field/{{param:fieldKey}}/option/{{param:optionId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldKey` (path, string, required) — The field key is specified in the following format: $(app-key)\\$(field-key). For example, example-add-on\\example-issue-field.
- `optionId` (path, string, required) — The ID of the option to be deleted.

## Original description

Deletes an option from a select list issue field.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
