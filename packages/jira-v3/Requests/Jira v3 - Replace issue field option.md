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
path: "/rest/api/3/field/{fieldKey}/option/{optionId}/issue"
category: "Issue custom field options (apps)"
writes_data: true
---
# Jira v3 - Replace issue field option

**Replace issue field option** — `DELETE /rest/api/3/field/{fieldKey}/option/{optionId}/issue`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Replace issue field option"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/field/{{param:fieldKey}}/option/{{param:optionId}}/issue?replaceWith={{param:replaceWith}}&jql={{param:jql}}&overrideScreenSecurity={{param:overrideScreenSecurity}}&overrideEditableFlag={{param:overrideEditableFlag}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldKey` (path, string, required) — The field key is specified in the following format: $(app-key)\\$(field-key). For example, example-add-on\\example-issue-field.
- `optionId` (path, string, required) — The ID of the option to be deselected.
- `replaceWith` (query, string, optional) — The ID of the option that will replace the currently selected option.
- `jql` (query, string, optional) — A JQL query that specifies the issues to be updated. For example, project=10000.
- `overrideScreenSecurity` (query, string, optional) — Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with admin permission.
- `overrideEditableFlag` (query, string, optional) — Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with Administer Jira global permission.

## Original description

Deselects an issue-field select-list option from all issues where it is selected. A different option can be selected to replace the deselected option. The update can also be limited to a smaller set of issues by using a JQL query.

Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

This is an [asynchronous operation](#async). The response object contains a link to the long-running task.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
