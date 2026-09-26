---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/request/{issueIdOrKey}/sla"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_sla_information]]"
---
# JSM - Get sla information

**Get sla information** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/sla`

- Run by the tool [[jsm_get_sla_information]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/sla?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request whose SLAs will be retrieved.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of request types to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all the SLA records on a customer request. A customer request can have zero or more SLAs. Each SLA can have recordings for zero or more "completed cycles" and zero or 1 "ongoing cycle". Each cycle includes information on when it started and stopped, and whether it breached the SLA goal.

**[Permissions](#permissions) required**:

 *  Agent for the Service Desk containing the queried customer request, AND
 *  Browse Projects permission on the project containing the customer request, including any restrictions imposed by issue security schemes or custom permission schemes on the specific issue.
