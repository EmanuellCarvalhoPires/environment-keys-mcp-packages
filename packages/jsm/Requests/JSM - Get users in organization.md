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
path: "/rest/servicedeskapi/organization/{organizationId}/user"
category: "Organization"
writes_data: false
tool_note: "[[jsm_get_users_in_organization]]"
---
# JSM - Get users in organization

**Get users in organization** — `GET /rest/servicedeskapi/organization/{organizationId}/user`

- Run by the tool [[jsm_get_users_in_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}/user?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of users to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all the users associated with an organization. Use this method where you want to provide a list of users for an organization or determine if a user is associated with an organization.

**[Permissions](#permissions) required**: Service desk administrator or agent.
