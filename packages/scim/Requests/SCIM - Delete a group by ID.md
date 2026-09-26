---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/groups
  - api/operation/delete
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: DELETE
path: "/scim/directory/{directoryId}/Groups/{id}"
category: "Groups"
writes_data: true
---
# SCIM - Delete a group by ID

**Delete a group by ID** — `DELETE /scim/directory/{directoryId}/Groups/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Delete a group by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
DELETE https://api.atlassian.com/scim/directory/{{param:directoryId}}/Groups/{{param:id}}
Authorization: {{service.scim_auth_token}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `id` (path, string, required) — Unique SCIM id that serves as reference to the group. Use the Get groups API to get the SCIM id.

## Original description

Deletes a group to remove the group from the organization's directory.
 
 **Note**: An attempt to delete a non-existent group will fail with a 404 (Resource Not found) error.

 **Note**: Deleting a synced group from your identity provider will delete the group from your organization's directory and associated sites. 
 1. If this group is used for allocating product license (granting role in a product), then members of this group may lose access to corresponding product after group deletion. 
 2. If this group is used to grant permissions in product, then members of this group may lose their permissions in the corresponding product.
