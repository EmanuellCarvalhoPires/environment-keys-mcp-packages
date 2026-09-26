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
path: "/api/v1/organization/profile/bulk"
category: "Organization bulk operations"
writes_data: true
---
# CSM - Bulk manage organization profiles

**Bulk manage organization profiles** — `POST /api/v1/organization/profile/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk manage organization profiles"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/profile/bulk
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

Bulk manage multiple organization profiles with detail fields.
Allows creating, updating or upserting up to 100 organization profiles in a single request.
**Organization Identification:** To identify organizations, provide either `id` or `name`. When using UPSERT operation, note that providing only `id` (without `name`) will not create a new organization if the organization doesn't exist. The `name` field must be provided to create new organizations.
**Permissions required:** Customer Service Management or Jira Service Management user. Note: Permission to create organizations can be switched to users with the Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) permission using the [Organization management](https://support.atlassian.com/jira-service-management-cloud/docs/manage-customer-organizations-using-jira-product-settings/) feature available in Jira Service Management product settings.
