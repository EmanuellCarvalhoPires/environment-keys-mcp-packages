---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/directory
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v2/orgs/{orgId}/directories"
category: "Directory"
writes_data: false
---
# Admin Orgs - Get directories in an organization

**Get directories in an organization** — `GET /v2/orgs/{orgId}/directories`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get directories in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories?accountId={{param:accountId}}&directoryIds={{param:directoryIds}}&searchTerm={{param:searchTerm}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, optional) — Filters the results to only the directories where the specified user is a member.
- `directoryIds` (query, string, optional) — A list of directory IDs. The requestor must have permissions to administer resources linked to these directories.
- `searchTerm` (query, string, optional) — A search term to search the name field.
- `cursor` (query, string, optional) — Sets the cursor position to retrieve the next set of results. If present, all other parameters are discarded when searching.
- `limit` (query, string, optional) — The desired number of results for the search request.

## Original description

Returns a page of directories in an organization that match the supplied parameters.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:directories:admin`
