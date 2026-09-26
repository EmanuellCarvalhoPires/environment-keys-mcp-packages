---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/label
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/labels"
category: "Label"
writes_data: false
tool_note: "[[confluence_get_labels]]"
---
# Confluence v2 - Get labels

**Get labels** — `GET /labels`

- Run by the tool [[confluence_get_labels]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/labels?label-id={{param:label_id}}&prefix={{param:prefix}}&cursor={{param:cursor}}&sort={{param:sort}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `label_id` (query, string, optional) — Filters on label ID. Multiple IDs can be specified as a comma-separated list.
- `prefix` (query, string, optional) — Filters on label prefix. Multiple IDs can be specified as a comma-separated list.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `limit` (query, string, optional) — Maximum number of labels per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all labels. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only labels that the user has permission to view will be returned.
