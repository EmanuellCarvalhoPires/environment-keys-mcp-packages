---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers/total_in_cloud"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get total subscribers in cloud

**Get total subscribers in cloud** — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/total_in_cloud`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get total subscribers in cloud"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers/total_in_cloud
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Get the total number of subscribers in the cloud for Status page.
