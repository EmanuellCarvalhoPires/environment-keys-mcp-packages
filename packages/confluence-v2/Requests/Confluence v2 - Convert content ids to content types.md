---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/search
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/content/convert-ids-to-types"
category: "Content"
writes_data: false
tool_note: "[[confluence_convert_content_ids_to_content_types]]"
---
# Confluence v2 - Convert content ids to content types

**Convert content ids to content types** — `POST /content/convert-ids-to-types`

- Run by the tool [[confluence_convert_content_ids_to_content_types]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/content/convert-ids-to-types
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Converts a list of content ids into their associated content types. This is useful for users migrating from v1 to v2
who may have stored just content ids without their associated type. This will return types as they should be used in v2.
Notably, this will return `inline-comment` for inline comments and `footer-comment` for footer comments, which is distinct from them
both being represented by `comment` in v1.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the requested content. Any content that the user does not have permission to view or does not exist will map to `null` in the response.
