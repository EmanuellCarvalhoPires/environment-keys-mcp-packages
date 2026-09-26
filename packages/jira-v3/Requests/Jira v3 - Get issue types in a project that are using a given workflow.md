---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages"
category: "Workflows"
writes_data: false
tool_note: "[[jira_get_issue_types_in_a_project_that_are_using_a_given_workflo]]"
---
# Jira v3 - Get issue types in a project that are using a given workflow

**Get issue types in a project that are using a given workflow** — `GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages`

- Run by the tool [[jira_get_issue_types_in_a_project_that_are_using_a_given_workflo]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflow/{{param:workflowId}}/project/{{param:projectId}}/issueTypeUsages?nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `workflowId` (path, string, required) — The workflow ID
- `projectId` (path, string, required) — The project ID
- `nextPageToken` (query, string, optional) — The cursor for pagination
- `maxResults` (query, string, optional) — The maximum number of results to return. Must be an integer between 1 and 200.

## Original description

Returns a page of issue types using a given workflow within a project.
