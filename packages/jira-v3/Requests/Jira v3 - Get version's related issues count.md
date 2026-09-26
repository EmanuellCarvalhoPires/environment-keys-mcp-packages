---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/version/{id}/relatedIssueCounts"
category: "Project versions"
writes_data: false
tool_note: "[[jira_get_version_s_related_issues_count]]"
---
# Jira v3 - Get version's related issues count

**Get version's related issues count** — `GET /rest/api/3/version/{id}/relatedIssueCounts`

- Run by the tool [[jira_get_version_s_related_issues_count]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/version/{{param:id}}/relatedIssueCounts
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the version.

## Original description

Returns the following counts for a version:

 *  Number of issues where the `fixVersion` is set to the version.
 *  Number of issues where the `affectedVersion` is set to the version.
 *  Number of issues where a version custom field is set to the version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
