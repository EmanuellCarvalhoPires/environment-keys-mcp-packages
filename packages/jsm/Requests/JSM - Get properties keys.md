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
path: "/rest/servicedeskapi/organization/{organizationId}/property"
category: "Organization"
writes_data: false
tool_note: "[[jsm_get_properties_keys]]"
---
# JSM - Get properties keys

**Get properties keys** — `GET /rest/servicedeskapi/organization/{organizationId}/property`

- Run by the tool [[jsm_get_properties_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}/property
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization from which keys will be returned.

## Original description

Returns the keys of all organization properties. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. [Learn more](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

To get organization detail field values which are visible in Jira Service Management, see the [Customer Service Management REST API](https://developer.atlassian.com/cloud/customer-service-management/rest/v1/api-group-organization/#api-group-organization).

**[Permissions](#permissions) required**: Any

**Response limitations**: Customers can only access properties of organizations of which they are members.
