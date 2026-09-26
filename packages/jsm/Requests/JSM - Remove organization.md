---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: DELETE
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/organization"
category: "Organization"
writes_data: true
tool_note: "[[jsm_remove_organization]]"
---
# JSM - Remove organization

**Remove organization** — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization`

- Run by the tool [[jsm_remove_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/organization
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk from which the organization will be removed. This can alternatively be a project identifier.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "organizationId": 1
}
```

## Original description

This method removes an organization from a service desk. If the organization ID does not match an organization associated with the service desk, no change is made and the resource returns a 204 success code.

**[Permissions](#permissions) required**: Service desk's agent.
