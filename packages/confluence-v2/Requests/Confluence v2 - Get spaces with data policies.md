---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/data-policies
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/data-policies/spaces"
category: "Data Policies"
writes_data: false
tool_note: "[[confluence_get_spaces_with_data_policies]]"
---
# Confluence v2 - Get spaces with data policies

**Get spaces with data policies** — `GET /data-policies/spaces`

- Run by the tool [[confluence_get_spaces_with_data_policies]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/data-policies/spaces?ids={{param:ids}}&keys={{param:keys}}&sort={{param:sort}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ids` (query, string, optional) — Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.
- `keys` (query, string, optional) — Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of spaces per result to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the `limit` parameter and
additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Only apps can make this request.
Permission to access the Confluence site ('Can use' global permission).
Only spaces that the app has permission to view will be returned.
