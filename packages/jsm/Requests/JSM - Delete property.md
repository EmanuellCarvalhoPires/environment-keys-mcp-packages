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
path: "/rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}"
category: "Organization"
writes_data: true
tool_note: "[[jsm_delete_property]]"
---
# JSM - Delete property

**Delete property** — `DELETE /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}`

- Run by the tool [[jsm_delete_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}/property/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization from which the property will be removed.
- `propertyKey` (path, string, required) — The key of the property to remove.

## Original description

Removes an organization property. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. [Learn more](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

For operations relating to organization detail field values which are visible in Jira Service Management, see the [Customer Service Management REST API](https://developer.atlassian.com/cloud/customer-service-management/rest/v1/api-group-organization/#api-group-organization).

**[Permissions](#permissions) required**: Service Desk Administrator or Agent.

Note: Permission to manage organizations can be switched to users with the Jira administrator permission, using the **[Organization management](https://confluence.atlassian.com/servicedeskcloud/setting-up-service-desk-users-732528877.html#Settingupservicedeskusers-manageorgsManageorganizations)** feature.
