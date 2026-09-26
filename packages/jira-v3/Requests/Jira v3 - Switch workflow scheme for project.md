---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme/project/switch"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_switch_workflow_scheme_for_project]]"
---
# Jira v3 - Switch workflow scheme for project

**Switch workflow scheme for project** — `POST /rest/api/3/workflowscheme/project/switch`

- Run by the tool [[jira_switch_workflow_scheme_for_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme/project/switch
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "mappingsByIssueTypeOverride": [
    {
      "issueTypeId": "10000",
      "statusMappings": [
        {
          "newStatusId": "10003",
          "oldStatusId": "3"
        },
        {
          "newStatusId": "10009",
          "oldStatusId": "10"
        }
      ]
    },
    {
      "issueTypeId": "10011",
      "statusMappings": [
        {
          "newStatusId": "10003",
          "oldStatusId": "3"
        },
        {
          "newStatusId": "10002",
          "oldStatusId": "10003"
        }
      ]
    }
  ],
  "projectId": "10001",
  "targetSchemeId": "10002"
}
```

## Original description

Switches a workflow scheme for a project.

Workflow schemes can only be assigned to classic projects.

**Calculating required mappings:** If statuses from the current workflow scheme won't exist in the target workflow scheme, you must provide `mappingsByIssueTypeOverride` to specify how issues with those statuses should be migrated. Use [the required workflow scheme mappings API](#api-rest-api-3-workflowscheme-update-mappings-post) to determine which statuses and issue types require mappings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
