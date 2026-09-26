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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/field"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_request_type_fields]]"
---
# JSM - Get request type fields

**Get request type fields** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/field`

- Run by the tool [[jsm_get_request_type_fields]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/field?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk containing the request types whose fields are to be returned. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The ID of the request types whose fields are to be returned.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts hiddenFields that returns hidden fields associated with the request type.

## Original description

This method returns the fields for a service desk's customer request type.

Also, the following information about the user's permissions for the request type is returned:

 *  `canRaiseOnBehalfOf` returns `true` if the user has permission to raise customer requests on behalf of other customers. Otherwise, returns `false`.
 *  `canAddRequestParticipants` returns `true` if the user can add customer request participants. Otherwise, returns `false`.

**[Permissions](#permissions) required**: Permission to view the Service Desk. However, hidden fields would be visible to only Service desk's Administrator.
