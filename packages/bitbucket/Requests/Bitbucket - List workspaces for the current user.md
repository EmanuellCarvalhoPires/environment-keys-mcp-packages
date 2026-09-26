---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/user/workspaces"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_workspaces_for_the_current_user]]"
---
# Bitbucket - List workspaces for the current user

**List workspaces for the current user** — `GET /user/workspaces`

- Run by the tool [[bitbucket_list_workspaces_for_the_current_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/user/workspaces?sort={{param:sort}}&administrator={{param:administrator}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `sort` (query, string, optional) — Name of a response property to sort results (only slug is supported).
- `administrator` (query, string, optional) — Filter workspaces based on which ones the caller has admin permissions or not.

## Original description

Returns an object for each workspace accessible to the caller. This object
also contains details on whether the caller has admin permissions on the workspace
(`"administrator" = true`) or not (`"administrator" = false`).

Queries support filtering based on administrator permissions,
[sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) or
[filtering](/cloud/bitbucket/rest/intro/#filtering) by `slug`. Results can
be [paginated](/cloud/bitbucket/rest/intro/#pagination).
