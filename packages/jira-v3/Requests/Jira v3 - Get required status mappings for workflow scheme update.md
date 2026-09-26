---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme/update/mappings"
category: "Workflow schemes"
writes_data: false
tool_note: "[[jira_get_required_status_mappings_for_workflow_scheme_update]]"
---
# Jira v3 - Get required status mappings for workflow scheme update

**Get required status mappings for workflow scheme update** — `POST /rest/api/3/workflowscheme/update/mappings`

- Run by the tool [[jira_get_required_status_mappings_for_workflow_scheme_update]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme/update/mappings
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultWorkflowId": "10010",
  "id": "10001",
  "workflowsForIssueTypes": [
    {
      "issueTypeIds": [
        "10010",
        "10011"
      ],
      "workflowId": "10001"
    }
  ]
}
```

## Original description

Gets the required status mappings for the desired changes to a workflow scheme. The results are provided per issue type and workflow. When updating a workflow scheme, status mappings can be provided per issue type, per workflow, or both.

**[Permissions](#permissions) required:**

 *  *Administer Jira* permission to update all, including global-scoped, workflow schemes.
 *  *Administer projects* project permission to update project-scoped workflow schemes.
