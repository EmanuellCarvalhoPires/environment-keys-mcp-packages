---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces"
category: "Space"
writes_data: false
tool_note: "[[confluence_get_spaces]]"
---
# Confluence v2 - Get spaces

**Get spaces** — `GET /spaces`

- Run by the tool [[confluence_get_spaces]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces?ids={{param:ids}}&keys={{param:keys}}&type={{param:type}}&status={{param:status}}&labels={{param:labels}}&favorited-by={{param:favorited_by}}&not-favorited-by={{param:not_favorited_by}}&sort={{param:sort}}&description-format={{param:description_format}}&include-icon={{param:include_icon}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ids` (query, string, optional) — Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.
- `keys` (query, string, optional) — Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.
- `type` (query, string, optional) — Filter the results to spaces based on their type.
- `status` (query, string, optional) — Filter the results to spaces based on their status.
- `labels` (query, string, optional) — Filter the results to spaces based on their labels. Multiple labels can be specified as a comma-separated list.
- `favorited_by` (query, string, optional) — Filter the results to spaces favorited by the user with the specified account ID.
- `not_favorited_by` (query, string, optional) — Filter the results to spaces NOT favorited by the user with the specified account ID.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `description_format` (query, string, optional) — The content format type to be returned in the description field of the response. If available, the representation will be available under a response field of the same name under the description field.
- `include_icon` (query, string, optional) — If the icon for the space should be fetched or not.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of spaces per result to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the `limit` parameter and
additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only spaces that the user has permission to view will be returned.
