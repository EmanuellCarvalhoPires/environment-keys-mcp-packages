---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: DELETE
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}"
category: "Servicedesk"
writes_data: true
tool_note: "[[jsm_delete_request_type]]"
---
# JSM - Delete request type

**Delete request type** — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}`

- Run by the tool [[jsm_delete_request_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID or project identifier of the service desk.
- `requestTypeId` (path, string, required) — The ID of the request type.

## Original description

This method deletes a customer request type from a service desk, and removes it from all customer requests.  
This only supports classic projects.

**[Permissions](#permissions) required**: Service desk administrator.
