---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/pages/{id}"
category: "Page"
writes_data: false
tool_note: "[[confluence_get_page_by_id]]"
---
# Confluence v2 - Get page by id

**Get page by id** — `GET /pages/{id}`

- Run by the tool [[confluence_get_page_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}?body-format={{param:body_format}}&get-draft={{param:get_draft}}&status={{param:status}}&version={{param:version}}&include-labels={{param:include_labels}}&include-properties={{param:include_properties}}&include-operations={{param:include_operations}}&include-likes={{param:include_likes}}&include-versions={{param:include_versions}}&include-version={{param:include_version}}&include-favorited-by-current-user-status={{param:include_favorited_by_current_user_status}}&include-webresources={{param:include_webresources}}&include-collaborators={{param:include_collaborators}}&include-direct-children={{param:include_direct_children}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the page to be returned. If you don't know the page ID, use Get pages and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `get_draft` (query, string, optional) — Retrieve the draft version of this page.
- `status` (query, string, optional) — Filter the page being retrieved by its status.
- `version` (query, string, optional) — Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
- `include_labels` (query, string, optional) — Includes labels associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes content properties associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_operations` (query, string, optional) — Includes operations associated with this page in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_likes` (query, string, optional) — Includes likes associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_versions` (query, string, optional) — Includes versions associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_version` (query, string, optional) — Includes the current version associated with this page in the response. By default this is included and can be omitted by setting the value to false.
- `include_favorited_by_current_user_status` (query, string, optional) — Includes whether this page has been favorited by the current user.
- `include_webresources` (query, string, optional) — Includes web resources that can be used to render page content on a client.
- `include_collaborators` (query, string, optional) — Includes collaborators on the page.
- `include_direct_children` (query, string, optional) — Includes direct children of the page, as defined in the ChildrenResponse object.

## Original description

Returns a specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the page and its corresponding space.
