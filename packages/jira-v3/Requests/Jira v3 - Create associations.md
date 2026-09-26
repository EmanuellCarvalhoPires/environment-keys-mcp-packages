---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-associations
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/field/association"
category: "Issue custom field associations"
writes_data: true
tool_note: "[[jira_create_associations]]"
---
# Jira v3 - Create associations

**Create associations** — `PUT /rest/api/3/field/association`

- Run by the tool [[jira_create_associations]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/field/association
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

Associates fields with projects.

Fields will be associated with each issue type on the requested projects.

Fields will be associated with all projects that share the same field configuration which the provided projects are using. This means that while the field will be associated with the requested projects, it will also be associated with any other projects that share the same field configuration.

If a success response is returned it means that the field association has been created in any applicable contexts where it wasn't already present.

Up to 50 fields and up to 100 projects can be associated in a single request. If more fields or projects are provided a 400 response will be returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
