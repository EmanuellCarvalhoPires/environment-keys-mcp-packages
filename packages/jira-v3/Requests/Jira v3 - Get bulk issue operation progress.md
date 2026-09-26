---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/bulk/queue/{taskId}"
category: "Issue bulk operations"
writes_data: false
tool_note: "[[jira_get_bulk_issue_operation_progress]]"
---
# Jira v3 - Get bulk issue operation progress

**Get bulk issue operation progress** — `GET /rest/api/3/bulk/queue/{taskId}`

- Run by the tool [[jira_get_bulk_issue_operation_progress]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/bulk/queue/{{param:taskId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `taskId` (path, string, required) — The ID of the task.

## Original description

Use this to get the progress state for the specified bulk operation `taskId`.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).

If the task is running, this resource will return:

    {"taskId":"10779","status":"RUNNING","progressPercent":65,"submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"created":1690180055963,"started":1690180056206,"updated":169018005829}

If the task has completed, then this resource will return:

    {"processedAccessibleIssues":[10001,10002],"created":1709189449954,"progressPercent":100,"started":1709189450154,"status":"COMPLETE","submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"invalidOrInaccessibleIssueCount":0,"taskId":"10000","totalIssueCount":2,"updated":1709189450354}

**Note:** You can view task progress for up to 14 days from creation.
