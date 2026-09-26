---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/count"
category: "Groups"
writes_data: false
---
# Admin Orgs - Get the count of groups in an organization

**Get the count of groups in an organization** — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/count`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get the count of groups in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/count?directoryIds={{param:directoryIds}}&accountIds={{param:accountIds}}&groupIds={{param:groupIds}}&resourceOwners={{param:resourceOwners}}&resourceIds={{param:resourceIds}}&searchTerm={{param:searchTerm}}&roleIds={{param:roleIds}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.
- `directoryIds` (query, string, optional) — A list of directory IDs. The requestor must have permissions to administer resources linked to these directories.
- `accountIds` (query, string, optional) — A list of user account IDs.
- `groupIds` (query, string, optional) — A list of group IDs.
- `resourceOwners` (query, string, optional) — The list of resource owners to filter the results by. Used to identify resources using their owner to which the user has at least one role assigned to.
- `resourceIds` (query, string, optional) — A list of resource IDs. The resource IDs should be specified using the Atlassian Resource Identifier (ARI) format. Example ARI: ari:cloud:jira-core::site/1
- `searchTerm` (query, string, optional) — A search term to search the name field.
- `roleIds` (query, string, optional) — A list of role IDs. The Atlassian canonical roles are used to determine the permissions of the user against resources within the organization.

## Original description

Returns the count of groups in an organization that match the supplied parameters.
