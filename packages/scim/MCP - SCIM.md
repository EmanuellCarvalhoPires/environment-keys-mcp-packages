---
tags:
  - moc
  - mcp
  - api/app/scim
up: "[[MCP Tools]]"
---
# MCP - SCIM

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 24
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Users

- [[SCIM - Get a user by ID]] — `GET /scim/directory/{directoryId}/Users/{userId}` — Get a user by ID
- [[SCIM - Update user via user attributes]] — `PUT /scim/directory/{directoryId}/Users/{userId}` — Update user via user attributes ✏️
- [[SCIM - Delete a user]] — `DELETE /scim/directory/{directoryId}/Users/{userId}` — Delete a user ✏️
- [[SCIM - Update user by ID (PATCH)]] — `PATCH /scim/directory/{directoryId}/Users/{userId}` — Update user by ID (PATCH) ✏️
- [[SCIM - Get users]] — `GET /scim/directory/{directoryId}/Users` — Get users
- [[SCIM - Create a user]] — `POST /scim/directory/{directoryId}/Users` — Create a user ✏️

## Groups

- [[SCIM - Get a group by ID]] — `GET /scim/directory/{directoryId}/Groups/{id}` — Get a group by ID
- [[SCIM - Update a group by ID]] — `PUT /scim/directory/{directoryId}/Groups/{id}` — Update a group by ID ✏️
- [[SCIM - Delete a group by ID]] — `DELETE /scim/directory/{directoryId}/Groups/{id}` — Delete a group by ID ✏️
- [[SCIM - Update a group by ID (PATCH)]] — `PATCH /scim/directory/{directoryId}/Groups/{id}` — Update a group by ID (PATCH) ✏️
- [[SCIM - Get groups]] — `GET /scim/directory/{directoryId}/Groups` — Get groups
- [[SCIM - Create a group]] — `POST /scim/directory/{directoryId}/Groups` — Create a group ✏️

## Schemas

- [[SCIM - Get all schemas]] — `GET /scim/directory/{directoryId}/Schemas` — Get all schemas
- [[SCIM - Get user schemas]] — `GET /scim/directory/{directoryId}/Schemas/urn{ietf}{params}{scim}{schemas}{core}:2.0{User}` — Get user schemas
- [[SCIM - Get group schemas]] — `GET /scim/directory/{directoryId}/Schemas/urn{ietf}{params}{scim}{schemas}{core}:2.0{Group}` — Get group schemas
- [[SCIM - Get user enterprise extension schemas]] — `GET /scim/directory/{directoryId}/Schemas/urn{ietf}{params}{scim}{schemas}{extension}{enterprise}:2.0{User}` — Get user enterprise extension schemas
- [[SCIM - Get feature metadata]] — `GET /scim/directory/{directoryId}/ServiceProviderConfig` — Get feature metadata

## Service Provider Configuration

- [[SCIM - Get resource types]] — `GET /scim/directory/{directoryId}/ResourceTypes` — Get resource types
- [[SCIM - Get user resource types]] — `GET /scim/directory/{directoryId}/ResourceTypes/User` — Get user resource types
- [[SCIM - Get group resource types]] — `GET /scim/directory/{directoryId}/ResourceTypes/Group` — Get group resource types

## Admin APIs

- [[SCIM - Delete user in SCIM DB]] — `DELETE /admin/user-provisioning/v1/org/{orgId}/user/{AAID}/onlyDeleteUserInDB` — Delete user in SCIM DB ✏️
- [[SCIM - Get SCIM links for an account]] — `GET /admin/user-provisioning/v1/org/{orgId}/user/{aaId}/get-scim-links` — Get SCIM links for an account
- [[SCIM - Get SCIM Links for an email]] — `POST /admin/user-provisioning/v1/org/{orgId}/get-scim-links-for-email` — Get SCIM Links for an email
- [[SCIM - Unlink a SCIM user from their Atlassian account]] — `PATCH /admin/user-provisioning/v1/org/{orgId}/scimDirectoryId/{scimDirectoryId}/scimUserId/{scimUserId}/unlink` — Unlink a SCIM user from their Atlassian account ✏️
