---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_request_types]]"
---
# JSM - Get request types

**Get request types** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype`

- Run by the tool [[jsm_get_request_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype?groupId={{param:groupId}}&expand={{param:expand}}&searchQuery={{param:searchQuery}}&start={{param:start}}&limit={{param:limit}}&includeHiddenRequestTypesInSearch={{param:includeHiddenRequestTypesInSearch}}&restrictionStatus={{param:restrictionStatus}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk whose customer request types are to be returned. This can alternatively be a project identifier.
- `groupId` (query, string, optional) — Filters results to those in a customer request type group.
- `expand` (query, string, optional) — Query parameter expand.
- `searchQuery` (query, string, optional) — The string to be used to filter the results.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.
- `includeHiddenRequestTypesInSearch` (query, string, optional) — Whether to include hidden request types when searching with searchQuery.
- `restrictionStatus` (query, string, optional) — Request type restriction status (open or restricted) used to filter the results.

## Original description

This method returns all customer request types from a service desk. There are two parameters for filtering the returned list:

 *  `groupId` which filters the results to items in the customer request type group.
 *  `searchQuery` which is matched against request types' `name` or `description`. For example, the strings "Install", "Inst", "Equi", or "Equipment" will match a request type with the *name* "Equipment Installation Request".

**Note:** This API by default will filter out request types hidden in the portal (i.e. request types without groups and request types where a user doesn't have permission) when `searchQuery` is provided, unless `includeHiddenRequestTypesInSearch` is set to true. Restricted request types will not be returned for those who aren't admins.

**[Permissions](#permissions) required**: Permission to access the service desk.
