---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/search
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/search/user"
category: "Search"
writes_data: false
tool_note: "[[confluence_v1_search_users]]"
---
# Confluence v1 - Search users

**Search users** — `GET /wiki/rest/api/search/user`

- Run by the tool [[confluence_v1_search_users]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/search/user?cql={{param:cql}}&start={{param:start}}&limit={{param:limit}}&expand={{param:expand}}&sitePermissionTypeFilter={{param:sitePermissionTypeFilter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cql` (query, string, required) — The CQL query to be used for the search. See Advanced Searching using CQL for instructions on how to build a CQL query.
- `start` (query, string, optional) — The starting index of the returned users.
- `limit` (query, string, optional) — The maximum number of user objects to return per page. Note, this may be restricted by fixed system limits.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the user to expand. - operations returns the operations for the user, which are used when setting permissions.
- `sitePermissionTypeFilter` (query, string, optional) — Filters users by permission type. Use none to default to licensed users, externalCollaborator for external/guest users, and all to include all permission types.

## Original description

Searches for users using user-specific queries from the
[Confluence Query Language (CQL)](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/).

Note that CQL input queries submitted through the `/wiki/rest/api/search/user` endpoint only support user-specific fields like `user`, `user.fullname`, `user.accountid`, and `user.userkey`.

Note that some user fields may be set to null depending on the user's privacy settings.
These are: email, profilePicture, displayName, and timeZone.
