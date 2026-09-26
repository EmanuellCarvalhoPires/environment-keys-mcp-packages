---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: PUT
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}"
category: "Servicedesk"
writes_data: true
tool_note: "[[jsm_set_property_put]]"
---
# JSM - Set property (PUT)

**Set property** — `PUT /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}`

- Run by the tool [[jsm_set_property_put]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
PUT {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/property/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk which contains the request type. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The ID of the request type on which the property will be set.
- `propertyKey` (path, string, required) — The key of the request type property. The maximum length of the key is 255 bytes.

## Original description

Sets the value of a request type property. Use this resource to store custom data against a request type.

Properties for a Request Type in next-gen are stored as Issue Type properties and therefore can also be set by calling the Jira Cloud Platform [Set issue type property](https://developer.atlassian.com/cloud/jira/platform/rest/v3/#api-rest-api-3-issuetype-issueTypeId-properties-propertyKey-put) endpoint.

**[Permissions](#permissions) required**: Jira project administrator with a Jira Service Management agent license.
