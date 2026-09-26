---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/csm-request
  - api/operation/create
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/request/form/external"
category: "CSM Request"
writes_data: true
---
# CSM - Create CSM request from external intake channel

**Create CSM request from external intake channel** — `POST /api/v1/request/form/external`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Create CSM request from external intake channel"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/request/form/external
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "helpCenterId": "f17913e0-58f9-4be7-b6e6-a10ca70ccb55",
  "origin": "amazon-voice",
  "summary": "Unable to access application",
  "description": "I am unable to login to the application. The error message says 'Invalid credentials'."
}
```

## Original description

Creates a CSM request from an external source. This endpoint allows external systems to submit requests programmatically to your customer experience project.

**Authentication**: This endpoint supports all authentication types including OAuth 2.0 (2LO), API token, and session authentication. Note that scopes only apply to OAuth and API token authentication.

**Reporter Email Behavior**:
- When using 2LO authentication without specifying an email, the request is created on behalf of the caller.
- When using 2LO authentication with an email, the specified user becomes the reporter.
- For API token and session authentication, only agents can specify a reporter email. Non-agents will receive a 403 Forbidden error if they attempt to set this field.

**Metadata**: You can optionally include a metadata object to provide additional context about the request. The metadata object must only contain primitive values (string, int and boolean). Nested objects or arrays are not supported and will result in a 400 Bad Request error.

**Permissions required:**
- OAuth authentication: `write:csm-request:jira-service-management` scope
- API token authentication: `write:csm-request:jira-service-management` scope
- Session authentication: Authenticated user
- To set reporter email (non-2LO): Jira Service Management agent
