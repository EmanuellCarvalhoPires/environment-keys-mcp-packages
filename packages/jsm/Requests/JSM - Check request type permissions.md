---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/search
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/permissions/check"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_check_request_type_permissions]]"
---
# JSM - Check request type permissions

**Check request type permissions** — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/permissions/check`

- Run by the tool [[jsm_check_request_type_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/permissions/check
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `serviceDeskId` (path, string, required) — Value of serviceDeskId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns:

 *  a list of request type IDs where the given user has permission to administer.
 *  a list of request type IDs where the given user has permission to submit the request.

If no account ID is provided, the operation returns details for the logged in user.

Note that:

 *  invalid request type IDs are ignored.
 *  a maximum of 50 request types can be checked.

**[Permissions](#permissions) required:**

 *  *Administer Jira* or *Project Administrator* to check the permissions for other users.

However, Connect apps can make a call from the app server to the product to obtain permission details for any user, without admin permission. This Connect app ability doesn't apply to calls made using AP.request() in a browser.
