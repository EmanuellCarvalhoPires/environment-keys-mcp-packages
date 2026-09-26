---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/csm-request
  - api/operation/action
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/request/form/helpcenter/{helpCenterId}/issue/{issueIdOrKey}/comment"
category: "CSM Request"
writes_data: true
---
# CSM - Update issue with a comment

**Update issue with a comment** — `POST /api/v1/request/form/helpcenter/{helpCenterId}/issue/{issueIdOrKey}/comment`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Update issue with a comment"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/request/form/helpcenter/{{param:helpCenterId}}/issue/{{param:issueIdOrKey}}/comment
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `helpCenterId` (path, string, required) — Value of helpCenterId in the path.
- `issueIdOrKey` (path, string, required) — Value of issueIdOrKey in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a comment to an existing issue in your customer experience project. This endpoint allows external systems to programmatically add comments with configurable visibility.

**Authentication**: This endpoint supports all authentication types including OAuth 2.0 (2LO), API token, and session authentication. Note that scopes only apply to OAuth and API token authentication.

**Permissions required:**
- OAuth authentication: `write:csm-request:jira-service-management` scope
- API token authentication: `write:csm-request:jira-service-management` scope
- Session authentication: Authenticated user
