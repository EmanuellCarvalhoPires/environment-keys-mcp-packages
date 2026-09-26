---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer-experience
  - api/operation/action
  - api/effect/write
  - api/status/experimental
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/helpcenter/{helpCenterId}/issue/{issueIdOrKey}/raise"
category: "Customer experience"
writes_data: true
---
# CSM - Raise issue on the help center

**Raise issue on the help center** — `POST /api/v1/helpcenter/{helpCenterId}/issue/{issueIdOrKey}/raise`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Raise issue on the help center"`.
- **Experimental:** sends the `X-ExperimentalApi: opt-in` header.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/helpcenter/{{param:helpCenterId}}/issue/{{param:issueIdOrKey}}/raise
Authorization: {{service.auth_token}}
Accept: application/json
X-ExperimentalApi: opt-in
```

## Parameters

- `helpCenterId` (path, string, required) — Value of helpCenterId in the path.
- `issueIdOrKey` (path, string, required) — Value of issueIdOrKey in the path.

## Original description

Raises the issue to be visible on the provided help center for the reporter to see.

If the issue has no submitted form, it attaches and submits the help center's default form.
The values submitted in the form will use the values of _Summary_ and _Description_ on the provided issue.

If a form is already attached to the issue, this operation returns `409 Conflict`.

**Permissions required:** The caller must be able to view the provided help center and be a Customer Service Management agent with `EDIT_ISSUES` permission for the provided issue.
