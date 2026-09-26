---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/requesttype
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/requesttype"
category: "Requesttype"
writes_data: false
tool_note: "[[jsm_get_all_request_types]]"
---
# JSM - Get all request types

**Get all request types** — `GET /rest/servicedeskapi/requesttype`

- Run by the tool [[jsm_get_all_request_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/requesttype?searchQuery={{param:searchQuery}}&serviceDeskId={{param:serviceDeskId}}&start={{param:start}}&limit={{param:limit}}&expand={{param:expand}}&includeHiddenRequestTypesInSearch={{param:includeHiddenRequestTypesInSearch}}&restrictionStatus={{param:restrictionStatus}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `searchQuery` (query, string, optional) — String to be used to filter the results.
- `serviceDeskId` (query, string, optional) — Filter the request types by service desk Ids provided. Multiple values of the query parameter are supported.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.
- `expand` (query, string, optional) — Query parameter expand.
- `includeHiddenRequestTypesInSearch` (query, string, optional) — Whether to include hidden request types when searching with searchQuery.
- `restrictionStatus` (query, string, optional) — Request type restriction status (open or restricted) used to filter the results.

## Original description

This method returns all customer request types used in the Jira Service Management instance, optionally filtered by a query string.

Use [servicedeskapi/servicedesk/\{serviceDeskId\}/requesttype](#api-servicedesk-serviceDeskId-requesttype-get) to find the customer request types supported by a specific service desk.

The returned list of customer request types can be filtered using the `searchQuery` parameter. The parameter is matched against the customer request types' `name` or `description`. For example, searching for "Install", "Inst", "Equi", or "Equipment" will match a customer request type with the *name* "Equipment Installation Request".

**Note:** This API by default will filter out request types hidden in the portal (i.e. request types without groups and request types where a user doesn't have permission) when `searchQuery` is provided, unless `includeHiddenRequestTypesInSearch` is set to true. Restricted request types will not be returned for those who aren't admins.

**[Permissions](#permissions) required**: Any
