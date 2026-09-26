---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard/{dashboardId}/gadget"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_get_gadgets]]"
---
# Jira v3 - Get gadgets

**Get gadgets** — `GET /rest/api/3/dashboard/{dashboardId}/gadget`

- Run by the tool [[jira_get_gadgets]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/gadget?moduleKey={{param:moduleKey}}&uri={{param:uri}}&gadgetId={{param:gadgetId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `moduleKey` (query, string, optional) — The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: moduleKey=key:one&moduleKey=key:two.
- `uri` (query, string, optional) — The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: uri=/rest/example/uri/1&uri=/rest/example/uri/2.
- `gadgetId` (query, string, optional) — The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: gadgetId=10000&gadgetId=10001.

## Original description

Returns a list of dashboard gadgets on a dashboard.

This operation returns:

 *  Gadgets from a list of IDs, when `id` is set.
 *  Gadgets with a module key, when `moduleKey` is set.
 *  Gadgets from a list of URIs, when `uri` is set.
 *  All gadgets, when no other parameters are set.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
