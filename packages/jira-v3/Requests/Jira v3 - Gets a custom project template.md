---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project-template/live-template"
category: "Project templates"
writes_data: false
tool_note: "[[jira_gets_a_custom_project_template]]"
---
# Jira v3 - Gets a custom project template

**Gets a custom project template** — `GET /rest/api/3/project-template/live-template`

- Run by the tool [[jira_gets_a_custom_project_template]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project-template/live-template?projectId={{param:projectId}}&templateKey={{param:templateKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectId` (query, string, optional) — optional - The \{@link String\} containing the project key linked to the custom template to retrieve
- `templateKey` (query, string, optional) — optional - The \{@link String\} containing the key of the custom template to retrieve

## Original description

Get custom template

This API endpoint allows you to get a live custom project template details by either templateKey or projectId

***Note: Custom Templates are only supported for Jira Enterprise edition.***
