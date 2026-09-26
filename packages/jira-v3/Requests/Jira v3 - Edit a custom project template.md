---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project-template/edit-template"
category: "Project templates"
writes_data: true
tool_note: "[[jira_edit_a_custom_project_template]]"
---
# Jira v3 - Edit a custom project template

**Edit a custom project template** — `PUT /rest/api/3/project-template/edit-template`

- Run by the tool [[jira_edit_a_custom_project_template]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project-template/edit-template
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Edit custom template

This API endpoint allows you to edit an existing customised template.

***Note: Custom Templates are only supported for Jira Enterprise edition.***
