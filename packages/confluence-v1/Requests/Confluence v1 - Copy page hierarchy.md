---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/pagehierarchy/copy"
category: "Content - children and descendants"
writes_data: true
tool_note: "[[confluence_v1_copy_page_hierarchy]]"
---
# Confluence v1 - Copy page hierarchy

**Copy page hierarchy** — `POST /wiki/rest/api/content/{id}/pagehierarchy/copy`

- Run by the tool [[confluence_v1_copy_page_hierarchy]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/pagehierarchy/copy
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Copy page hierarchy allows the copying of an entire hierarchy of pages and their associated properties, permissions and attachments.
 The id path parameter refers to the content id of the page to copy, and the new parent of this copied page is defined using the destinationPageId in the request body.
 The titleOptions object defines the rules of renaming page titles during the copy;
 for example, search and replace can be used in conjunction to rewrite the copied page titles.

 Response example:
 
 {
      "id" : "1180606",
      "links" : {
           "status" : "/rest/api/longtask/1180606"
      }
 }
 
 Use the /longtask/ REST API to get the copy task status.
