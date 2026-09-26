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
path: "/rest/servicedeskapi/organization/{organizationId}"
category: "Organization"
writes_data: true
tool_note: "[[jsm_delete_organization]]"
---
# JSM - Delete organization

**Delete organization** — `DELETE /rest/servicedeskapi/organization/{organizationId}`

- Run by the tool [[jsm_delete_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization.

## Original description

This method deletes an organization. Note that the organization is deleted regardless of other associations it may have. For example, associations with service desks.

**[Permissions](#permissions) required**: Jira administrator.
