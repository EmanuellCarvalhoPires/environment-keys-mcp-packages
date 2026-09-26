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
path: "/rest/servicedeskapi/organization"
category: "Organization"
writes_data: false
tool_note: "[[jsm_get_organizations]]"
---
# JSM - Get organizations

**Get organizations** — `GET /rest/servicedeskapi/organization`

- Run by the tool [[jsm_get_organizations]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/organization?start={{param:start}}&limit={{param:limit}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of organizations to return per page. Default: 50. See the Pagination section for more details.
- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.

## Original description

This method returns a list of organizations in the Jira Service Management instance. Use this method when you want to present a list of organizations or want to locate an organization by name.

**[Permissions](#permissions) required**: Any. However, to fetch organizations based on `accountId` the user must have a Service Desk agent license.

**Response limitations**: If the user is a customer, only those organizations of which the customer is a member are listed.
