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
path: "/rest/api/3/workflow/{workflowId}/workflowSchemes"
category: "Workflows"
writes_data: false
tool_note: "[[jira_get_workflow_schemes_which_are_using_a_given_workflow]]"
---
# Jira v3 - Get workflow schemes which are using a given workflow

**Get workflow schemes which are using a given workflow** — `GET /rest/api/3/workflow/{workflowId}/workflowSchemes`

- Run by the tool [[jira_get_workflow_schemes_which_are_using_a_given_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflow/{{param:workflowId}}/workflowSchemes?nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `workflowId` (path, string, required) — The workflow ID
- `nextPageToken` (query, string, optional) — The cursor for pagination
- `maxResults` (query, string, optional) — The maximum number of results to return. Must be an integer between 1 and 200.

## Original description

Returns a page of workflow schemes using a given workflow.
