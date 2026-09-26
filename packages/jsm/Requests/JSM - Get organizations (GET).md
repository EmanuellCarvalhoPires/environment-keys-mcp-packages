---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/organization"
category: "Organization"
writes_data: false
tool_note: "[[jsm_get_organizations_get]]"
---
# JSM - Get organizations (GET)

**Get organizations** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization`

- Run by the tool [[jsm_get_organizations_get]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/organization?start={{param:start}}&limit={{param:limit}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk from which the organization list will be returned. This can alternatively be a project identifier.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.
- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.

## Original description

This method returns a list of all organizations associated with a service desk.

**[Permissions](#permissions) required**: Service desk's agent.
