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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_properties_keys_get]]"
---
# JSM - Get properties keys (GET)

**Get properties keys** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property`

- Run by the tool [[jsm_get_properties_keys_get]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/property
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk which contains the request type. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The ID of the request type for which keys will be retrieved.

## Original description

Returns the keys of all properties for a request type.

Properties for a Request Type in next-gen are stored as Issue Type properties and therefore the keys of all properties for a request type are also available by calling the Jira Cloud Platform [Get issue type property keys](https://developer.atlassian.com/cloud/jira/platform/rest/v3/#api-rest-api-3-issuetype-issueTypeId-properties-get) endpoint.

**[Permissions](#permissions) required**: The user must have permission to view the request type.
