---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization-bulk-operations
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/organization/bulk"
category: "Organization bulk operations"
writes_data: true
---
# CSM - Bulk manage organizations

**Bulk manage organizations** — `POST /api/v1/organization/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk manage organizations"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Idempotency-Key: {{param:idempotency_key}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idempotency_key` (header, string, required) — Value of the `Idempotency-Key` header.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Bulk manage multiple organizations. This allows up to 50 organizations in a single request.
**Permissions required:** Customer Service Management or Jira Service Management user. Note: Permission to update organizations can be switched to users with the Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) permission using the [Organization management](https://support.atlassian.com/jira-service-management-cloud/docs/manage-customer-organizations-using-jira-product-settings/) feature available in Jira Service Management product settings.
