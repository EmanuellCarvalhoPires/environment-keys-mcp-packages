---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/organizations/{id}"
category: "Organizations"
writes_data: true
---
# Trello - Update an Organization

**Update an Organization** — `PUT /organizations/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/organizations/{{param:id}}?name={{param:name}}&displayName={{param:displayName}}&desc={{param:desc}}&website={{param:website}}&prefs/associatedDomain={{param:prefs_associatedDomain}}&prefs/externalMembersDisabled={{param:prefs_externalMembersDisabled}}&prefs/googleAppsVersion={{param:prefs_googleAppsVersion}}&prefs/boardVisibilityRestrict/org={{param:prefs_boardVisibilityRestrict_org}}&prefs/boardVisibilityRestrict/private={{param:prefs_boardVisibilityRestrict_private}}&prefs/boardVisibilityRestrict/public={{param:prefs_boardVisibilityRestrict_public}}&prefs/orgInviteRestrict={{param:prefs_orgInviteRestrict}}&prefs/permissionLevel={{param:prefs_permissionLevel}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — A new name for the organization. At least 3 lowercase letters, underscores, and numbers. Must be unique
- `displayName` (query, string, optional) — A new displayName for the organization. Must be at least 1 character long and not begin or end with a space.
- `desc` (query, string, optional) — A new description for the organization
- `website` (query, string, optional) — A URL starting with http://, https://, or null
- `prefs_associatedDomain` (query, string, optional) — The Google Apps domain to link this org to.
- `prefs_externalMembersDisabled` (query, string, optional) — Whether non-workspace members can be added to boards inside the Workspace
- `prefs_googleAppsVersion` (query, string, optional) — 1 or 2
- `prefs_boardVisibilityRestrict_org` (query, string, optional) — Who on the Workspace can make Workspace visible boards. One of admin, none, org
- `prefs_boardVisibilityRestrict_private` (query, string, optional) — Who can make private boards. One of: admin, none, org
- `prefs_boardVisibilityRestrict_public` (query, string, optional) — Who on the Workspace can make public boards. One of: admin, none, org
- `prefs_orgInviteRestrict` (query, string, optional) — An email address with optional wildcard characters. (E.g. subdomain..trello.com)
- `prefs_permissionLevel` (query, string, optional) — Whether the Workspace page is publicly visible. One of: private, public

## Original description

Update an organization
