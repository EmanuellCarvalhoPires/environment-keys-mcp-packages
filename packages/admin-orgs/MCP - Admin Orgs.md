---
tags:
  - moc
  - mcp
  - api/app/admin
up: "[[MCP Tools]]"
---
# MCP - Admin Orgs

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 45
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/admin/organization/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Orgs

- [[Admin Orgs - Get organizations]] — `GET /v1/orgs` — Get organizations
- [[Admin Orgs - Get an organization by ID]] — `GET /v1/orgs/{orgId}` — Get an organization by ID

## Directory

- [[Admin Orgs - Get directories in an organization]] — `GET /v2/orgs/{orgId}/directories` — Get directories in an organization

## Users

- [[Admin Orgs - Search for users in an organization]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/users/search` — Search for users in an organization
- [[Admin Orgs - Get details of a user in a directory]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/{userId}` — Get details of a user in a directory
- [[Admin Orgs - Get managed accounts in an organization]] — `GET /v1/orgs/{orgId}/users` — Get managed accounts in an organization
- [[Admin Orgs - Invite users to an organization]] — `POST /v2/orgs/{orgId}/users/invite` — Invite users to an organization ✏️
- [[Admin Orgs - Get user role assignments]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}/role-assignments` — Get user role assignments
- [[Admin Orgs - Grant user access]] — `POST /v1/orgs/{orgId}/users/{userId}/roles/assign` — Grant user access ✏️
- [[Admin Orgs - Revoke user access]] — `POST /v1/orgs/{orgId}/users/{userId}/roles/revoke` — Revoke user access ✏️
- [[Admin Orgs - Suspend user access in directory]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}/suspend` — Suspend user access in directory ✏️
- [[Admin Orgs - Restore user access in directory]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}/restore` — Restore user access in directory ✏️
- [[Admin Orgs - Remove user from directory]] — `DELETE /v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}` — Remove user from directory ✏️
- [[Admin Orgs - Assign organization-level role]] — `POST /v1/orgs/{orgId}/users/{userId}/role-assignments/assign` — Assign organization-level role ✏️
- [[Admin Orgs - Remove organization-level role]] — `POST /v1/orgs/{orgId}/users/{userId}/role-assignments/revoke` — Remove organization-level role ✏️
- [[Admin Orgs - Get count of users in an organization]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/count` — Get count of users in an organization
- [[Admin Orgs - Get user stats in an organization]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/stats` — Get user stats in an organization
- [[Admin Orgs - User’s last active dates]] — `GET /v1/orgs/{orgId}/directory/users/{accountId}/last-active-dates` — User’s last active dates

## Groups

- [[Admin Orgs - Search for groups in an organization]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/search` — Search for groups in an organization
- [[Admin Orgs - Get group role assignments]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments` — Get group role assignments
- [[Admin Orgs - Grant access to group]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments/assign` — Grant access to group ✏️
- [[Admin Orgs - Remove access from group]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments/revoke` — Remove access from group ✏️
- [[Admin Orgs - Add user to group]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/memberships` — Add user to group ✏️
- [[Admin Orgs - Remove user from group]] — `DELETE /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/memberships/{accountId}` — Remove user from group ✏️
- [[Admin Orgs - Get group details]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}` — Get group details
- [[Admin Orgs - Delete group]] — `DELETE /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}` — Delete group ✏️
- [[Admin Orgs - Get the count of groups in an organization]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/count` — Get the count of groups in an organization
- [[Admin Orgs - Get group stats]] — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/stats` — Get group stats
- [[Admin Orgs - Create group]] — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups` — Create group ✏️

## Domains

- [[Admin Orgs - Get domains in an organization]] — `GET /v1/orgs/{orgId}/domains` — Get domains in an organization
- [[Admin Orgs - Get domain by ID]] — `GET /v1/orgs/{orgId}/domains/{domainId}` — Get domain by ID

## Events

- [[Admin Orgs - Query audit log events]] — `GET /v1/orgs/{orgId}/events` — Query audit log events
- [[Admin Orgs - Poll audit log events]] — `GET /v1/orgs/{orgId}/events-stream` — Poll audit log events
- [[Admin Orgs - Get an event by ID]] — `GET /v1/orgs/{orgId}/events/{eventId}` — Get an event by ID
- [[Admin Orgs - Get list of event actions]] — `GET /v1/orgs/{orgId}/event-actions` — Get list of event actions

## Policies

- [[Admin Orgs - Get list of policies]] — `GET /v1/orgs/{orgId}/policies` — Get list of policies
- [[Admin Orgs - Create a policy]] — `POST /v1/orgs/{orgId}/policies` — Create a policy ✏️
- [[Admin Orgs - Get a policy by ID]] — `GET /v1/orgs/{orgId}/policies/{policyId}` — Get a policy by ID
- [[Admin Orgs - Update a policy]] — `PUT /v1/orgs/{orgId}/policies/{policyId}` — Update a policy ✏️
- [[Admin Orgs - Delete a policy]] — `DELETE /v1/orgs/{orgId}/policies/{policyId}` — Delete a policy ✏️
- [[Admin Orgs - Add Resource to Policy]] — `POST /v1/orgs/{orgId}/policies/{policyId}/resources` — Add Resource to Policy ✏️
- [[Admin Orgs - Update Policy Resource]] — `PUT /v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}` — Update Policy Resource ✏️
- [[Admin Orgs - Delete Policy Resource]] — `DELETE /v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}` — Delete Policy Resource ✏️
- [[Admin Orgs - Validate Policy]] — `GET /v1/orgs/{orgId}/policies/{policyId}/validate` — Validate Policy

## Workspaces

- [[Admin Orgs - Get list of workspaces]] — `POST /v2/orgs/{orgId}/workspaces` — Get list of workspaces
