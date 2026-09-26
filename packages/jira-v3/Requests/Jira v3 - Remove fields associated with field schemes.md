---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/config/fieldschemes/fields"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_remove_fields_associated_with_field_schemes]]"
---
# Jira v3 - Remove fields associated with field schemes

**Remove fields associated with field schemes** — `DELETE /rest/api/3/config/fieldschemes/fields`

- Run by the tool [[jira_remove_fields_associated_with_field_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/config/fieldschemes/fields
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "customfield_10000": {
    "schemeIds": [
      10000,
      10001
    ]
  },
  "customfield_10001": {
    "schemeIds": [
      10002
    ]
  }
}
```

## Original description

Remove fields associated with field association schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
