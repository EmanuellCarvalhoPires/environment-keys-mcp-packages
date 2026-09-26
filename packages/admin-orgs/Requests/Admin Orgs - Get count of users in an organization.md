---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v2/orgs/{orgId}/directories/{directoryId}/users/count"
category: "Users"
writes_data: false
---
# Admin Orgs - Get count of users in an organization

**Get count of users in an organization** — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/count`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get count of users in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/users/count?accountIds={{param:accountIds}}&directoryIds={{param:directoryIds}}&resourceIds={{param:resourceIds}}&groupIds={{param:groupIds}}&mfaEnabled={{param:mfaEnabled}}&claimStatus={{param:claimStatus}}&status={{param:status}}&accountStatus={{param:accountStatus}}&membershipStatus={{param:membershipStatus}}&roleIds={{param:roleIds}}&searchTerm={{param:searchTerm}}&emailDomains={{param:emailDomains}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.
- `accountIds` (query, string, optional) — A list of user account IDs.
- `directoryIds` (query, string, optional) — A list of directory IDs. The requestor must have permissions to administer resources linked to these directories.
- `resourceIds` (query, string, optional) — A list of resource IDs. The resource IDs should be specified using the Atlassian Resource Identifier (ARI) format. Example ARI: ari:cloud:jira-core::site/1
- `groupIds` (query, string, optional) — A list of group IDs.
- `mfaEnabled` (query, string, optional) — Whether or not a managed account has two-step verification enabled on their account. If true, they have two-step verification enabled.
- `claimStatus` (query, string, optional) — The claim status for the user account. By default, both managed and unmanaged accounts are returned. - managed - Returns only managed accounts.
- `status` (query, string, optional) — The status for the user account. This status is a composite of accountStatus and membershipStatus. - active - accountStatus is active and membershipStatus is active.
- `accountStatus` (query, string, optional) — The lifecycle status of the account. - active - The account is active and can be used. - inactive - The account is inactive and doesn't have access to any resources.
- `membershipStatus` (query, string, optional) — A list of membership statuses. The membership status is the status of the user account in the organization.
- `roleIds` (query, string, optional) — A list of role IDs. The Atlassian canonical roles are used to determine the permissions of the user against resources within the organization.
- `searchTerm` (query, string, optional) — A search term to search the nickname and email fields.
- `emailDomains` (query, string, optional) — The email domain to filter the results. The email domain will be used to search against the account email domain. For example, get all users with the @atlassian.com or @example.com email domain.

## Original description

Returns a count of users in an organization that match the supplied parameters. By default, users in all your directories and all your managed accounts are counted (including managed accounts that aren’t in a directory). 

To count users in a directory only, use the `directoryIds` field. To count your managed accounts, regardless if they’re in a directory or not, use the `claimStatus` field.
