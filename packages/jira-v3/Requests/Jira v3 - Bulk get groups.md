---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/group/bulk"
category: "Groups"
writes_data: false
tool_note: "[[jira_bulk_get_groups]]"
---
# Jira v3 - Bulk get groups

**Bulk get groups** — `GET /rest/api/3/group/bulk`

- Run by the tool [[jira_bulk_get_groups]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/group/bulk?startAt={{param:startAt}}&maxResults={{param:maxResults}}&groupId={{param:groupId}}&groupName={{param:groupName}}&accessType={{param:accessType}}&applicationKey={{param:applicationKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `groupId` (query, string, optional) — The ID of a group. To specify multiple IDs, pass multiple groupId parameters. For example, groupId=5b10a2844c20165700ede21g&groupId=5b10ac8d82e05b22cc7d4ef5.
- `groupName` (query, string, optional) — The name of a group. To specify multiple names, pass multiple groupName parameters. For example, groupName=administrators&groupName=jira-software-users.
- `accessType` (query, string, optional) — The access level of a group. Valid values: 'site-admin', 'admin', 'user'.
- `applicationKey` (query, string, optional) — The application key of the product user groups to search for. Valid values: 'jira-servicedesk', 'jira-software', 'jira-product-discovery', 'jira-core'.

## Original description

Returns a [paginated](#pagination) list of groups.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
