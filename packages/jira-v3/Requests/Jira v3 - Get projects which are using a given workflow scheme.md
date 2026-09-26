---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages"
category: "Workflow schemes"
writes_data: false
tool_note: "[[jira_get_projects_which_are_using_a_given_workflow_scheme]]"
---
# Jira v3 - Get projects which are using a given workflow scheme

**Get projects which are using a given workflow scheme** — `GET /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages`

- Run by the tool [[jira_get_projects_which_are_using_a_given_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:workflowSchemeId}}/projectUsages?nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `workflowSchemeId` (path, string, required) — The workflow scheme ID
- `nextPageToken` (query, string, optional) — The cursor for pagination
- `maxResults` (query, string, optional) — The maximum number of results to return. Must be an integer between 1 and 200.

## Original description

Returns a page of projects using a given workflow scheme.
