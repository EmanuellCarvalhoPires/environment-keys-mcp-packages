---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/group/picker"
category: "Group"
writes_data: false
tool_note: "[[confluence_v1_search_groups_by_partial_query]]"
---
# Confluence v1 - Search groups by partial query

**Search groups by partial query** — `GET /wiki/rest/api/group/picker`

- Run by the tool [[confluence_v1_search_groups_by_partial_query]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/group/picker?query={{param:query}}&start={{param:start}}&limit={{param:limit}}&shouldReturnTotalSize={{param:shouldReturnTotalSize}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, required) — the search term used to query results.
- `start` (query, string, optional) — The starting index of the returned groups.
- `limit` (query, string, optional) — The maximum number of groups to return per page. Note, this is restricted to a maximum limit of 200 groups.
- `shouldReturnTotalSize` (query, string, optional) — Whether to include total size parameter in the results. Note, fetching total size property is an expensive operation; use it if your use case needs this value.

## Original description

Get search results of groups by partial query provided.
