---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/redactions
  - api/operation/action
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/pages/{id}/redact"
category: "Redactions"
writes_data: true
tool_note: "[[confluence_redact_content_in_a_confluence_page]]"
---
# Confluence v2 - Redact Content in a Confluence Page

**Redact Content in a Confluence Page** — `POST /pages/{id}/redact`

- Run by the tool [[confluence_redact_content_in_a_confluence_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/pages/{{param:id}}/redact
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the page to redact content from.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Redacts sensitive content in a Confluence page by replacing specified text ranges with redaction markers. 
Each redaction in the response includes a unique UUID for restoration (except code block redactions). 
The response metadata items maintain the same order as the input redaction pointers, and completely 
overlapping redactions are merged into a single redaction with one UUID.

**Note**: This endpoint requires **Atlassian Guard Premium**.
