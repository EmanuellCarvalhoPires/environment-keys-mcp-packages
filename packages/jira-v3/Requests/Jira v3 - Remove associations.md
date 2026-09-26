---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-associations
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/field/association"
category: "Issue custom field associations"
writes_data: true
tool_note: "[[jira_remove_associations]]"
---
# Jira v3 - Remove associations

**Remove associations** — `DELETE /rest/api/3/field/association`

- Run by the tool [[jira_remove_associations]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/field/association
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "associationContexts": [
    {
      "identifier": 10000,
      "type": "PROJECT_ID"
    },
    {
      "identifier": 10001,
      "type": "PROJECT_ID"
    }
  ],
  "fields": [
    {
      "identifier": "customfield_10000",
      "type": "FIELD_ID"
    },
    {
      "identifier": "customfield_10001",
      "type": "FIELD_ID"
    }
  ]
}
```

## Original description

Unassociates a set of fields with a project and issue type context.

Fields will be unassociated with all projects/issue types that share the same field configuration which the provided project and issue types are using. This means that while the field will be unassociated with the provided project and issue types, it will also be unassociated with any other projects and issue types that share the same field configuration.

If a success response is returned it means that the field association has been removed in any applicable contexts where it was present.

Up to 50 fields and up to 100 projects and issue types can be unassociated in a single request. If more fields or projects are provided a 400 response will be returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
