---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/request/{issueIdOrKey}"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_customer_request_by_id_or_key]]"
---
# JSM - Get customer request by id or key

**Get customer request by id or key** — `GET /rest/servicedeskapi/request/{issueIdOrKey}`

- Run by the tool [[jsm_get_customer_request_by_id_or_key]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or Key of the customer request to be returned
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the customer request to expand, where: serviceDesk returns additional service desk details.

## Original description

This method returns a customer request.

**[Permissions](#permissions) required**: Permission to access the specified service desk.

**Response limitations**: For customers, only a request they created, was created on their behalf, or they are participating in will be returned.

**Note:** `requestFieldValues` does not include hidden fields. To get a list of request type fields that includes hidden fields, see [/rest/servicedeskapi/servicedesk/\{serviceDeskId\}/requesttype/\{requestTypeId\}/field](https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-servicedesk/#api-rest-servicedeskapi-servicedesk-servicedeskid-requesttype-requesttypeid-field-get)
