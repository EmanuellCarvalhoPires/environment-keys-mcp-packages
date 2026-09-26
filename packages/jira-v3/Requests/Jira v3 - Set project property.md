---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}"
category: "Project properties"
writes_data: true
tool_note: "[[jira_set_project_property]]"
---
# Jira v3 - Set project property

**Set project property** — `PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}`

- Run by the tool [[jira_set_project_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `propertyKey` (path, string, required) — The key of the project property. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "number": 5,
  "string": "string-value"
}
```

## Original description

Sets the value of the [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). You can use project properties to store custom data against the project.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the property is created.
