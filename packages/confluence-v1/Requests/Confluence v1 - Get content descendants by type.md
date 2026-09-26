---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/descendant/{type}"
category: "Content - children and descendants"
writes_data: false
tool_note: "[[confluence_v1_get_content_descendants_by_type]]"
---
# Confluence v1 - Get content descendants by type

**Get content descendants by type** — `GET /wiki/rest/api/content/{id}/descendant/{type}`

- Run by the tool [[confluence_v1_get_content_descendants_by_type]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/descendant/{{param:type}}?depth={{param:depth}}&expand={{param:expand}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its descendants.
- `type` (path, string, required) — The type of descendants to return.
- `depth` (query, string, optional) — Filter the results to descendants upto a desired level of the content. Note, the maximum value supported is 100. root level of the content means immediate (level 1) descendants of the type requested.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand. - childTypes.all returns whether the content has attachments, comments, or child pages/whiteboards.
- `start` (query, string, optional) — The starting index of the returned content.
- `limit` (query, string, optional) — The maximum number of content to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns all descendants of a given type, for a piece of content. This is
similar to [Get content children by type](#api-content-id-child-type-get),
except that this method returns child pages at all levels, rather than just
the direct child pages.

A piece of content has different types of descendants, depending on its type:

- `page`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `whiteboard`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `database`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `embed`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `folder`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `blogpost`: descendant is `comment`, `attachment`
- `attachment`: descendant is `comment`
- `comment`: descendant is `attachment`

Custom content types that are provided by apps can also be returned.

If the expand query parameter is used with the `body.export_view` and/or `body.styled_view` properties, then the query limit parameter will be restricted to a maximum value of 25.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space, and permission to view the content if it
is a page.
