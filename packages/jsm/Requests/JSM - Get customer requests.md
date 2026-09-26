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
path: "/rest/servicedeskapi/request"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_customer_requests]]"
---
# JSM - Get customer requests

**Get customer requests** — `GET /rest/servicedeskapi/request`

- Run by the tool [[jsm_get_customer_requests]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request?searchTerm={{param:searchTerm}}&requestOwnership={{param:requestOwnership}}&requestStatus={{param:requestStatus}}&approvalStatus={{param:approvalStatus}}&organizationId={{param:organizationId}}&serviceDeskId={{param:serviceDeskId}}&requestTypeId={{param:requestTypeId}}&expand={{param:expand}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `searchTerm` (query, string, optional) — Filters customer requests where the request summary matches the searchTerm. Wildcards can be used in the searchTerm parameter.
- `requestOwnership` (query, string, optional) — Filters customer requests using the following values: OWNEDREQUESTS returns customer requests where the user is the creator.
- `requestStatus` (query, string, optional) — Filters customer requests where the request is closed, open, or either of the two where: CLOSEDREQUESTS returns customer requests that are closed.
- `approvalStatus` (query, string, optional) — Filters results to customer requests based on their approval status: MYPENDINGAPPROVAL returns customer requests pending the user's approval.
- `organizationId` (query, string, optional) — Filters customer requests that belong to a specific organization (note that the user must be a member of that organization). Note: Valid only when used with requestOwnership=ORGANIZATION.
- `serviceDeskId` (query, string, optional) — Filters customer requests by service desk.
- `requestTypeId` (query, string, optional) — Filters customer requests by request type. Note that the serviceDeskId must be specified for the service desk in which the request type belongs.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the customer request to expand, where: serviceDesk returns additional details for each service desk.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all customer requests for the user executing the query.

The returned customer requests are ordered chronologically by the latest activity on each request. For example, the latest status transition or comment.

**[Permissions](#permissions) required**: Permission to access the specified service desk.

**Response limitations**: For customers, the list returned will include request they created (or were created on their behalf) or are participating in only.
