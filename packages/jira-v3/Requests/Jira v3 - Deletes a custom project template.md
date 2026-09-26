---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/project-template/remove-template"
category: "Project templates"
writes_data: true
tool_note: "[[jira_deletes_a_custom_project_template]]"
---
# Jira v3 - Deletes a custom project template

**Deletes a custom project template** — `DELETE /rest/api/3/project-template/remove-template`

- Run by the tool [[jira_deletes_a_custom_project_template]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/project-template/remove-template?templateKey={{param:templateKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `templateKey` (query, string, required) — The \{@link String\} containing the key of the custom template to remove

## Original description

Remove custom template

This API endpoint allows you to remove a specified customised template

***Note: Custom Templates are only supported for Jira Enterprise edition.***
