---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-classification-levels
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectIdOrKey}/classification-level/default"
category: "Project classification levels"
writes_data: true
tool_note: "[[jira_update_the_default_data_classification_level_of_a_project]]"
---
# Jira v3 - Update the default data classification level of a project

**Update the default data classification level of a project** — `PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default`

- Run by the tool [[jira_update_the_default_data_classification_level_of_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/classification-level/default
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case-sensitive).
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "id": "ari:cloud:platform::classification-tag/dec24c48-5073-4c25-8fef-9d81a992c30c"
}
```

## Original description

Updates the default data classification level for a project.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
