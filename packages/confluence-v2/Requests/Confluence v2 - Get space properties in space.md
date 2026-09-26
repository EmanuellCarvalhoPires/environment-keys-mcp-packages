---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces/{space-id}/properties"
category: "Space Properties"
writes_data: false
tool_note: "[[confluence_get_space_properties_in_space]]"
---
# Confluence v2 - Get space properties in space

**Get space properties in space** — `GET /spaces/{space-id}/properties`

- Run by the tool [[confluence_get_space_properties_in_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:space_id}}/properties?key={{param:key}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `space_id` (path, string, required) — The ID of the space for which space properties should be returned.
- `key` (query, string, optional) — The key of the space property to retrieve. This should be used when a user knows the key of their property, but needs to retrieve the id for use in other methods.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all properties for the given space. Space properties are a key-value storage associated with a space.
The limit parameter specifies the maximum number of results returned in a single response. Use the `link` response header
to paginate through additional results.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission) and 'View' permission for the space.
