---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options-apps
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/field/{fieldKey}/option/{optionId}"
category: "Issue custom field options (apps)"
writes_data: true
---
# Jira v3 - Update issue field option

**Update issue field option** — `PUT /rest/api/3/field/{fieldKey}/option/{optionId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Update issue field option"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/field/{{param:fieldKey}}/option/{{param:optionId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldKey` (path, string, required) — The field key is specified in the following format: $(app-key)\\$(field-key). For example, example-add-on\\example-issue-field.
- `optionId` (path, string, required) — The ID of the option to be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "config": {
    "attributes": [],
    "scope": {
      "global": {},
      "projects": [],
      "projects2": [
        {
          "attributes": [
            "notSelectable"
          ],
          "id": 1001
        },
        {
          "attributes": [
            "notSelectable"
          ],
          "id": 1002
        }
      ]
    }
  },
  "id": 1,
  "properties": {
    "description": "The team's description",
    "founded": "2016-06-06",
    "leader": {
      "email": "lname@example.com",
      "name": "Leader Name"
    },
    "members": 42
  },
  "value": "Team 1"
}
```

## Original description

Updates or creates an option for a select list issue field. This operation requires that the option ID is provided when creating an option, therefore, the option ID needs to be specified as a path and body parameter. The option ID provided in the path and body must be identical.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
