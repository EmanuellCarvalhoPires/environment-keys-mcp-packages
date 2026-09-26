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
path: "/rest/api/3/config/fieldschemes/fields/parameters"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_update_field_parameters]]"
---
# Jira v3 - Update field parameters

**Update field parameters** — `PUT /rest/api/3/config/fieldschemes/fields/parameters`

- Run by the tool [[jira_update_field_parameters]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/config/fieldschemes/fields/parameters
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
      "parameters": {
        "description": "Field description",
        "isRequired": true,
        "rendererType": "atlassian-wiki-renderer"
      },
      "schemeIds": [
        10000,
        10001
      ],
      "workTypeParameters": [
        {
          "description": "Description for Bug",
          "isRequired": false,
          "rendererType": "jira-text-renderer",
          "workTypeId": 10002
        }
      ]
    }
  ],
  "customfield_10001": [
    {
      "schemeIds": [
        10001
      ],
      "workTypeParameters": [
        {
          "description": "Description for Bug",
          "isRequired": false,
          "workTypeId": 10002
        },
        {
          "description": "Description for Task",
          "isRequired": true,
          "rendererType": "atlassian-wiki-renderer",
          "workTypeId": 10003
        }
      ]
    }
  ]
}
```

## Original description

Update field association item parameters in field association schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
