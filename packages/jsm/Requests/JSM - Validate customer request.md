---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/search
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/request/validate"
category: "Request"
writes_data: false
tool_note: "[[jsm_validate_customer_request]]"
---
# JSM - Validate customer request

**Validate customer request** — `POST /rest/servicedeskapi/request/validate`

- Run by the tool [[jsm_validate_customer_request]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/validate
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Validates a customer request payload without creating (persisting) a request.

This endpoint runs exactly the same structural and semantic validations as [Create customer request](#api-request-post) \\u2014 including ProForma form validation \\u2014 but performs **no mutation**: no issue is created and no side effects (attachments, comments, analytics) run.

The response is intentionally verbose and structured so that it can be consumed by automated agents (for example an LLM repairing an invalid payload): every failure carries a machine-readable location (field id / form entity) and a human-readable reason. A valid payload returns HTTP 200 with \{@code valid: true\}; an invalid payload returns HTTP 400 with \{@code valid: false\} together with the field, form and general validation errors.

**[Permissions](#permissions) required**: Permission to create requests in the specified service desk.
