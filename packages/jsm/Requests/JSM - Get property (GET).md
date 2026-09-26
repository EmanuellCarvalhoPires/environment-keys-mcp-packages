---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_property_get]]"
---
# JSM - Get property (GET)

**Get property** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}`

- Run by the tool [[jsm_get_property_get]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/property/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk which contains the request type. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The ID of the request type from which the property will be retrieved.
- `propertyKey` (path, string, required) — The key of the property to return.

## Original description

Returns the value of the property from a request type.

Properties for a Request Type in next-gen are stored as Issue Type properties and therefore also available by calling the Jira Cloud Platform [Get issue type property](https://developer.atlassian.com/cloud/jira/platform/rest/v3/#api-rest-api-3-issuetype-issueTypeId-properties-propertyKey-get) endpoint.

**[Permissions](#permissions) required**: User must have permission to view the request type.
