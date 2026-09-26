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
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments"
category: "Groups"
writes_data: false
---
# Admin Orgs - Get group role assignments

**Get group role assignments** — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get group role assignments"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/{{param:groupId}}/role-assignments?cursor={{param:cursor}}&limit={{param:limit}}&directoryIds={{param:directoryIds}}&resourceOwners={{param:resourceOwners}}&resourceIds={{param:resourceIds}}&roleIds={{param:roleIds}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.
- `groupId` (path, string, required) — Unique ID associated with a group.
- `cursor` (query, string, optional) — Sets the cursor position to retrieve the next set of results. If present, all other parameters are discarded when searching.
- `limit` (query, string, optional) — The desired number of results for the search request.
- `directoryIds` (query, string, optional) — A list of directory IDs. The requestor must have permissions to administer resources linked to these directories.
- `resourceOwners` (query, string, optional) — The list of resource owners to filter the results by. Used to identify resources using their owner to which the user has at least one role assigned to.
- `resourceIds` (query, string, optional) — A list of resource IDs. The resource IDs should be specified using the Atlassian Resource Identifier (ARI) format. Example ARI: ari:cloud:jira-core::site/1
- `roleIds` (query, string, optional) — A list of role IDs. The Atlassian canonical roles are used to determine the permissions of the user against resources within the organization.

## Original description

Returns a page of role assignments for a group that match the supplied parameters.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:groups:admin`
