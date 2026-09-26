---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/config/fieldschemes/fields"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_update_fields_associated_with_field_schemes]]"
---
# Jira v3 - Update fields associated with field schemes

**Update fields associated with field schemes** — `PUT /rest/api/3/config/fieldschemes/fields`

- Run by the tool [[jira_update_fields_associated_with_field_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/config/fieldschemes/fields
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
  "customfield_10000": [
    {
      "restrictedToWorkTypes": [
        1,
        2
      ],
      "schemeIds": [
        10000,
        10001
      ]
    }
  ],
  "customfield_10001": [
    {
      "schemeIds": [
        10002
      ]
    }
  ]
}
```

## Original description

Update fields associated with field association schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
