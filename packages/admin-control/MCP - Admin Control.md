---
tags:
  - moc
  - mcp
  - api/app/admin
up: "[[MCP Tools]]"
---
# MCP - Admin Control

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 22
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/admin/control/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Policies

- [[Admin Control - Get list of policies]] — `GET /admin/control/v1/orgs/{orgId}/policies` — Get list of policies
- [[Admin Control - Create a new policy]] — `POST /admin/control/v1/orgs/{orgId}/policies` — Create a new policy ✏️
- [[Admin Control - Get single policy]] — `GET /admin/control/v1/orgs/{orgId}/policies/{policyId}` — Get single policy
- [[Admin Control - Update single policy]] — `PUT /admin/control/v1/orgs/{orgId}/policies/{policyId}` — Update single policy ✏️
- [[Admin Control - Delete single policy]] — `DELETE /admin/control/v1/orgs/{orgId}/policies/{policyId}` — Delete single policy ✏️
- [[Admin Control - Get list of policies V2]] — `GET /admin/control/v2/orgs/{orgId}/policies` — Get list of policies V2
- [[Admin Control - Create a new policy V2]] — `POST /admin/control/v2/orgs/{orgId}/policies` — Create a new policy V2 ✏️
- [[Admin Control - Get single policy V2]] — `GET /admin/control/v2/orgs/{orgId}/policies/{policyId}` — Get single policy V2
- [[Admin Control - Update single policy V2]] — `PUT /admin/control/v2/orgs/{orgId}/policies/{policyId}` — Update single policy V2 ✏️
- [[Admin Control - Publish data security policies]] — `POST /admin/control/v2/orgs/{orgId}/policies/publishDraftPolicies` — Publish data security policies ✏️
- [[Admin Control - Validate a policy]] — `GET /admin/control/v1/orgs/{orgId}/policies/{policyId}/validate` — Validate a policy

## Resources

- [[Admin Control - Get list of resources associated with a policy]] — `GET /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources` — Get list of resources associated with a policy
- [[Admin Control - Create a new policy resource]] — `POST /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources` — Create a new policy resource ✏️
- [[Admin Control - Delete all policy resources]] — `DELETE /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources` — Delete all policy resources ✏️
- [[Admin Control - Update single policy resource]] — `PUT /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}` — Update single policy resource ✏️
- [[Admin Control - Delete single policy resource]] — `DELETE /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}` — Delete single policy resource ✏️
- [[Admin Control - Get list of resources associated with a policy V2]] — `GET /admin/control/v2/orgs/{orgId}/policies/{policyId}/resources` — Get list of resources associated with a policy V2
- [[Admin Control - Add or remove policy resources V2]] — `POST /admin/control/v2/orgs/{orgId}/policies/{policyId}/resources` — Add or remove policy resources V2 ✏️
- [[Admin Control - Delete all policy resources V2]] — `DELETE /admin/control/v2/orgs/{orgId}/policies/{policyId}/resources` — Delete all policy resources V2 ✏️

## Authentication Policies

- [[Admin Control - Add users to a policy]] — `POST /admin/control/v1/orgs/{orgId}/auth-policy/{policyId}/add-users` — Add users to a policy ✏️
- [[Admin Control - Get the status of a task]] — `GET /admin/control/v1/orgs/{orgId}/auth-policy/task/{taskId}` — Get the status of a task
- [[Admin Control - Get policy information for managed users]] — `POST /admin/control/v1/orgs/{orgId}/users/auth-policies/bulk-fetch` — Get policy information for managed users
