---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/request/{issueIdOrKey}/sla/{slaMetricId}"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_sla_information_by_id]]"
---
# JSM - Get sla information by id

**Get sla information by id** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/sla/{slaMetricId}`

- Run by the tool [[jsm_get_sla_information_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/sla/{{param:slaMetricId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request whose SLAs will be retrieved.
- `slaMetricId` (path, string, required) — The ID or key of the SLAs metric to be retrieved.

## Original description

This method returns the details for an SLA on a customer request.

**[Permissions](#permissions) required**:

 *  Agent for the Service Desk containing the queried customer request, AND
 *  Browse Projects permission on the project containing the customer request, including any restrictions imposed by issue security schemes or custom permission schemes on the specific issue.
