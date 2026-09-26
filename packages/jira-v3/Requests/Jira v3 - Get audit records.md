---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/audit-records
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/auditing/record"
category: "Audit records"
writes_data: false
tool_note: "[[jira_get_audit_records]]"
---
# Jira v3 - Get audit records

**Get audit records** — `GET /rest/api/3/auditing/record`

- Run by the tool [[jira_get_audit_records]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/auditing/record?offset={{param:offset}}&limit={{param:limit}}&filter={{param:filter}}&from={{param:from}}&to={{param:to}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `offset` (query, string, optional) — The number of records to skip before returning the first result.
- `limit` (query, string, optional) — The maximum number of results to return.
- `filter` (query, string, optional) — The strings to match with audit field content, space separated.
- `from` (query, string, optional) — The date and time on or after which returned audit records must have been created. If to is provided from must be before to or no audit records are returned.
- `to` (query, string, optional) — The date and time on or before which returned audit results must have been created. If from is provided to must be after from or no audit records are returned.

## Original description

Returns a list of audit records. The list can be filtered to include items:

 *  where each item in `filter` has at least one match in any of these fields:
    
     *  `summary`
     *  `category`
     *  `eventSource`
     *  `objectItem.name` If the object is a user, account ID is available to filter.
     *  `objectItem.parentName`
     *  `objectItem.typeName`
     *  `changedValues.changedFrom`
     *  `changedValues.changedTo`
     *  `remoteAddress`
    
    For example, if `filter` contains *man ed*, an audit record containing `summary": "User added to group"` and `"category": "group management"` is returned.
 *  created on or after a date and time.
 *  created or or before a date and time.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
