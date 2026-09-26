---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project-template/save-template"
category: "Project templates"
writes_data: true
tool_note: "[[jira_save_a_custom_project_template]]"
---
# Jira v3 - Save a custom project template

**Save a custom project template** — `POST /rest/api/3/project-template/save-template`

- Run by the tool [[jira_save_a_custom_project_template]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project-template/save-template
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Save custom template

This API endpoint allows you to save a customised template

***Note: Custom Templates are only supported for Jira Enterprise edition.***
