---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldId}/association/project"
category: "Issue fields"
writes_data: false
tool_note: "[[jira_get_field_project_associations]]"
---
# Jira v3 - Get field project associations

**Get field project associations** — `GET /rest/api/3/field/{fieldId}/association/project`

- Run by the tool [[jira_get_field_project_associations]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/association/project?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the field, for example customfield10000.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of project associations for the given custom field. Each association contains the ID of a project the field is associated with.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
