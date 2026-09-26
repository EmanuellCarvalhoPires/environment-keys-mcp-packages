---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/organization"
category: "Organization"
writes_data: true
tool_note: "[[jsm_add_organization]]"
---
# JSM - Add organization

**Add organization** — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization`

- Run by the tool [[jsm_add_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/organization
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk to which the organization will be added. This can alternatively be a project identifier.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "organizationId": 1
}
```

## Original description

This method adds an organization to a service desk. If the organization ID is already associated with the service desk, no change is made and the resource returns a 204 success code.

**[Permissions](#permissions) required**: Service desk's agent.
