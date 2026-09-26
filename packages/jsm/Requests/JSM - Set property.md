---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: PUT
path: "/rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}"
category: "Organization"
writes_data: true
tool_note: "[[jsm_set_property]]"
---
# JSM - Set property

**Set property** — `PUT /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}`

- Run by the tool [[jsm_set_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
PUT {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}/property/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization on which the property will be set.
- `propertyKey` (path, string, required) — The key of the organization's property. The maximum length of the key is 255 bytes.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "mail": "charlie@example.com",
  "phone": "0800-1233456789"
}
```

## Original description

Sets the value of an organization property. Use this resource to store custom data against an organization. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. [Learn more](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

To store organization detail field values which are visible in Jira Service Management, see the [Customer Service Management REST API](https://developer.atlassian.com/cloud/customer-service-management/rest/v1/api-group-organization/#api-group-organization).

**[Permissions](#permissions) required**: Service Desk Administrator or Agent.

Note: Permission to manage organizations can be switched to users with the Jira administrator permission, using the **[Organization management](https://confluence.atlassian.com/servicedeskcloud/setting-up-service-desk-users-732528877.html#Settingupservicedeskusers-manageorgsManageorganizations)** feature.
