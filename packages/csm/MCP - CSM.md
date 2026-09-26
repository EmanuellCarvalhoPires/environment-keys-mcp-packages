---
tags:
  - moc
  - mcp
  - api/app/csm
up: "[[MCP Tools]]"
---
# MCP - CSM

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 60
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Organization

- [[CSM - Get organization detail fields]] — `GET /api/v1/organization/details` — Get organization detail fields
- [[CSM - Create organization detail field]] — `POST /api/v1/organization/details` — Create organization detail field ✏️
- [[CSM - Edit organization detail field]] — `PUT /api/v1/organization/details/{fieldName}` — Edit organization detail field ✏️
- [[CSM - Delete organization detail field]] — `DELETE /api/v1/organization/details/{fieldName}` — Delete organization detail field ✏️
- [[CSM - Get organization]] — `GET /api/v1/organization/{organizationId}` — Get organization
- [[CSM - Update organization]] — `PUT /api/v1/organization/{organizationId}` — Update organization ✏️
- [[CSM - Delete organization]] — `DELETE /api/v1/organization/{organizationId}` — Delete organization ✏️
- [[CSM - Set organization detail]] — `PUT /api/v1/organization/{organizationId}/details` — Set organization detail ✏️
- [[CSM - Get organization entitlements]] — `GET /api/v1/organization/{organizationId}/entitlement` — Get organization entitlements
- [[CSM - Create organization entitlement]] — `POST /api/v1/organization/{organizationId}/entitlement` — Create organization entitlement ✏️
- [[CSM - Create organization]] — `POST /api/v1/organization` — Create organization ✏️
- [[CSM - Fetch multiple organizations]] — `POST /api/v1/organization/fetch` — Fetch multiple organizations
- [[CSM - Get organization profile]] — `GET /api/v1/organization/profile/{organizationId}` — Get organization profile
- [[CSM - Create organization profile]] — `POST /api/v1/organization/profile` — Create organization profile ✏️
- [[CSM - Fetch multiple organization profiles]] — `POST /api/v1/organization/profile/fetch` — Fetch multiple organization profiles

## Organization bulk operations

- [[CSM - Bulk create organization detail field definitions]] — `POST /api/v1/organization/details/definitions/bulk` — Bulk create organization detail field definitions ✏️
- [[CSM - Bulk manage organization profiles]] — `POST /api/v1/organization/profile/bulk` — Bulk manage organization profiles ✏️
- [[CSM - Bulk manage organizations]] — `POST /api/v1/organization/bulk` — Bulk manage organizations ✏️
- [[CSM - Bulk manage organizations' detail field values]] — `POST /api/v1/organization/details/bulk` — Bulk manage organizations' detail field values ✏️

## Customer

- [[CSM - Get customer detail fields]] — `GET /api/v1/customer/details` — Get customer detail fields
- [[CSM - Create customer detail field]] — `POST /api/v1/customer/details` — Create customer detail field ✏️
- [[CSM - Edit customer detail field]] — `PUT /api/v1/customer/details/{fieldName}` — Edit customer detail field ✏️
- [[CSM - Delete customer detail field]] — `DELETE /api/v1/customer/details/{fieldName}` — Delete customer detail field ✏️
- [[CSM - Get customer]] — `GET /api/v1/customer/{customerId}` — Get customer
- [[CSM - Get customer accessible customer experiences]] — `GET /api/v1/customer/{customerId}/customer-experiences` — Get customer accessible customer experiences
- [[CSM - Search customer by detail field and value]] — `POST /api/v1/customer/search-by-detail-field` — Search customer by detail field and value
- [[CSM - Set customer detail]] — `PUT /api/v1/customer/{customerId}/details` — Set customer detail ✏️
- [[CSM - Get customer entitlements]] — `GET /api/v1/customer/{customerId}/entitlement` — Get customer entitlements
- [[CSM - Create customer entitlement]] — `POST /api/v1/customer/{customerId}/entitlement` — Create customer entitlement ✏️
- [[CSM - Create customer account]] — `POST /api/v1/customer` — Create customer account ✏️
- [[CSM - Get customer account]] — `GET /api/v1/customer/account/{customerId}` — Get customer account
- [[CSM - Update customer account]] — `PUT /api/v1/customer/account/{customerId}` — Update customer account ✏️
- [[CSM - Delete customer account]] — `DELETE /api/v1/customer/account/{customerId}` — Delete customer account ✏️
- [[CSM - Get customer profile]] — `GET /api/v1/customer/profile/{customerId}` — Get customer profile
- [[CSM - Create customer profile]] — `POST /api/v1/customer/profile` — Create customer profile ✏️
- [[CSM - Fetch multiple customer profiles]] — `POST /api/v1/customer/profile/fetch` — Fetch multiple customer profiles

## Customer bulk operations

- [[CSM - Bulk create customer detail field definitions]] — `POST /api/v1/customer/details/definitions/bulk` — Bulk create customer detail field definitions ✏️
- [[CSM - Bulk manage customers' detail field values]] — `POST /api/v1/customer/details/bulk` — Bulk manage customers' detail field values ✏️
- [[CSM - Bulk manage customer accounts]] — `POST /api/v1/customer/bulk` — Bulk manage customer accounts ✏️
- [[CSM - Bulk manage multiple customer profiles]] — `POST /api/v1/customer/profile/bulk` — Bulk manage multiple customer profiles ✏️

## Product

- [[CSM - Get products]] — `GET /api/v1/product` — Get products
- [[CSM - Create product]] — `POST /api/v1/product` — Create product ✏️
- [[CSM - Get product]] — `GET /api/v1/product/{productId}` — Get product
- [[CSM - Rename product]] — `PUT /api/v1/product/{productId}` — Rename product ✏️
- [[CSM - Delete product]] — `DELETE /api/v1/product/{productId}` — Delete product ✏️

## Entitlement

- [[CSM - Get entitlement detail fields]] — `GET /api/v1/entitlement/details` — Get entitlement detail fields
- [[CSM - Create entitlement detail field]] — `POST /api/v1/entitlement/details` — Create entitlement detail field ✏️
- [[CSM - Edit entitlement detail field]] — `PUT /api/v1/entitlement/details/{fieldName}` — Edit entitlement detail field ✏️
- [[CSM - Delete entitlement detail field]] — `DELETE /api/v1/entitlement/details/{fieldName}` — Delete entitlement detail field ✏️
- [[CSM - Get entitlement]] — `GET /api/v1/entitlement/{entitlementId}` — Get entitlement
- [[CSM - Delete entitlement]] — `DELETE /api/v1/entitlement/{entitlementId}` — Delete entitlement ✏️
- [[CSM - Set entitlement detail]] — `PUT /api/v1/entitlement/{entitlementId}/details` — Set entitlement detail ✏️
- [[CSM - Get entitlements]] — `GET /api/v1/entitlements` — Get entitlements

## CSM Request

- [[CSM - Create CSM request from external intake channel]] — `POST /api/v1/request/form/external` — Create CSM request from external intake channel ✏️
- [[CSM - Update issue with a comment]] — `POST /api/v1/request/form/helpcenter/{helpCenterId}/issue/{issueIdOrKey}/comment` — Update issue with a comment ✏️

## Task

- [[CSM - Get task status]] — `GET /api/v1/tasks/{taskId}` — Get task status

## Customer experience

- [[CSM - Get organizations with access to a Customer Experience]] — `GET /api/v1/helpcenter/{helpCenterId}/access/organization` — Get organizations with access to a Customer Experience
- [[CSM - Grant organizations access to a Customer Experience]] — `POST /api/v1/helpcenter/{helpCenterId}/access/organization` — Grant organizations access to a Customer Experience ✏️
- [[CSM - Remove an organization from a Customer Experience]] — `DELETE /api/v1/helpcenter/{helpCenterId}/access/organization/{organizationId}` — Remove an organization from a Customer Experience ✏️
- [[CSM - Raise issue on the help center]] — `POST /api/v1/helpcenter/{helpCenterId}/issue/{issueIdOrKey}/raise` — Raise issue on the help center ✏️
