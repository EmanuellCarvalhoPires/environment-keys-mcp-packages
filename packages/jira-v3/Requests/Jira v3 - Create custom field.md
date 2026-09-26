---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field"
category: "Issue fields"
writes_data: true
tool_note: "[[jira_create_custom_field]]"
---
# Jira v3 - Create custom field

**Create custom field** — `POST /rest/api/3/field`

- Run by the tool [[jira_create_custom_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Custom field for picking groups",
  "name": "New custom field",
  "searcherKey": "com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher",
  "type": "com.atlassian.jira.plugin.system.customfieldtypes:grouppicker"
}
```

## Original description

Creates a custom field.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
