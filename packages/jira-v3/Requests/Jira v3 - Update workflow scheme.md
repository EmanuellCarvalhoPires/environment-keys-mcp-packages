---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme/update"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_update_workflow_scheme]]"
---
# Jira v3 - Update workflow scheme

**Update workflow scheme** — `POST /rest/api/3/workflowscheme/update`

- Run by the tool [[jira_update_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme/update
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
  "defaultWorkflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677",
  "description": "description",
  "id": "10000",
  "name": "name",
  "statusMappingsByIssueTypeOverride": [
    {
      "issueTypeId": "10001",
      "statusMappings": [
        {
          "newStatusId": "2",
          "oldStatusId": "1"
        },
        {
          "newStatusId": "4",
          "oldStatusId": "3"
        }
      ]
    },
    {
      "issueTypeId": "10002",
      "statusMappings": [
        {
          "newStatusId": "4",
          "oldStatusId": "1"
        },
        {
          "newStatusId": "2",
          "oldStatusId": "3"
        }
      ]
    }
  ],
  "statusMappingsByWorkflows": [
    {
      "newWorkflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677",
      "oldWorkflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677",
      "statusMappings": [
        {
          "newStatusId": "2",
          "oldStatusId": "1"
        },
        {
          "newStatusId": "4",
          "oldStatusId": "3"
        }
      ]
    }
  ],
  "version": {
    "id": "527213fc-bc72-400f-aae0-df8d88db2c8a",
    "versionNumber": 1
  },
  "workflowsForIssueTypes": [
    {
      "issueTypeIds": [
        "10000",
        "10003"
      ],
      "workflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677"
    },
    {
      "issueTypeIds": [
        "10001`",
        "10002"
      ],
      "workflowId": "3f83dg2a-ns2n-56ab-9812-42h5j1461629"
    }
  ]
}
```

## Original description

Updates company-managed and team-managed project workflow schemes. This API doesn't have a concept of draft, so any changes made to a workflow scheme are immediately available. When changing the available statuses for issue types, an [asynchronous task](#async) migrates the issues as defined in the provided mappings.

**[Permissions](#permissions) required:**

 *  *Administer Jira* project permission to update all, including global-scoped, workflow schemes.
 *  *Administer projects* project permission to update project-scoped workflow schemes.
