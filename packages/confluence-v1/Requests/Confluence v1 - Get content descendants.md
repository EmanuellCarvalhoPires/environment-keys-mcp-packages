---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/descendant"
category: "Content - children and descendants"
writes_data: false
tool_note: "[[confluence_v1_get_content_descendants]]"
---
# Confluence v1 - Get content descendants

**Get content descendants** — `GET /wiki/rest/api/content/{id}/descendant`

- Run by the tool [[confluence_v1_get_content_descendants]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/descendant?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its descendants.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the children to expand, where: - attachment returns all attachments for the content. - comments returns all comments for the content.

## Original description

Returns a map of the descendants of a piece of content. This is similar
to [Get content children](#api-content-id-child-get), except that this
method returns child pages at all levels, rather than just the direct
child pages.

A piece of content has different types of descendants, depending on its type:

- `page`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `whiteboard`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `database`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `embed`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `folder`: descendant is `page`, `whiteboard`, `database`, `embed`, `folder`, `comment`, `attachment`
- `blogpost`: descendant is `comment`, `attachment`
- `attachment`: descendant is `comment`
- `comment`: descendant is `attachment`

The map will always include all descendant types that are valid for the content.
However, if the content has no instances of a descendant type, the map will
contain an empty array for that descendant type.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space, and permission to view the content if it
is a page.
