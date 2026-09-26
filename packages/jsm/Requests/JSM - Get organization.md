---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/organization/{organizationId}"
category: "Organization"
writes_data: false
tool_note: "[[jsm_get_organization]]"
---
# JSM - Get organization

**Get organization** — `GET /rest/servicedeskapi/organization/{organizationId}`

- Run by the tool [[jsm_get_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization.

## Original description

This method returns details of an organization. Use this method to get organization details whenever your application component is passed an organization ID but needs to display other organization details.

To get organization detail field values which are visible in Jira Service Management, see the [Customer Service Management REST API](https://developer.atlassian.com/cloud/customer-service-management/rest/v1/api-group-organization/#api-group-organization).

**[Permissions](#permissions) required**: Any

**Response limitations**: Customers can only retrieve organization of which they are members.
