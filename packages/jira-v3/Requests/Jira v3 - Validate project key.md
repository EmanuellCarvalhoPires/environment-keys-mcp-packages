---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-key-and-name-validation
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/projectvalidate/key"
category: "Project key and name validation"
writes_data: false
tool_note: "[[jira_validate_project_key]]"
---
# Jira v3 - Validate project key

**Validate project key** — `GET /rest/api/3/projectvalidate/key`

- Run by the tool [[jira_validate_project_key]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/projectvalidate/key?key={{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `key` (query, string, optional) — The project key.

## Original description

Validates a project key by confirming the key is a valid string and not in use.

**[Permissions](#permissions) required:** None.
