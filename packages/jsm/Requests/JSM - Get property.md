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
path: "/rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}"
category: "Organization"
writes_data: false
tool_note: "[[jsm_get_property]]"
---
# JSM - Get property

**Get property** — `GET /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}`

- Run by the tool [[jsm_get_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}/property/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization from which the property will be returned.
- `propertyKey` (path, string, required) — The key of the property to return.

## Original description

Returns the value of an organization property. Use this method to obtain the JSON content for an organization's property. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. [Learn more](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

To get organization detail field values which are visible in Jira Service Management, see the [Customer Service Management REST API](https://developer.atlassian.com/cloud/customer-service-management/rest/v1/api-group-organization/#api-group-organization).

**[Permissions](#permissions) required**: Any

**Response limitations**: Customers can only access properties of organizations of which they are members.
