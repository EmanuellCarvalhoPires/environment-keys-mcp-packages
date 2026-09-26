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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}"
category: "Servicedesk"
writes_data: true
tool_note: "[[jsm_delete_property_delete]]"
---
# JSM - Delete property (DELETE)

**Delete property** — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}`

- Run by the tool [[jsm_delete_property_delete]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/property/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk which contains the request type. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The ID of the request type for which the property will be removed.
- `propertyKey` (path, string, required) — The key of the property to remove.

## Original description

Removes a property from a request type.

Properties for a Request Type in next-gen are stored as Issue Type properties and therefore can also be deleted by calling the Jira Cloud Platform [Delete issue type property](https://developer.atlassian.com/cloud/jira/platform/rest/v3/#api-rest-api-3-issuetype-issueTypeId-properties-propertyKey-delete) endpoint.

**[Permissions](#permissions) required**: Jira project administrator with a Jira Service Management agent license.
