---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme/{id}/draft/publish"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_publish_draft_workflow_scheme]]"
---
# Jira v3 - Publish draft workflow scheme

**Publish draft workflow scheme** — `POST /rest/api/3/workflowscheme/{id}/draft/publish`

- Run by the tool [[jira_publish_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/publish?validateOnly={{param:validateOnly}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `validateOnly` (query, string, optional) — Whether the request only performs a validation.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "statusMappings": [
    {
      "issueTypeId": "10001",
      "newStatusId": "1",
      "statusId": "3"
    },
    {
      "issueTypeId": "10001",
      "newStatusId": "2",
      "statusId": "2"
    },
    {
      "issueTypeId": "10002",
      "newStatusId": "10003",
      "statusId": "10005"
    },
    {
      "issueTypeId": "10003",
      "newStatusId": "1",
      "statusId": "4"
    }
  ]
}
```

## Original description

Publishes a draft workflow scheme.

Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
