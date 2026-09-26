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
path: "/rest/api/3/config/fieldschemes/projects"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_associate_projects_to_field_schemes]]"
---
# Jira v3 - Associate projects to field schemes

**Associate projects to field schemes** — `PUT /rest/api/3/config/fieldschemes/projects`

- Run by the tool [[jira_associate_projects_to_field_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/config/fieldschemes/projects
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
  "10000": {
    "projectIds": [
      10000,
      10001
    ]
  },
  "10001": {
    "projectIds": [
      10002
    ]
  }
}
```

## Original description

Associate projects to field association schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
