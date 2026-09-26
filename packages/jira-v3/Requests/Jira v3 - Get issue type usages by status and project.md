---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages"
category: "Status"
writes_data: false
tool_note: "[[jira_get_issue_type_usages_by_status_and_project]]"
---
# Jira v3 - Get issue type usages by status and project

**Get issue type usages by status and project** — `GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages`

- Run by the tool [[jira_get_issue_type_usages_by_status_and_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuses/{{param:statusId}}/project/{{param:projectId}}/issueTypeUsages?nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `statusId` (path, string, required) — The statusId to fetch issue type usages for
- `projectId` (path, string, required) — The projectId to fetch issue type usages for
- `nextPageToken` (query, string, optional) — The cursor for pagination
- `maxResults` (query, string, optional) — The maximum number of results to return. Must be an integer between 1 and 200.

## Original description

Returns a page of issue types in a project using a given status.
