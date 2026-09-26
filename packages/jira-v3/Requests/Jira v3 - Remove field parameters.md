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
path: "/rest/api/3/config/fieldschemes/fields/parameters"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_remove_field_parameters]]"
---
# Jira v3 - Remove field parameters

**Remove field parameters** — `DELETE /rest/api/3/config/fieldschemes/fields/parameters`

- Run by the tool [[jira_remove_field_parameters]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/config/fieldschemes/fields/parameters
Authorization: {{service.auth_token}}
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
      "parameters": [
        "description",
        "isRequired"
      ],
      "schemeId": 10000,
      "workTypeIds": [
        1,
        2
      ]
    }
  ],
  "description": [
    {
      "parameters": [
        "description"
      ],
      "schemeId": 10001,
      "workTypeIds": [
        3
      ]
    }
  ]
}
```

## Original description

Remove field association parameters overrides for work types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
