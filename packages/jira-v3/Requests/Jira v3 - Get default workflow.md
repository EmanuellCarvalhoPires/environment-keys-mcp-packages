---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{id}/default"
category: "Workflow schemes"
writes_data: false
tool_note: "[[jira_get_default_workflow]]"
---
# Jira v3 - Get default workflow

**Get default workflow** — `GET /rest/api/3/workflowscheme/{id}/default`

- Run by the tool [[jira_get_default_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/default?returnDraftIfExists={{param:returnDraftIfExists}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
- `returnDraftIfExists` (query, string, optional) — Set to true to return the default workflow for the workflow scheme's draft rather than scheme itself.

## Original description

Returns the default workflow for a workflow scheme. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
