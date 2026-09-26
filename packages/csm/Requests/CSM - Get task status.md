---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/task
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/tasks/{taskId}"
category: "Task"
writes_data: false
---
# CSM - Get task status

**Get task status** — `GET /api/v1/tasks/{taskId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get task status"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/tasks/{{param:taskId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `taskId` (path, string, required) — Value of taskId in the path.

## Original description

Returns the status of a given task, including a list of any failures on completion.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/), or Customer Service Management or Jira Service Management user.
