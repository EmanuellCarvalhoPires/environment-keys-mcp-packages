---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/component/{id}/relatedIssueCounts"
category: "Project components"
writes_data: false
tool_note: "[[jira_get_component_issues_count]]"
---
# Jira v3 - Get component issues count

**Get component issues count** — `GET /rest/api/3/component/{id}/relatedIssueCounts`

- Run by the tool [[jira_get_component_issues_count]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/component/{{param:id}}/relatedIssueCounts
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the component.

## Original description

Returns the counts of issues assigned to the component.

This operation can be accessed anonymously.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

 *  **Classic**: `read:jira-work`
 *  **Granular**: `read:field:jira`, `read:project.component:jira`

**[Permissions](#permissions) required:** None.
