---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/info
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/info"
category: "Info"
writes_data: false
tool_note: "[[jsm_get_info]]"
---
# JSM - Get info

**Get info** — `GET /rest/servicedeskapi/info`

- Run by the tool [[jsm_get_info]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/info
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

This method retrieves information about the Jira Service Management instance such as software version, builds, and related links.

**[Permissions](#permissions) required**: None, the user does not need to be logged in.
