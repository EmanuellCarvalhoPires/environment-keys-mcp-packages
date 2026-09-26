---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/field/{fieldId}"
category: "Issue fields"
writes_data: true
tool_note: "[[jira_update_custom_field]]"
---
# Jira v3 - Update custom field

**Update custom field** — `PUT /rest/api/3/field/{fieldId}`

- Run by the tool [[jira_update_custom_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/field/{{param:fieldId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Select the manager and the corresponding employee.",
  "name": "Managers and employees list",
  "searcherKey": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher"
}
```

## Original description

Updates a custom field.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
