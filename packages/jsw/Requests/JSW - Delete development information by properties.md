---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/development-information
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/devinfo/0.10/bulkByProperties"
category: "Development Information"
writes_data: true
---
# JSW - Delete development information by properties

**Delete development information by properties** — `DELETE /rest/devinfo/0.10/bulkByProperties`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete development information by properties"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/devinfo/0.10/bulkByProperties?_updateSequenceId={{param:_updateSequenceId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `_updateSequenceId` (query, string, optional) — An optional property to use to control deletion. Only stored data with an updateSequenceId less than or equal to that provided will be deleted.

## Original description

Deletes development information entities which have all the provided properties. Repositories which have properties that match ALL of the properties (i.e. treated as an AND), and all their related development information (such as commits, branches and pull requests), will be deleted. For example if request is `DELETE bulk?accountId=123&projectId=ABC` entities which have properties `accountId=123` and `projectId=ABC` will be deleted. Optional param `_updateSequenceId` is no longer supported. Deletion is performed asynchronously: specified entities will eventually be removed from Jira.
