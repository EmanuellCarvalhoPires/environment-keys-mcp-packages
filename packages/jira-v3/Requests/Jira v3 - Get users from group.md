---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/group/member"
category: "Groups"
writes_data: false
tool_note: "[[jira_get_users_from_group]]"
---
# Jira v3 - Get users from group

**Get users from group** — `GET /rest/api/3/group/member`

- Run by the tool [[jira_get_users_from_group]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/group/member?groupname={{param:groupname}}&groupId={{param:groupId}}&includeInactiveUsers={{param:includeInactiveUsers}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `groupname` (query, string, optional) — As a group's name can change, use of groupId is recommended to identify a group. The name of the group. This parameter cannot be used with the groupId parameter.
- `groupId` (query, string, optional) — The ID of the group. This parameter cannot be used with the groupName parameter.
- `includeInactiveUsers` (query, string, optional) — Include inactive users.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page (number should be between 1 and 50).

## Original description

Returns a [paginated](#pagination) list of all users in a group.

Note that users are ordered by username, however the username is not returned in the results due to privacy reasons.

**[Permissions](#permissions) required:** either of:

 *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
