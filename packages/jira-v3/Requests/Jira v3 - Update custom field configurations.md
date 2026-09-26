---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-configuration-apps
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/app/field/{fieldIdOrKey}/context/configuration"
category: "Issue custom field configuration (apps)"
writes_data: true
---
# Jira v3 - Update custom field configurations

**Update custom field configurations** — `PUT /rest/api/3/app/field/{fieldIdOrKey}/context/configuration`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Update custom field configurations"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/app/field/{{param:fieldIdOrKey}}/context/configuration
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldIdOrKey` (path, string, required) — The ID or key of the custom field, for example customfield10000.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "configurations": [
    {
      "id": "10000"
    },
    {
      "configuration": {
        "maxValue": 10000,
        "minValue": 0
      },
      "id": "10001",
      "schema": {
        "properties": {
          "amount": {
            "type": "number"
          },
          "currency": {
            "type": "string"
          }
        },
        "required": [
          "amount",
          "currency"
        ]
      }
    }
  ]
}
```

## Original description

Update the configuration for contexts of a custom field of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field type.
